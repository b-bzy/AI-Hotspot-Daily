---
name: github-ai-trending
description: 每天抓 GitHub Trending 日榜，筛出 AI 相关的前 3 个项目（不足 3 个用非 AI 项目按 today's stars 倒序补足），按正经科技媒体风格写一篇 800–1500 字的中文介绍文章，保存到本地待审核区。绝不自动发布。当用户说"跑一下 github trending"/"今天的 GitHub AI 热点"/"整理今日 AI 开源项目"/"github 日榜跑一下"/"抓今天 AI 项目写文章"等，使用本 skill。也支持定时任务每天早上 9:00 自动跑。
---

# GitHub AI Trending 每日内容工作流

每天抓一次 GitHub Trending 日榜，挑出 AI 相关的前 3 个项目（不足 3 个时用非 AI 项目补足 3 个），写一篇 800–1500 字、**正经科技媒体风格**的中文介绍文章，存到本地待审核区。**不自动发布**，由 jacob 人工审核后手动归档。

---

## 路径约定（重要）

skill 内置文件（read-only，跟随 skill 安装）：
- `SKILL.md`（本文件）
- `配置.yaml`
- `reference/ai-keywords.md`
- `reference/style-tech-media.md`
- `reference/article-template.md`
- `scripts/fetch_trending.py`

用户工作区文件（persistent，跟随 jacob 的工作目录）：

```
{WORKSPACE}/GitHub-AI-Trending/
├── 选题历史.md                ← 防重复（每天追加）
├── 待审核/YYYY-MM-DD/         ← 自动产出
│   ├── raw-trending.json
│   ├── repos-meta.json
│   ├── raw/                  ← API 原始 dump，debug 用
│   └── article.md
├── 已发布/                    ← jacob 手动归档
└── 失败记录/                  ← 失败时的快照
```

**（2026-07-12 迁移后）工作区已固定为 AI-Hotspot-Daily 仓库内的子目录**：
`/Users/jacob/Desktop/账号运营的内容/AI热点抓取/GitHub-Trending/`
——本目录既是本地工作区，也是 git 仓库（b-bzy/AI-Hotspot-Daily）的一部分。上文 `{WORKSPACE}/GitHub-AI-Trending/` 一律按此路径理解。核心文件（SKILL.md/配置.yaml/reference/选题历史.md）与 待审核/ 都在此目录内，不再区分"skill 内置"与"用户工作区"。`scripts/fetch_trending.py` 不存在（历史遗留描述），抓取直接用 WebFetch 抓 `https://github.com/trending?since=daily` 的 HTML 由 Claude 解析。

---

## 步骤 1：选今天写哪 3 个项目

### 1.1 幂等性检查

跑之前先看 `{WORKSPACE}/GitHub-AI-Trending/待审核/YYYY-MM-DD/article.md` 是不是已经存在。存在就退出，写报告"今日已产出，跳过"，**不要覆盖**。

### 1.2 抓 Trending 日榜

```bash
cd "{WORKSPACE}/GitHub-AI-Trending"
mkdir -p "待审核/$(TZ=Asia/Shanghai date +%F)"
python3 scripts/fetch_trending.py > "待审核/$(TZ=Asia/Shanghai date +%F)/raw-trending.json"
```

> 时区按 Asia/Shanghai 算"今天"，避免 UTC 错位。
>
> 脚本会优先抓 `https://github.com/trending?since=daily` 的 HTML，失败自动 fallback 到 OSSInsight 公开 API。两个都失败 → 写报告"今日数据源全部不可用"，退出。

### 1.3 AI 相关性筛选

读 `reference/ai-keywords.md` 的关键词词表，对当天 Trending 项目逐个打分（规则在词表文件里）。

- 得分 ≥ 3 进入候选池
- 候选池里再扣掉 `选题历史.md` 里 90 天内出现过的 `owner/name`
- 剩余的项目让 Claude 二判，挑出真正"今日 AI 热点"的前 3
- 二判时优先考虑：① 信息密度（能写满 200–400 字）；② 数据可信度（star 数与项目形态是否匹配）；③ 多样性（避免三个都是同一细分主题）

### 1.4 不足 3 个时的补位逻辑

**jacob 的决策**：AI 候选不足 3 个时，从 trending 榜里按 today's stars 倒序，把非 AI 项目补进来凑齐 3 个。**绝不只发 1–2 个**。

补位项目在文章里照样按"正经科技媒体风格"写，不需要硬凑 AI 角度。

### 1.5 记录今日选题

把三个 `owner/name` 追加到 `选题历史.md`，格式：

```
YYYY-MM-DD: owner1/repo1, owner2/repo2, owner3/repo3
```

---

## 步骤 2：拉每个项目的 Metadata + README

每个项目调 GitHub REST API（**无 token，限流 60 req/h，三个项目大约 6–8 次调用，注意控制**）：

```bash
curl -s -i "https://api.github.com/repos/OWNER/REPO" -H "Accept: application/vnd.github+json" -H "User-Agent: AlexBot"
# 返回头里有 topics（不需要单独调 topics endpoint）
curl -s -i "https://api.github.com/repos/OWNER/REPO/readme" -H "Accept: application/vnd.github+json" -H "User-Agent: AlexBot"
```

需要的字段：

