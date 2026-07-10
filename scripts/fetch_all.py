#!/usr/bin/env python3
"""AI 热点抓取 — 多源抓取脚本（仅用标准库，零依赖）。

用法:
    python3 fetch_all.py                 # 抓过去 24h，输出到 待审核/YYYY-MM-DD/
    python3 fetch_all.py --hours 48      # 自定义时间窗
    python3 fetch_all.py --force         # 覆盖当日已有产物

输出:
    待审核/YYYY-MM-DD/items.json         # 统一 schema 的全部条目（给 Claude 整理用）
    待审核/YYYY-MM-DD/fetch_report.json  # 各源成败报告

铁律: 单源失败不阻塞; 不重试; 所有条目摘要截断，Claude 不需要读任何原始 HTML/RSS。
"""

import argparse
import gzip
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from zoneinfo import ZoneInfo

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

WORKDIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = WORKDIR / "配置.json"

# ---------------------------------------------------------------- 基础工具

def http_get(url, headers=None, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
        if resp.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    return data


def get_json(url, headers=None):
    return json.loads(http_get(url, headers).decode("utf-8", "replace"))


def get_text(url, headers=None):
    return http_get(url, headers).decode("utf-8", "replace")


def strip_html(s, limit=200):
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = html.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s[:limit]


def parse_dt(s):
    """尽力解析 ISO8601 / RFC822 时间字符串为 aware datetime，失败返回 None。"""
    if not s:
        return None
    s = s.strip()
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except ValueError:
        pass
    try:
        dt = parsedate_to_datetime(s)
        # -0000/无时区的 RFC822 日期会返回 naive datetime，不补齐会让 within() 抛 TypeError
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except Exception:
        return None


def within(dt, hours):
    if dt is None:
        return True  # 无时间戳的条目不按时间过滤（榜单快照类）
    return datetime.now(timezone.utc) - dt <= timedelta(hours=hours)


def canon_url(url):
    """URL 规范化: 去跟踪参数、去 fragment、统一协议、去末尾斜杠。"""
    try:
        p = urllib.parse.urlsplit(url)
        q = [(k, v) for k, v in urllib.parse.parse_qsl(p.query)
             if not k.lower().startswith(("utm_", "ref", "spm", "from"))]
        return urllib.parse.urlunsplit(
            ("https", p.netloc.lower(), p.path.rstrip("/"),
             urllib.parse.urlencode(q), ""))
    except Exception:
        return url


def make_item(source, lang, title, url, heat, heat_val, published, summary="", native_ai=False):
    return {
        "source": source, "lang": lang,
        "title": strip_html(title, 150), "url": url,
        "heat": heat, "heat_val": round(float(heat_val), 1),
        "published_at": published.isoformat() if published else "",
        "summary": strip_html(summary, 200), "native_ai": native_ai,
    }

# ---------------------------------------------------------------- AI 相关性过滤

def build_matchers(cfg):
    # 用 (?<!\w)/(?!\w) 而非 \b：词表里 "A\.I\." 这类以标点结尾的模式在 \b 下永远匹配不到
    en_re = re.compile(r"(?<!\w)(" + "|".join(cfg["keywords_en"]) + r")(?!\w)", re.IGNORECASE)
    zh_words = cfg["keywords_zh"]

    def en_match(text):
        return bool(en_re.search(text or ""))

    def zh_match(text):
        t = text or ""
        return any(w in t for w in zh_words) or bool(en_re.search(t))

    return en_match, zh_match

# ---------------------------------------------------------------- 各源适配器
# 每个适配器: fetch_xxx(cfg, hours, en_match, zh_match) -> list[item]

def fetch_hackernews(cfg, hours, en_match, zh_match):
    items, seen = [], set()
    # ① 当前首页里 AI 相关的
    data = get_json("https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=30")
    for h in data.get("hits", []):
        title = h.get("title") or ""
        if h["objectID"] in seen or not en_match(title):
            continue
        seen.add(h["objectID"])
        url = h.get("url") or f"https://news.ycombinator.com/item?id={h['objectID']}"
        pts, nc = h.get("points") or 0, h.get("num_comments") or 0
        items.append(make_item("hackernews", "en", title, url,
                               f"首页·{pts}分/{nc}评论", pts,
                               parse_dt(h.get("created_at"))))
    # ② 时间窗内的 AI 新帖（多个关键词查询，客户端过滤分数）
    ts = int(time.time()) - hours * 3600
    for q in cfg["hn_queries"]:
        u = ("https://hn.algolia.com/api/v1/search_by_date?"
             + urllib.parse.urlencode({"query": q, "tags": "story", "hitsPerPage": 30,
                                       "numericFilters": f"created_at_i>{ts}"}))
        for h in get_json(u).get("hits", []):
            pts = h.get("points") or 0
            if h["objectID"] in seen or pts < cfg["hn_min_points"]:
                continue
            # Algolia 是全文搜索，正文提一句 AI 也会命中 query，标题再过一遍词表防误入
            if not en_match(h.get("title") or ""):
                continue
            seen.add(h["objectID"])
            url = h.get("url") or f"https://news.ycombinator.com/item?id={h['objectID']}"
            items.append(make_item("hackernews", "en", h.get("title") or "", url,
                                   f"{pts}分/{h.get('num_comments') or 0}评论", pts,
                                   parse_dt(h.get("created_at"))))
    return items


def fetch_hf_papers(cfg, hours, en_match, zh_match):
    items = []
    for e in get_json("https://huggingface.co/api/daily_papers?limit=50"):
        p = e.get("paper") or {}
        pid, up = p.get("id"), p.get("upvotes") or 0
        if not pid or up < cfg["hf_paper_min_upvotes"]:
            continue
        # 该 API 一次返回可横跨 10 天，不过滤会让热门论文每天重复入报；放宽到 72h 兼顾批次延迟
        if not within(parse_dt(e.get("publishedAt")), max(hours, 72)):
            continue
        items.append(make_item("hf_papers", "en", p.get("title") or "",
                               f"https://huggingface.co/papers/{pid}",
                               f"{up}赞", up, parse_dt(e.get("publishedAt")),
                               p.get("summary") or "", native_ai=True))
    return items


def fetch_hf_trending(cfg, hours, en_match, zh_match):
    items = []
    for kind, n in (("models", 15), ("spaces", 8)):
        for m in get_json(f"https://huggingface.co/api/{kind}?sort=trendingScore&limit={n}"):
            mid = m.get("id") or m.get("modelId") or ""
            score = m.get("trendingScore") or 0
            likes = m.get("likes") or 0
            label = "模型" if kind == "models" else "Space"
            items.append(make_item("hf_trending", "en", f"[{label}] {mid}",
                                   f"https://huggingface.co/{'spaces/' if kind=='spaces' else ''}{mid}",
                                   f"趋势分{score}·{likes}赞", score, None, native_ai=True))
    return items


def fetch_github_trending(cfg, hours, en_match, zh_match):
    page = get_text("https://github.com/trending?since=daily")
    items = []
    for block in page.split("<article")[1:]:
        m = re.search(r'href="/([^/"]+/[^/"]+)"', block)
        if not m:
            continue
        slug = m.group(1)
        desc_m = re.search(r'<p class="col-9[^"]*">\s*(.*?)\s*</p>', block, re.S)
        desc = strip_html(desc_m.group(1)) if desc_m else ""
        stars_m = re.search(r"([\d,]+)\s+stars today", block)
        stars = int(stars_m.group(1).replace(",", "")) if stars_m else 0
        if not en_match(slug + " " + desc):
            continue
        items.append(make_item("github_trending", "en", slug,
                               f"https://github.com/{slug}",
                               f"今日+{stars}星", stars, None, desc))
    return items


def _rss_entries(url, headers=None):
    """解析 RSS/Atom，返回 [(title, link, pubdate_str, desc)]。"""
    text = get_text(url, headers)
    # 有些源(如 smol.ai)的正文混有非法控制字符，会弄崩 XML 解析，先清洗
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text)
    # 剥掉 XML 声明：已按 UTF-8 解码成 str，保留 encoding="gb2312" 之类声明会让 ET 拒绝解析
    text = re.sub(r"^\s*<\?xml[^>]*\?>", "", text)
    root = ET.fromstring(text)
    out = []
    for it in root.iter("item"):  # RSS 2.0
        g = lambda tag: (it.findtext(tag) or "")
        content = it.findtext("{http://purl.org/rss/1.0/modules/content/}encoded") or ""
        out.append((g("title"), g("link"), g("pubDate"), content or g("description")))
    if not out:  # Atom
        ns = "{http://www.w3.org/2005/Atom}"
        for e in root.iter(f"{ns}entry"):
            link = ""
            for l in e.findall(f"{ns}link"):
                if l.get("rel") in (None, "alternate"):
                    link = l.get("href") or ""
                    break
            out.append((e.findtext(f"{ns}title") or "", link,
                        e.findtext(f"{ns}published") or e.findtext(f"{ns}updated") or "",
                        e.findtext(f"{ns}summary") or e.findtext(f"{ns}content") or ""))
    return out


