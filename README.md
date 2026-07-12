# AI-Hotspot-Daily · AI 内容运营自动化平台

5 条流水线,全云端运行(claude.ai routine + GitHub Actions),零 API 成本,产物统一推送 Telegram。从"每日 AI 热点日报工具"演化而来,现覆盖日报、周报、GitHub 项目文章、资讯笔记四类内容的自动生产。

## 每日节奏(GST 迪拜时间)

| 时间 | 产物 | 说明 |
|---|---|---|
| 07:17 | **资讯笔记** 正文+标题包 | 从早报选题深耕,机器之心风格,评审迭代,卡兹克标题包 |
| 07:43 | 日报原始数据 | GitHub Action 抓 25 个中英文源 |
| 08:17 | **AI 热点日报 + 爆款选题榜** | 8 板块分类日报 + TOP10 选题卡 |
| 08:47 | **GitHub Trending 文章** | AI 前 3 项目,科技媒体风格,800-1500 字 |
| 周日 08:27 | **周选题 TOP10 + 串烧初稿** | 一周早报拉通,选题榜 + 口播串烧稿 |

## 📖 文档(从这里找一切)

- **[docs/00-仓库总览.md](docs/00-仓库总览.md)** ← 平台地图/时间表/目录去向/排障速查
- [docs/01-日报模块.md](docs/01-日报模块.md) · [docs/02-周报模块.md](docs/02-周报模块.md) · [docs/03-GitHub-Trending模块.md](docs/03-GitHub-Trending模块.md) · [docs/04-资讯笔记模块.md](docs/04-资讯笔记模块.md)

## 目录速览

```
待审核/          ①日报产物(items.json + 日报 + 选题榜)   ← SKILL.md/配置.json/reference/ 服务于此模块
周报/            ②周报产物
GitHub-Trending/ ③Trending 模块(自包含: SKILL+配置+reference+选题历史+待审核)
资讯笔记/         ④笔记模块(reference 4个skill规范 + 每日三文件)
scripts/         抓取脚本(fetch_all.py) + TG推送(send_telegram.py,全模块共用)
.github/         5个Action: fetch-daily + 4个telegram推送
docs/            全部说明文档
```

## 设计原则

- **脚本干确定性重活,Claude 只做判断性整理**(绝不读原始网页烧额度)
- **抓取放 GitHub Actions**(全网通),云端 routine 沙箱只放行 github.com
- **绝不自动发布到内容平台**——一切产物到 Telegram 送审,人工决定发布
- **失败安全**:幂等检查/单源失败不阻塞/宁缺毋滥不编造
- token 只存 GitHub Secrets 与本地 gitignore 文件,永不进仓库
