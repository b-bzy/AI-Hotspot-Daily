<!--
标题候选：
1. 今日GitHub AI热点：代码图谱与法律基准同台
2. ComfyUI领衔今日GitHub AI三项目，另两个同样值得关注
3. 今日GitHub AI热点：三项目24小时增星超500
当前正在使用：候选 1
-->

# 今日GitHub AI热点：代码图谱与法律基准同台

> 今天的 GitHub Trending 日榜里，AI 相关项目跨度较大：一个是运作多年、刚完成账号迁移的生成引擎，一个是把代码库结构化为图数据库的开发者工具，还有一个是刚起步的垂直行业基准。三者分别代表成熟生态、通用工具和细分场景三种不同阶段。

---

## 1. ComfyUI — 从个人账号迁移到组织账号的模块化生成引擎

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 125.7k | 365 | Python | GPL-3.0 |

ComfyUI 用节点图的方式组织生成模型工作流：开发者把图像、视频、3D、音频等模型分别做成节点，按需连接，不用写代码就能拼出一条完整的生成流水线，再通过桌面客户端、本地 API 或云端运行。

README 里的发布、下载徽章仍链接到个人账号 comfyanonymous/ComfyUI，但当前仓库已运作在组织账号 Comfy-Org 下，原生支持的模型列表也扩展到了 Stable Diffusion 1.5/SDXL/SD3.5、Flux.1/Flux.2、Qwen Image、Wan 2.1/2.2 等数十个图像与视频模型，并提供 API 节点调用 Nano Banana、Seedance 等闭源模型。125.7k star、14.9k fork 的规模，使它在扩散模型工具链里已是头部项目之一。

适合需要本地部署可视化生成流水线，或者要把多个生成模型串联进生产环境的开发者和内容团队。

🔗 项目地址：https://github.com/Comfy-Org/ComfyUI

---

## 2. code-graph-rag — 面向多语言单体仓库的代码知识图谱问答工具

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 3.1k | 96 | Python | MIT |

Code-Graph-RAG 用 Tree-sitter 解析多语言代码库，把函数、类、方法之间的调用与引用关系写入 Memgraph 图数据库。开发者可以用自然语言提问，系统据此生成 Cypher 查询定位代码，而不是靠关键词做全文检索。

和纯文本检索的 RAG 方案相比，它把代码结构本身建成图：支持按 AST 模式做结构化查找和批量重写，目前已完整支持 Python、TypeScript、JavaScript、Rust、Go、Java、C、C++、C#、PHP、Lua、Dart 共 12 种语言，Ruby 支持仍在开发中。项目还提供 MCP Server，可以作为工具接入 Claude Code 等编码助手，让 Agent 编辑代码前先拿到基于图结构的检索结果。

适合维护大型多语言单体仓库、需要跨模块理解代码调用关系的团队，尤其是想让编码 Agent 精确定位代码而非依赖关键词匹配的场景。

🔗 项目地址：https://github.com/vitali87/code-graph-rag

---

## 3. Harvey LAB — 评测 LLM Agent 处理真实法律任务能力的开源基准

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 871 | 47 | Python | MIT |

Harvey LAB（Legal Agent Benchmark）是法律科技公司 Harvey 开源的一套评测集，专门衡量 LLM Agent 在真实法律工作场景下的表现，覆盖 24 个以上法律执业领域，目前包含 1671 个任务。

项目由两部分组成：一套带指令、文档和评分标准的任务数据集，以及一套执行 Agent 并打分的评估框架。官方文档给出的示例是一次完整的并购数据room（M&A data-room）尽调任务，从任务拆解、Agent 运行、评分到生成对比报告全流程可跑通，评分依据"全部通过"的规则打分，同时支持 LLM 作裁判的评估方式。作为一个 871 star 的早期项目，它目前仍处于持续扩充任务集和评估框架的阶段。

适合关注法律科技、需要评测 Agent 在专业垂直领域可靠性的研究者和团队参考。

🔗 项目地址：https://github.com/harveyai/harvey-labs

---

## 今日观察

三个项目的共同点是"图结构"和"结构化评测"取代了纯文本处理：ComfyUI 用节点图组织生成流程，code-graph-rag 用知识图谱理解代码，Harvey LAB 用带评分标准的任务集衡量 Agent 表现，而不是靠人工主观判断。

---

**Tags**：#GitHub热点 #AI开源 #ComfyUI #RAG #LLMAgent