def fetch_techmeme(cfg, hours, en_match, zh_match):
    items = []
    for title, link, pub, desc in _rss_entries("https://www.techmeme.com/feed.xml"):
        dt = parse_dt(pub)
        if not within(dt, hours) or not en_match(title):
            continue
        items.append(make_item("techmeme", "en", title, link, "Techmeme头条", 50, dt, desc))
    return items


def fetch_smolai(cfg, hours, en_match, zh_match):
    entries = _rss_entries("https://news.smol.ai/rss.xml")
    items = []
    for title, link, pub, content in entries[:2]:
        dt = parse_dt(pub)
        if not within(dt, 72):  # 周一可能拿到周五的期号，放宽到 72h
            continue
        digest = strip_html(content, cfg["smolai_digest_chars"])
        items.append({**make_item("smolai", "en", title, link, "每日X/Reddit/Discord综述",
                                  100, dt, native_ai=True),
                      "summary": digest})
        break  # 只要最新一期
    return items


def fetch_zpravobot(cfg, hours, en_match, zh_match):
    items = []
    errors = []
    for acc in cfg["zpravobot_accounts"]:
        try:
            for title, link, pub, desc in _rss_entries(f"https://zpravobot.news/@{acc}.rss")[:10]:
                dt = parse_dt(pub)
                if not within(dt, hours):
                    continue
                text = strip_html(desc or title, 200)
                items.append(make_item("kol_x", "en", f"@{acc}: {text[:80]}", link,
                                       "官方号/KOL推文", 30, dt, text, native_ai=True))
        except Exception as e:  # 单账号失败不影响其他账号
            errors.append(f"@{acc}: {e}")
    if errors and not items:
        raise RuntimeError("; ".join(errors))
    # 部分账号失败也要浮出水面，否则镜像号下线会无声丢数月推文
    return items, ("部分账号失败: " + "; ".join(errors)) if errors else ""