| 字段 | 来源 |
|---|---|
| description | meta.json `.description` |
| 主语言 | meta.json `.language` |
| 协议 | meta.json `.license.spdx_id` |
| 总 star | meta.json `.stargazers_count` |
| 今日新增 star | trending 抓取里的 `stars_today` |
| 创建时间 | meta.json `.created_at` |
| 主页 | meta.json `.homepage` |
| topics | meta.json `.topics` |
| README 摘要 | readme.md base64 解码后前 4000 字符 |

README 取前 4000 字符（约 200 行）。超出截断，文末标注 "[README 截断，完整版见仓库]"。

**限流处理**：API 返回 403 + `X-RateLimit-Remaining: 0` → 立刻停止，**不要重试**。把已拿到的项目数据落盘，写报告"GitHub API 限流，剩余 X 个项目未拉取，请明天再跑或配置 PAT"。

把三个项目的数据合成一个 `repos-meta.json` 存到 `待审核/YYYY-MM-DD/`，debug 用。

---

## 步骤 3：写正文

按 `reference/article-template.md` 的模板写，**严格遵守** `reference/style-tech-media.md` 的风格约束（禁用词、必带数字、不夸大）。

文章保存到 `待审核/YYYY-MM-DD/article.md`。

### 正文写作硬约束（**不要忘**）

- **禁用词**：炸裂、王炸、颠覆、震撼、革命、神器、yyds、绝绝子、太牛了、屌爆、绝杀（完整清单见 style 文件）
- **要用的词**：发布、迭代、开源、提升、对比、值得关注、可用于、适合、相比……提高了 X%
- **数据要带具体数字**：star 数、版本号、benchmark 数据，没有具体数就别说"性能强"这种话
- **不夸大**：1k star 说"刚起步"，10k+ 才说"已有规模"，10w+ 才是"明星项目"
- **不喊口号**：不写"AI 改变世界"这种空话，写"X 公司用它做了 Y，每天处理 Z 个请求"这种具体的

### 标题生成

让 Claude 一次性生成 3 个候选标题（趋势型 / 项目型 / 数据型各一），写到 article.md 最上面的注释里供 jacob 挑：

```markdown
<!--
标题候选：
1. 今日 GitHub AI 项目：本地推理框架重新成主线
2. {头名项目} 登顶今日 Trending，另两个项目同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24h 新增超 X star
当前正在使用：候选 1
-->
```

### 自查清单（写完必跑）

- grep 禁用词清单 → 应该 0 命中
- 全文 emoji → 应该只有 🔗（每个项目链接前一个）
- 字数 → 800–1500 区间
- 数据栏 → 4 列填齐，没有 `—` 或空格

---

## 步骤 4：写执行报告

报告写到 Claude 的 `outputs/` 目录（不写到 workspace，避免把 jacob 的目录搞乱），文件名 `任务执行报告_YYYY-MM-DD.md`。

报告必须包含：执行时间、数据源、抓取数、AI 候选数、去重剔除数、入选 3 个 + 一句话定位、淘汰名单+原因、文章字数、3 个标题候选、API 限流余额、产物路径、需要 jacob 做的事。

---

## 步骤 4.5：推送 GitHub → Telegram 自动送达（2026-07-12 迁移新增）

文章与执行报告写完后，在仓库根目录执行：

```bash
cd "/Users/jacob/Desktop/账号运营的内容/AI热点抓取"
D=$(TZ=Asia/Shanghai date +%F)
git add "GitHub-Trending/待审核/$D/" "GitHub-Trending/选题历史.md"
git commit -m "GitHub-Trending: 文章 $D"
git pull --rebase -q origin main; git push origin main
```

- 推送后仓库的 `trending-push` Action 自动把当日 `article.md` 发到 Telegram（Hotspot 机器人窗口）。**Claude 不要再手动发 Telegram**
- push 失败不阻塞：产物已在本地，报告注明"未推送，需手动 git push"即可，最多重试一次

## 步骤 5：归档（由 jacob 手动）

Claude **不**自动移动文件到 `已发布/`。由 jacob 在小红书/公众号或其他平台发完后，手动把 `待审核/YYYY-MM-DD/` 整体拖到 `已发布/`。

---

## 失败处理（统一规则）

任何步骤报错都按这套走：

1. **不重试**（API 抓取最多重试 1 次）
2. 当前产物原样留在 `待审核/YYYY-MM-DD/`，错误日志同目录
3. 报告写明：卡在哪一步 / 错误原文 / jacob 要做什么
4. 退出，等 jacob 处理后手动重跑

**常见失败场景预案**：

| 场景 | 处理 |
|---|---|
| 主源 HTML 解析失败 | 脚本自动切备源（OSSInsight），无需 Claude 介入 |
| 两源都失败 | 写报告"今日数据源全部不可用"，退出 |
| AI 候选 + 非 AI 补位仍不足 3 个（极小概率） | 有几个写几个，报告说明 |
| GitHub API 限流 | 写报告"剩余 N 个未拉取，建议明天再跑或配置 PAT" |
| README 拉取失败 | 该项目降级为"仅 metadata 版"，文章里标注 "[README 暂不可访问]" |
| 选题历史里写过的全部命中 | 选题池清空 90 天前的记录，重新挑 |

---

## 配置

运行时配置在 `配置.yaml`，关键开关：

- `ai_filter.min_score: 3` — AI 相关性打分阈值
- `dedup_window_days: 90` — 去重窗口
- `readme_max_chars: 4000` — README 截断长度
- `article_target_chars: 1200` — 文章目标字数

改这个文件不需要改 SKILL.md。
