# 信息源清单与坑（2026-07-09/10 本机实测）

MVP 已接入 14 源。端点细节都在 `scripts/fetch_all.py` 的适配器里，这里记「为什么这样写」和已知的坑，供维护时查。

## 已接入

| 源 | 类型 | 关键坑 |
|---|---|---|
| hackernews | 热度(points) | Algolia `numericFilters` 的 `>` 必须 URL 编码 `%3E`；points 过滤参数不可靠，客户端过滤（配置 hn_min_points=20） |
| hf_papers | 热度(upvotes) | daily_papers 本身就是"昨天的论文"，天然契合 |
| hf_trending | 热度(trendingScore) | models + spaces 两个端点 |
| github_trending | 热度(stars today) | 无官方 API，HTML 正则解析，**页面改版会挂**，挂了看 `<article>` 结构改正则 |
| techmeme | 上榜即热度 | 标题自带信源署名，信息密度高 |
| smolai | 每日综述 | 一条 item = 全天 X/Reddit/Discord 热议；摘要截 2500 字符给 Claude 提炼；周一可能是上周五的期号（放宽 72h） |
| zpravobot | KOL 推文镜像 | 个人维护的 Mastodon 实例，**可能停摆**；单账号失败不影响其他账号 |
| weibo | 榜单排名+num | **必须带 Referer: https://weibo.com/**，裸请求 403 |
| zhihu | 榜单排名+热度文本 | **必须用 api.zhihu.com 域**，www 域的端点要登录 |
| bilibili | view/like | 参数是 `rid` 不是 `tid`；需要普通 UA |
| qbitai | AI 垂直媒体 | 100% AI，机器之心 RSS 已死后的替代 |
| ithome | 泛科技快讯 | 量大，关键词过滤后仍是中文条目主力 |
| kr36 | 商业动态 | 只用 /feed；快讯 API 要签名，别碰 |
| juejin | 开发者热榜 | category_id=6809637773935378440 是"人工智能"分类 |
| thedecoder | 英文AI媒体 | 100% AI，native_ai 无需过滤 |
| techcrunch | 英文AI频道 | /category/artificial-intelligence/feed/，天然AI |
| theverge | 英文AI频道 | Atom，天然AI |
| venturebeat | 英文AI媒体 | **必须用主 feed /feed/ 并过滤**——/category/ai/feed/ 已冻结停更数月，是坑 |
| mit_tr | 英文AI频道 | 更新慢，日常 0-2 条正常 |
| arstechnica | 英文泛科技 | 需过滤；更新慢，多数日 0-2 条 |
| leiphone | 中文AI媒体 | 需过滤；首条常是频道名"雷峰网"要在解析层忽略 |
| producthunt | AI新品 | Atom，标题即产品名，过滤出 AI 相关；多数日 3-8 条 |
| newsnow | 社会热榜聚合 | 抖音/百度/头条榜里捞 AI；**低产源**——平时社会新闻刷屏 0 条，大 AI 新闻日才有；个人实例无 SLA |
| zpravobot | X 官号/掌舵人镜像 | Mastodon RSS。账号在 `配置.json` zpravobot_accounts：sama/OpenAI/AnthropicAI/googledeepmind/xai/perplexity_ai |
| bluesky | AI 博主/掌舵人 | api.bsky.app getAuthorFeed，只取原创帖（跳过回复/转发）。账号在 `配置.json` bluesky_handles：Mollick/Willison/Lambert/Karpathy镜像/Carmack镜像 |

## KOL / 官号信源实测结论（2026-07-10，决定谁能抓）

X 免费抓取已死，KOL/官号只能靠**镜像**，且大部分账号根本没有可用镜像。逐个探测过 65+ 账号，结论：

**zpravobot（X→Mastodon 镜像）实际有镜像且新鲜的**：OpenAI ✓ · AnthropicAI ✓ · GoogleDeepMind ✓ · sama ✓ · perplexity_ai ✓ · xai(8天前较旧) · StabilityAI(基本停更)。
**zpravobot 无镜像(404)**：Meta/MistralAI/nvidia/cohere/huggingface/midjourney 等所有其他官号；**全部中国厂商**(deepseek_ai/Qwen/Kimi/Zhipu/MiniMax…)；除 sama 外**所有个人**(马斯克/Hassabis/Pichai/Nadella/LeCun/Ng/Dario…)。

**Bluesky 原生活跃(值得抓)**：Ethan Mollick(每天发) · Simon Willison(活跃) · Nathan Lambert(半活跃)。
**Bluesky 镜像号活跃**：Karpathy(karpathy-mirr.selfhosted.social) · Carmack(id-aa-carmack-x)。
**Bluesky 有号但已弃用(数月~1年+没更新，不加)**：Yann LeCun · Gary Marcus · swyx · Jeremy Howard · Sebastian Raschka · Mistral CEO Arthur Mensch · HuggingFace 官号。

**结论**：官号能拿 3 大实验室 + Altman + Perplexity；个人能拿 Karpathy/Carmack/Mollick/Willison/Lambert。**其余(马斯克、中国厂商、Meta/NVIDIA 官号、多数掌舵人)无免费途径**——它们的动态主要靠 smol.ai 综述(每天读 544 个 X 账号)间接覆盖。想要更全需付费 X API 或用 Claude in Chrome 人工看。

## 死亡名单（别再试）

- Reddit 匿名 JSON：本机 IP 被 Cloudflare 拦，403（要接需注册免费 OAuth app）
- Nitter 全部公共实例、RSSHub 全部公共实例：反爬墙/停服
- 机器之心 RSS：已随改版下线
- tophub.today：反爬严；InBrief API（ai-news-skill）：404 失效
- `public.api.bsky.app` 的 searchPosts：403，要用 `api.bsky.app`（Bluesky 尚未接入，扩展项）

## 扩展候选（下一版可加）

- anyknew `www.anyknew.com/api/v1/sites/{site}`：微博/知乎的降级链互备
- Bluesky `api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed`：镜像号 karpathy-mirr.selfhosted.social / sama-mirr.selfhosted.social / anthropicbot.bsky.social
- Reddit OAuth（r/LocalLLaMA 等 5 个 sub，需 jacob 注册免费 app 才能绕过匿名 403）
- 36氪快讯：`36kr.com/newsflashes` 页内 `window.initialState` JSON（脆弱）
- 已评估但**不加**：钛媒体（AI 占比太低，首屏集成灶/医药/美妆）、arXiv（HF 论文已覆盖热门研究，原始 arXiv 每天 15+ 篇纯噪声）、InfoQ（与掘金重叠）、虎嗅（超时不稳）、PingWest（RSS 405）

## 关键词表维护

词表在 `配置.json`（keywords_zh / keywords_en）。原则沿用 GitHub-AI-Trending 的经验：保持高质量词 50–100 个；每次看日报发现误放/漏放，就来改词表。英文词是正则（注意转义），短词自带 `\b` 词边界防止 "air" 误命中 "ai"。