def fetch_vendor_blogs(cfg, hours, en_match, zh_match):
    """抓各大厂官方博客/newsroom 的最新发布——最权威的"官号"一手来源。
    清单在 配置.json vendor_blogs：{name, url, native_ai}。native_ai=false 的需关键词过滤。"""
    items, errors = [], []
    for b in cfg.get("vendor_blogs", []):
        try:
            for title, link, pub, desc in _rss_entries(b["url"]):
                dt = parse_dt(pub)
                if not within(dt, hours):
                    continue
                if not b.get("native_ai") and not en_match(title + " " + strip_html(desc, 200)):
                    continue
                items.append(make_item("vendor_blog", "en", f"[{b['name']}] {title}", link,
                                       f"官方·{b['name']}", 12, dt, desc,
                                       native_ai=b.get("native_ai", False)))
        except Exception as e:  # 单个厂商 feed 失败不拖累其他
            errors.append(f"{b['name']}: {e}")
    if errors and not items:
        raise RuntimeError("; ".join(errors))
    return items, ("部分厂商feed失败: " + "; ".join(errors)) if errors else ""


def fetch_bluesky(cfg, hours, en_match, zh_match):
    """抓 AI 博主/掌舵人在 Bluesky 的最新原创帖（原生号 + X 镜像号）。
    补 zpravobot 拿不到的个人 KOL；用 api.bsky.app（public.api 域的 searchPosts 会 403）。"""
    items, errors = [], []
    for h in cfg.get("bluesky_handles", []):
        handle = h["handle"]
        name = h.get("name", handle)
        try:
            url = ("https://api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed"
                   f"?limit=15&actor={urllib.parse.quote(handle)}")
            for fi in get_json(url).get("feed", []):
                post = fi.get("post") or {}
                rec = post.get("record") or {}
                if rec.get("reply") or fi.get("reason"):  # 跳过回复和转发，只要原创发言
                    continue
                text = rec.get("text") or ""
                dt = parse_dt(rec.get("createdAt"))
                if not text or not within(dt, hours):
                    continue
                rkey = (post.get("uri") or "").rsplit("/", 1)[-1]
                link = f"https://bsky.app/profile/{handle}/post/{rkey}" if rkey else f"https://bsky.app/profile/{handle}"
                items.append(make_item("kol_bsky", "en", f"{name}: {text[:80]}", link,
                                       f"KOL·{name}", 30, dt, text, native_ai=True))
        except Exception as e:  # 单账号失败不拖累其他账号
            errors.append(f"{handle}: {e}")
    if errors and not items:
        raise RuntimeError("; ".join(errors))
    return items, ("部分账号失败: " + "; ".join(errors)) if errors else ""


