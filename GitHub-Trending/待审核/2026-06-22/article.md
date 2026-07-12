<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub AI 项目：从 Agent 框架到记忆层
2. 字节 DeerFlow 2.0 登上今日 Trending，另两个 AI 项目同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时合计新增超 1.3k star
当前使用：候选 1
-->

# 今日 GitHub AI 项目：从 Agent 框架到记忆层

> 今天 Trending 上的 AI 项目，集中在"怎么搭一个能干活的 agent"这条线上。我们挑了三个方向不重叠的：一个 agent 执行框架、一个 agent 记忆层，以及一个把大模型用在自选股分析上的垂直应用。

---

## 1. DeerFlow — 字节开源的 super agent harness

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 72.7k | 442 | Python | MIT |

DeerFlow（Deep Exploration and Efficient Research Flow）想凑齐一个"能自己干活的 agent"需要的零件：子 agent 调度、长期记忆、沙箱执行、可扩展的 skill 体系。它面向的是一次要跑几分钟到几小时的长任务——做调研、写代码、产出内容，而不是一问一答。

当前的 2.0 是从零重写的版本，和 1.x 不共用代码。1.x 原本是一个 Deep Research（深度调研）框架，2.0 把范围扩到通用 agent harness，补上了沙箱与文件系统、上下文工程、长期记忆几个模块，并支持接入 Claude Code 的 skill。README 里提到，2.0 发布后项目曾排到 GitHub Trending 第一。

适合想自建 agent 系统、又不愿意从调度和沙箱开始造轮子的团队参考。官方推荐配合 Doubao、DeepSeek、Kimi 等模型运行。

🔗 项目地址：https://github.com/bytedance/deer-flow

---

## 2. cognee — 给 AI agent 用的开源记忆层

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 18.7k | 347 | Python | Apache-2.0 |

cognee 处理的是 agent "记不住事"的问题。它把喂进去的各种格式数据，持续构建成一个自托管的知识图谱，让 agent 在多次会话之间保留长期记忆，而不是每次都从零开始。

技术上，它把向量检索、图谱推理和本体（ontology）生成结合在一起，既能按语义搜索，也能顺着实体之间的关系查。对外的接口被收敛成 remember、recall、forget、improve 四个操作，用 pip 或 uv 即可安装，并提供了 Claude Code 插件。项目 2023 年 8 月开源，目前 18.7k star。

适合需要给 agent 加"长期记忆 + 知识库"的开发者，尤其是想把公司内部多源数据统一成一张图来查询的场景。

🔗 项目地址：https://github.com/topoteretes/cognee

---

## 3. daily_stock_analysis — LLM 驱动的自选股日报工具

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 44.7k | 568 | Python | MIT |

这个项目把"每天盯盘"自动化：配置好自选股后，它每天自动拉行情和新闻，用大模型做分析，再把一份"决策仪表盘"推送到企业微信、飞书、Telegram、Discord、Slack 或邮箱，覆盖 A 股、港股、美股、日股、韩股。

它的特点是"零成本定时运行"——可以直接 Fork 仓库用 GitHub Actions 跑，不需要自己的服务器，也支持 Docker 和本地定时任务。模型侧兼容 Gemini、DeepSeek、通义千问、Claude、Ollama 等，行情数据接了 AkShare、Tushare、YFinance 等多个源，还内置了均线、缠论、波浪等 15 种分析策略，以及支持多轮追问的 Agent 问股。

项目 2026 年 1 月开源，几个月内涨到 44.7k star。需要说明的是，它产出的是模型分析结果，不构成投资建议，更适合当作信息整理与自动推送工具来看。

🔗 项目地址：https://github.com/ZhuLinsen/daily_stock_analysis

---

## 今日观察

今天上榜的三个 AI 项目，正好落在 agent 生态的不同层：DeerFlow 提供执行框架，cognee 补上长期记忆，daily_stock_analysis 则是一个直接面向用户的垂直应用。从"造工具"到"用工具解决某个具体行当的问题"，这条链路上的各个环节都有人在做。

---

**Tags**：#GitHub热点 #AI开源 #AIAgent #知识图谱 #量化分析
