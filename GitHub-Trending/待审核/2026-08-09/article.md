<!--
标题候选：
1. 今日 GitHub AI 热点：Agent Skills 成关注焦点
2. google/skills 登顶今日 Trending，另两个项目同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时合计新增超 700 star
当前使用：候选 1
-->

# 今日 GitHub AI 热点：Agent Skills 成关注焦点

> 今日 GitHub Trending 日榜中，Google 官方维护的 Agent Skills 仓库以 24 小时新增 481 star 排在日榜第 4 位。多智能体交易框架 TradingAgents 与老牌 Java 基础库 Guava 同时上榜,三者分别代表 Agent 工具链、垂直领域应用与基础设施库三个不同方向。

---

## 1. google/skills — 为 Google 云与 AI 产品打包的 Agent Skills 集合

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 16.8k | 481 | Python | Apache-2.0 |

google/skills 是 Google 官方维护的 Agent Skills 仓库，把 Google Cloud、Gemini、BigQuery、GKE 等上百项产品的操作文档整理成可被 Claude Code、Codex、Antigravity CLI 等智能体工具直接调用的技能包。开发者执行一次 `npx skills add google/skills`，就能按需挑选安装，不用再分头翻阅各产品线的官方手册。

与此前分散在 Flutter、Firebase、Genkit 等各自仓库的 Skills 不同，这个仓库把 Cloud 基础设施、AI/ML Agent Platform、广告 API 等多条产品线统一到一个索引下，并为 Claude Code、Codex 两类主流编码 Agent 提供了插件市场安装入口，属于把内部工具沉淀对外开放的一次整理，而不是全新技术。

适合已经在用 Claude Code、Codex 等编码 Agent、且经常要接 Google Cloud、GKE 或 BigQuery 的开发者参考。

🔗 项目地址：https://github.com/google/skills

---

## 2. TauricResearch/TradingAgents — 多智能体协作的金融交易研究框架

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 96.6k | 153 | Python | Apache-2.0 |

TradingAgents 把一次交易决策拆给多个 LLM 驱动的角色分工完成：基本面分析师、情绪分析师、技术分析师先各自输出判断，再由看多、看空研究员展开结构化辩论，最后交给交易员和风控团队给出可执行建议，而不是让单一模型直接输出买卖信号。

框架基于 LangGraph 构建，最新的 0.3.1 版本修复了 Alpha Vantage 数据源的"未来数据"泄露问题（回测时误用了尚未发生的财报数据），并支持在 OpenAI、Anthropic、Google、DeepSeek、Qwen 等多家模型供应商之间切换。把"防止用到未来行情"这类细节写进更新日志，在同类项目里并不常见。

README 中明确写明该框架用于研究目的，不构成投资建议。适合做量化研究、多智能体协作范式实验的团队参考，不建议直接接入实盘交易。

🔗 项目地址：https://github.com/TauricResearch/TradingAgents

---

## 3. google/guava — Google 内部长期使用的 Java 核心工具库

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 51.9k | 93 | Java | Apache-2.0 |

Guava 补上了 JDK 标准库缺失的一批基础能力：不可变集合、Multimap/Multiset、图结构、并发工具、哈希与字符串处理。它是 Google 内部大多数 Java 项目的公共依赖，同时也被大量外部公司直接使用。

项目同时维护 JRE 和 Android 两套构建产物，当前版本为 33.6.0-jre / 33.6.0-android。最近一次改动集中在 CompactHashMap 等容器内部实现的持续优化，而不是新增大面积 API，体现的是一个成熟基础库常见的迭代节奏。

适合已经在用 Java 或 Kotlin 做后端、Android 开发，想减少重复造轮子的团队参考；新项目做技术选型时也可以直接对比它和 JDK 自带集合类的取舍。

🔗 项目地址：https://github.com/google/guava

---

## 今日观察

今天日榜里的 AI 相关项目集中在"工具链整合"（Agent Skills）和"垂直应用"（金融交易 Agent）两端，没有新模型或新训练框架发布。Guava 这样有十余年历史的基础库仍能凭稳定维护挤进日榜前十，说明当天的热度并非全部来自 AI 议题。

---

**Tags**：#GitHub热点 #AI开源 #AgentSkills #多智能体 #Java