def fetch_weibo(cfg, hours, en_match, zh_match):
    data = get_json("https://weibo.com/ajax/side/hotSearch",
                    headers={"Referer": "https://weibo.com/"})
    raw = data.get("data", {}).get("realtime", [])
    if not raw:  # 正常热搜必有几十条，空说明接口结构变化或被风控，不能静默全绿
        raise RuntimeError("榜单原始数据为空——接口结构变化或被风控")
    items = []
    for i, e in enumerate(raw, 1):
        word = e.get("word") or ""
        if not zh_match(word):
            continue
        num = e.get("num") or 0
        label = e.get("label_name") or ""
        q = urllib.parse.quote(f"#{word}#")
        items.append(make_item("weibo", "zh", word,
                               f"https://s.weibo.com/weibo?q={q}",
                               f"热搜#{i}·{num}{('·' + label) if label else ''}",
                               1000 - i, None))
    return items


def fetch_zhihu(cfg, hours, en_match, zh_match):
    data = get_json("https://api.zhihu.com/topstory/hot-list?limit=50")
    raw = data.get("data", [])
    if not raw:
        raise RuntimeError("榜单原始数据为空——接口结构变化或被风控")
    items = []
    for i, e in enumerate(raw, 1):
        t = e.get("target") or {}
        title = t.get("title") or ""
        if not zh_match(title):
            continue
        api_url = t.get("url") or ""
        m = re.search(r"/questions?/(\d+)", api_url)
        url = f"https://www.zhihu.com/question/{m.group(1)}" if m else api_url
        heat = e.get("detail_text") or f"热榜#{i}"
        items.append(make_item("zhihu", "zh", title, url,
                               f"热榜#{i}·{heat}", 1000 - i, None,
                               t.get("excerpt") or ""))
    return items


def fetch_bilibili(cfg, hours, en_match, zh_match):
    data = get_json("https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all")
    raw = (data.get("data") or {}).get("list", [])
    if not raw:
        raise RuntimeError("榜单原始数据为空——接口结构变化或被风控")
    items = []
    for e in raw:
        title, tname = e.get("title") or "", e.get("tname") or ""
        if not zh_match(title + " " + tname):
            continue
        stat = e.get("stat") or {}
        view = stat.get("view") or 0
        bvid = e.get("bvid") or ""
        if not bvid:  # 缺 id 会构造出相同 URL，在去重里互相撞车
            continue
        items.append(make_item("bilibili", "zh", title,
                               f"https://www.bilibili.com/video/{bvid}",
                               f"{view // 10000}万播放·{tname}", view, None,
                               e.get("desc") or ""))
    return items


def _fetch_rss_source(source, url, hours, match, native_ai=False, lang="zh", heat="资讯", heat_val=10):
    items = []
    for title, link, pub, desc in _rss_entries(url):
        dt = parse_dt(pub)
        if not within(dt, hours):
            continue
        if not native_ai and not match(title):
            continue
        items.append(make_item(source, lang, title, link, heat, heat_val, dt, desc,
                               native_ai=native_ai))
    return items


def fetch_qbitai(cfg, hours, en_match, zh_match):
    return _fetch_rss_source("qbitai", "https://www.qbitai.com/feed", hours,
                             zh_match, native_ai=True, heat="量子位")


def fetch_ithome(cfg, hours, en_match, zh_match):
    return _fetch_rss_source("ithome", "https://www.ithome.com/rss/", hours,
                             zh_match, heat="IT之家")


def fetch_36kr(cfg, hours, en_match, zh_match):
    return _fetch_rss_source("kr36", "https://36kr.com/feed", hours,
                             zh_match, heat="36氪")


