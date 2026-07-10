# AI 热点抓取（ai-hotspot-daily）

每天从 25 个中英文信息源抓取过去 24 小时的 AI 热点，由 Claude Code 整理成一份分类日报。零 API 成本：抓取脚本纯 Python 标准库（零依赖），所有信息源均为免费匿名接口，整理跑在 Claude Code 定时任务里。

## 信息源（全部实测可用）

**英文**：Hacker News（Algolia API）· HuggingFace Daily Papers / Trending · GitHub Trending · Techmeme · smol.ai AINews（X/Reddit/Discord 每日综述）· TechCrunch AI · The Verge AI · VentureBeat · The Decoder · MIT 科技评论 · Ars Technica · ProductHunt

**官方博客**：OpenAI · Google DeepMind · Google AI · Mistral · HuggingFace · Apple ML · NVIDIA · 微软研究院（各厂官方 newsroom RSS，最权威的一手发布）

**KOL / 官号推文**：zpravobot（OpenAI / Anthropic / DeepMind / Sam Altman / Perplexity 等 X 官号镜像）· Bluesky（Ethan Mollick / Simon Willison / Nathan Lambert / Karpathy / Carmack）— 详见 `reference/sources.md` 的实测结论

**中文**：微博热搜 · 知乎热榜 · B站排行 · 量子位 · IT之家 · 36氪 · 掘金 AI 热榜 · 雷锋网 · NewsNow（抖音/百度/头条热榜聚合）

## 结构

```
├── SKILL.md              # Claude Code skill 工作流（4 步流水线）
├── 配置.json              # 源开关 / 时间窗 / 中英文关键词表
├── scripts/fetch_all.py   # 多源抓取脚本（stdlib-only）
├── reference/sources.md   # 源清单、已知坑、死亡名单、扩展候选
└── 待审核/YYYY-MM-DD/     # 每日产物：items.json + fetch_report.json + AI热点日报.md
```

## 用法

```bash
# 手动跑一次抓取（幂等，当日已有产物则跳过；--force 覆盖）
python3 scripts/fetch_all.py

# 完整流水线（抓取 + 日报整理）在 Claude Code 里触发：
#   "抓一下AI热点" / "跑一下热点日报"
```

设计原则：脚本做确定性工作（抓取/过滤/去重），Claude 只读压缩后的 items.json 做判断性整理；单源失败不阻塞；超 60% 源失败视为本次不可用（不写 items.json，避免锁死幂等）；绝不自动发布。
