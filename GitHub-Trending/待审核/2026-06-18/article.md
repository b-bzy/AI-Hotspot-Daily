<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub AI 热点：时序预测大模型、代码索引 MCP、多模态 GUI Agent
2. Google 的时序预测模型 TimesFM 登上今日 Trending，另两个项目同样值得关注
3. 今日 GitHub AI 三连：一个 24 小时新增超 600 star，一个把 Linux 内核索引压到 3 分钟
当前使用：候选 1
-->

# 今日 GitHub AI 热点：时序预测大模型、代码索引 MCP 与多模态 GUI Agent

> 今天 Trending 榜上的 AI 项目集中在三个不同方向：时间序列预测、给编码 Agent 用的代码索引引擎、以及多模态 GUI 操作 Agent。三个项目分属预训练模型、开发者工具和 Agent 框架，互不重叠，适合一起看一下当前的几条主线。

---

## 1. TimesFM — Google Research 的时间序列预测基础模型

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 22k | 606 | Python | Apache-2.0 |

TimesFM 要解决的问题是时间序列预测：给一段历史数据（销量、流量、负载等），预测未来一段时间的走势。它的思路是把 NLP 里"预训练一个基础模型、下游直接用"的做法搬到时序场景，用一个 decoder-only 架构做零样本预测，背后是 ICML 2024 的论文《A decoder-only foundation model for time-series forecasting》。

和针对单一数据集训练的传统预测模型相比，TimesFM 的差异在于"一次预训练、多处复用"。最新的 2.5 版本把参数量从 500M 降到 200M，上下文长度从 2048 提到 16k，并通过一个可选的 30M quantile head 支持到 1k horizon 的连续分位数预测。仓库还提供了基于 HuggingFace Transformers + PEFT（LoRA）的微调示例。

它已经接入了 BigQuery ML、Google Sheets 和 Vertex Model Garden。适合需要做批量时序预测、又不想为每个数据集单独训模型的团队参考。

🔗 项目地址：https://github.com/google-research/timesfm

---

## 2. codebase-memory-mcp — 给 AI 编码 Agent 用的代码索引 MCP 服务

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 5.7k | 371 | C | MIT |

这是一个面向 AI 编码 Agent 的代码索引引擎，通过 MCP（Model Context Protocol）对外提供服务。它要解决的问题是：让 Cursor、Claude Code 这类编码助手在回答"这个函数在哪被调用"之类的结构性问题时，不必把整个代码库塞进上下文。

技术上，它用 tree-sitter 做 AST 解析覆盖 158 种语言，并为 Python、TypeScript、Go、C/C++、Java、Rust 等 11 种语言加了 Hybrid LSP 语义类型解析，最终生成一张包含函数、类、调用链、HTTP 路由的持久化知识图谱，对外暴露 14 个 MCP 工具。按 README 的说法，索引普通仓库在毫秒级，Linux 内核（28M 行、7.5 万文件）约 3 分钟，结构查询在 1ms 以内。项目用纯 C 写成，零依赖，打包为单一静态二进制，支持 macOS、Linux、Windows。

创建于 2026 年 2 月，目前已有一定关注度。适合在编码 Agent 工作流里需要快速代码导航、想减少 token 消耗的开发者。

🔗 项目地址：https://github.com/DeusData/codebase-memory-mcp

---

## 3. UI-TARS-desktop — 字节跳动开源的多模态 GUI Agent 栈

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 36.7k | 150 | TypeScript | Apache-2.0 |

UI-TARS-desktop 是字节跳动开源的多模态 AI Agent 项目，目前包含两部分：Agent TARS 和 UI-TARS Desktop。它的目标是让 Agent 能"看见"并直接操作图形界面，而不是只调用 API。

Agent TARS 是一个通用的多模态 Agent 栈，把 GUI Agent 和视觉能力带到终端、浏览器和桌面，主要以 CLI 和 Web UI 形式提供，并通过 MCP 接入外部工具。UI-TARS Desktop 则是一个桌面应用，基于 UI-TARS 模型提供原生 GUI Agent，支持本地和远程的计算机操作与浏览器操作。两者的共同点是依赖多模态 LLM 做视觉理解，再把理解结果转成对界面的点击、输入等动作。

创建于 2025 年 1 月，已有规模。适合想研究 computer-use / GUI 自动化方向，或需要让 Agent 直接操作真实软件界面的开发者。

🔗 项目地址：https://github.com/bytedance/UI-TARS-desktop

---

## 今日观察

三个项目的方向各不相同，但都指向同一件事：AI 正在从"对话"往"接入真实系统"走——TimesFM 接进了 BigQuery 和表格，codebase-memory-mcp 接进了编码 Agent 的工作流，UI-TARS 直接去操作桌面和浏览器。模型本身之外，怎么把它接到具体场景里，正成为开源社区更关注的部分。

---

**Tags**：#GitHub热点 #AI开源 #时间序列预测 #MCP #GUIAgent