def fetch_juejin(cfg, hours, en_match, zh_match):
    u = ("https://api.juejin.cn/content_api/v1/content/article_rank"
         "?category_id=6809637773935378440&type=hot")
    items = []
    for e in get_json(u).get("data", [])[:20]:
        c = e.get("content") or {}
        if not c.get("content_id"):
            continue
        counter = e.get("content_counter") or {}
        view = counter.get("view") or 0
        items.append(make_item("juejin", "zh", c.get("title") or "",
                               f"https://juejin.cn/post/{c.get('content_id')}",
                               f"AI热榜·{view}阅读", view, None, native_ai=True))
    return items


# --- 英文科技媒体 RSS（补足公司/产品/行业新闻深度，此前英文侧只有 Techmeme） ---
# native AI 频道无需过滤；Ars 是泛科技需过滤。heat_val=8 让媒体条目排在有真实热度的源之后。

def fetch_thedecoder(cfg, hours, en_match, zh_match):
    return _fetch_rss_source("thedecoder", "https://the-decoder.com/feed/", hours,
                             en_match, native_ai=True, lang="en", heat="The Decoder", heat_val=8)


def fetch_techcrunch(cfg, hours, en_match, zh_match):
    return _fetch_rss_source("techcrunch", "https://techcrunch.com/category/artificial-intelligence/feed/",
                             hours, en_match, native_ai=True, lang="en", heat="TechCrunch", heat_val=8)


def fetch_theverge(cfg, hours, en_match, zh_match):
    return _fetch_rss_source("theverge", "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml",
                             hours, en_match, native_ai=True, lang="en", heat="The Verge", heat_val=8)


def fetch_venturebeat(cfg, hours, en_match, zh_match):
    # 用主 feed + 过滤：/category/ai/feed/ 已冻结不更新（最新条目停在数月前），主 feed 才是新鲜的
    return _fetch_rss_source("venturebeat", "https://venturebeat.com/feed/",
                             hours, en_match, native_ai=False, lang="en", heat="VentureBeat", heat_val=8)


def fetch_mittr(cfg, hours, en_match, zh_match):
    return _fetch_rss_source("mit_tr", "https://www.technologyreview.com/topic/artificial-intelligence/feed",
                             hours, en_match, native_ai=True, lang="en", heat="MIT科技评论", heat_val=8)


def fetch_arstechnica(cfg, hours, en_match, zh_match):
    return _fetch_rss_source("arstechnica", "https://feeds.arstechnica.com/arstechnica/technology-lab",
                             hours, en_match, native_ai=False, lang="en", heat="Ars Technica", heat_val=8)


# --- 中文补充 ---

def fetch_leiphone(cfg, hours, en_match, zh_match):
    return _fetch_rss_source("leiphone", "https://www.leiphone.com/feed", hours,
                             zh_match, heat="雷锋网")


# --- ProductHunt：AI 新产品发布（Atom，标题即产品名，过滤出 AI 相关） ---

def fetch_producthunt(cfg, hours, en_match, zh_match):
    items = []
    for title, link, pub, desc in _rss_entries("https://www.producthunt.com/feed"):
        dt = parse_dt(pub)
        if not within(dt, hours):
            continue
        if not (en_match(title) or en_match(desc)):
            continue
        items.append(make_item("producthunt", "en", title, link, "PH新品", 8, dt, desc))
    return items


# --- NewsNow 聚合：补抖音/百度/头条社会热榜里的 AI 条目（排名当热度，需过滤） ---

def fetch_newsnow(cfg, hours, en_match, zh_match):
    items, errors, reached = [], [], 0
    src_names = {"douyin": "抖音", "baidu": "百度", "toutiao": "头条", "kuaishou": "快手"}
    for sid in cfg.get("newsnow_ids", ["douyin", "baidu", "toutiao"]):
        try:
            data = get_json(f"https://newsnow.busiyi.world/api/s?id={sid}")
            reached += 1  # 能连通就算这个源健康（哪怕过滤后 0 条 AI）
            for i, e in enumerate(data.get("items", []), 1):
                title = e.get("title") or ""
                url = e.get("url") or ""
                if not url or not zh_match(title):
                    continue
                items.append(make_item("newsnow", "zh", title, url,
                                       f"{src_names.get(sid, sid)}热榜#{i}", 500 - i, None))
        except Exception as e:  # 公共实例偶发 500，单子源失败很常见
            errors.append(f"{sid}: {e}")
    if reached == 0:  # 只有全部子源都连不上才算本源失败
        raise RuntimeError("全部子源不可达: " + "; ".join(errors))
    return items, ("部分子源异常: " + "; ".join(errors)) if errors else ""


