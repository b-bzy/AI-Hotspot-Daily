# 模块文档 · ③GitHub AI Trending 每日文章

> 每天抓 GitHub Trending 日榜,筛出 AI 相关前 3 项目,写一篇 800-1500 字"正经科技媒体风格"的中文介绍文章。2026-07-12 从独立工作区(Alex-content-updata)迁入本仓库,并从纯本地运行升级为云端主跑。

## 每日时间线(GST)

```
08:47  云端 routine(trig_014WNHD9bVxBBvkv6sm9Ggmk)
       ① curl github.com/trending?since=daily(恰好在沙箱放行的 github.com 域!)
       ② ai-keywords.md 打分筛 AI(≥3分双信号) + grep 硬校验选题历史(90天去重)
       ③ README: 先试 api.github.com,被阻则 git clone --depth 1 兜底
       ④ 按模板与禁用词清单写文章 → 待审核/日期/article.md(顶部3个标题候选)
       ⑤ 追加选题历史 → 推 main
08:5x  trending-push Action → 文章发 Hotspot 机器人
09:00  (本地兜底)Documents/Claude/Scheduled/github-ai-trending,先 pull 见云端已产出即跳过
```

## 目录结构(自包含,全在 `GitHub-Trending/` 下)

| 文件 | 说明 |
|---|---|
| `SKILL.md` | 完整工作流(选题/抓取/写作/报告/失败预案) |
| `配置.yaml` | 打分阈值/去重窗口(90天)/字数/行为开关 |
| `reference/ai-keywords.md` | AI 相关性打分词表(命中+2/反向词-2/双信号阈值) |
| `reference/style-tech-media.md` | 写作硬约束:**禁用词清单(炸裂/王炸/颠覆等绝对不能出现)** |
| `reference/article-template.md` | 文章结构模板(3项目各一节+今日观察) |
| `选题历史.md` | 一行一天 `日期: repo1, repo2, repo3`,防重复的唯一事实源 |
| `待审核/日期/` | article.md + raw-trending.json + repos-meta.json;33天历史完整迁入 |

## 关键机制

- **去重必须 grep 硬校验**,不能凭记忆——旧版靠 prompt 自觉曾 3 次违反 90 天规则,血泪教训
- GitHub API 无 token 限流 60 req/h:403+RateLimit-0 → 立即停,不重试
- 不足 3 个 AI 项目时按 today's stars 用非 AI 项目补足
- **绝不自动发布到内容平台**(Telegram 送审样稿除外);`已发布/` 归档由 jacob 手动

## 迁移备注

- 旧工作区 `Alex-content-updata/GitHub-AI-Trending/` 未删,由 jacob 确认稳定后自行处理
- 迁移备份文档在 Desktop(641KB),可留档