ADAPTERS = {
    "hackernews": fetch_hackernews,
    "hf_papers": fetch_hf_papers,
    "hf_trending": fetch_hf_trending,
    "github_trending": fetch_github_trending,
    "techmeme": fetch_techmeme,
    "smolai": fetch_smolai,
    "vendor_blogs": fetch_vendor_blogs,
    "zpravobot": fetch_zpravobot,
    "bluesky": fetch_bluesky,
    "weibo": fetch_weibo,
    "zhihu": fetch_zhihu,
    "bilibili": fetch_bilibili,
    "qbitai": fetch_qbitai,
    "ithome": fetch_ithome,
    "kr36": fetch_36kr,
    "juejin": fetch_juejin,
    # 扩展源（2026-07-10 新增）
    "thedecoder": fetch_thedecoder,
    "techcrunch": fetch_techcrunch,
    "theverge": fetch_theverge,
    "venturebeat": fetch_venturebeat,
    "mit_tr": fetch_mittr,
    "arstechnica": fetch_arstechnica,
    "leiphone": fetch_leiphone,
    "producthunt": fetch_producthunt,
    "newsnow": fetch_newsnow,
}

# ---------------------------------------------------------------- 主流程

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=int, default=None)
    ap.add_argument("--force", action="store_true", help="覆盖当日已有产物")
    args = ap.parse_args()

    cfg = json.loads(CONFIG_PATH.read_text("utf-8"))
    hours = args.hours or cfg["hours"]
    tz = ZoneInfo(cfg["timezone"])
    today = datetime.now(tz).strftime("%Y-%m-%d")
    outdir = WORKDIR / "待审核" / today
    items_path = outdir / "items.json"

    if items_path.exists() and not args.force:
        print(f"IDEMPOTENT_SKIP: {items_path} 已存在（--force 可覆盖）")
        sys.exit(0)
    outdir.mkdir(parents=True, exist_ok=True)

    en_match, zh_match = build_matchers(cfg)
    all_items, report = [], []
    seen_urls = set()

    for name, fn in ADAPTERS.items():
        if not cfg["sources"].get(name, True):
            report.append({"source": name, "ok": None, "count": 0, "note": "配置中已关闭"})
            continue
        t0 = time.time()
        try:
            result = fn(cfg, hours, en_match, zh_match)
            fetched, note = result if isinstance(result, tuple) else (result, "")
            kept = []
            for it in fetched:
                cu = canon_url(it["url"])
                if cu in seen_urls:
                    continue
                seen_urls.add(cu)
                kept.append(it)
            kept.sort(key=lambda x: -x["heat_val"])
            all_items.extend(kept)
            entry = {"source": name, "ok": True, "count": len(kept),
                     "secs": round(time.time() - t0, 1)}
            if note:
                entry["note"] = note
            report.append(entry)
            print(f"  ✓ {name}: {len(kept)} 条 ({time.time()-t0:.1f}s)"
                  + (f" ⚠ {note}" if note else ""))
        except Exception as e:
            report.append({"source": name, "ok": False, "count": 0,
                           "error": f"{type(e).__name__}: {e}", "secs": round(time.time() - t0, 1)})
            print(f"  ✗ {name}: {type(e).__name__}: {e}")

    ok_n = sum(1 for r in report if r["ok"])
    enabled_n = sum(1 for r in report if r["ok"] is not None)
    meta = {"date": today, "window_hours": hours,
            "generated_at": datetime.now(tz).isoformat(timespec="seconds"),
            "sources_ok": ok_n, "sources_enabled": enabled_n,
            "total_items": len(all_items)}

    (outdir / "fetch_report.json").write_text(
        json.dumps({"meta": meta, "sources": report}, ensure_ascii=False, indent=1), "utf-8")

    payload = json.dumps({"meta": meta, "items": all_items}, ensure_ascii=False, indent=1)
    if enabled_n and ok_n / enabled_n < 0.4:
        # 失败时绝不写 items.json：否则幂等检查会把当天锁死在残缺数据上
        (outdir / "items.failed.json").write_text(payload, "utf-8")
        print(f"\nFATAL: 超过 60% 的源失败，本次抓取不可用。"
              f"残缺数据存为 items.failed.json，未写 items.json（不影响重跑）")
        sys.exit(2)

    items_path.write_text(payload, "utf-8")
    print(f"\n完成: {len(all_items)} 条 | 源 {ok_n}/{enabled_n} 正常 | → {items_path}")


if __name__ == "__main__":
    main()
