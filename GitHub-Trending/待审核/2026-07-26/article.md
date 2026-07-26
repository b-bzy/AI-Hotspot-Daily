<!--
标题候选：
1. 今日 GitHub AI 热点：Claude 生态从教程走向工具链
2. ECC 登顶今日 AI 类 GitHub 项目，另两个 Claude 生态项目同样值得关注
3. 今日 GitHub AI 热点：三个项目 24 小时合计新增超 900 star
当前正在使用：候选 1
-->

# 今日 GitHub AI 热点：Claude 生态从教程走向工具链

> 今天的 GitHub 日榜上，AI 类项目集中出现在 Claude 生态周边：一份运营两年的官方教程库、一款成立四个月的 AI 视频编辑器、一套半年内新增 23 万 star 的多 Agent 配置工具。三者分别对应教程、消费应用、开发者基础设施三种形态。

---

## 1. anthropics/claude-cookbooks — Anthropic 官方维护的 Claude API 代码示例库

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 49.9k | 132 | Jupyter Notebook | MIT |

claude-cookbooks 解决的是一个具体问题：开发者接入 Claude API 时，常常缺少可以直接复制、跑得通的实现范例。这个仓库把常见场景整理成 notebook，覆盖分类、检索增强生成（RAG）、摘要、工具调用等基础能力。

内容覆盖面比一般社区教程更完整：客服类 agent、SQL 查询、Pinecone 与 Wikipedia 等第三方集成、图像分析与图表解读等多模态场景、子 agent 编排、PDF 解析、自动化评测、JSON 模式、内容审核、prompt caching 等进阶用法都各有独立 notebook，且由 Anthropic 官方维护并随 API 版本更新。

仓库创建于 2023 年，两年多时间积累到 49.9k star，属于已有规模、被多个团队参考的项目。适合刚接触 Claude API、需要具体范例而非纯文档的开发者。

🔗 项目地址：https://github.com/anthropics/claude-cookbooks

---

## 2. palmier-io/palmier-pro — 面向人机协同剪辑的 macOS 视频编辑器

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 12.3k | 412 | Swift | GPL-3.0 |

palmier-pro 想解决的是视频剪辑里人和 AI 生成内容的时间线割裂问题：它是一款 Swift 原生编辑器，让用户和 AI agent 在同一条时间线上协作生成、编辑视频素材。

工程上的取舍比较明确：编辑器内核完全开源（GPL-3.0），接入 Seedance、Kling 等模型的生成式 AI 处理部分保持闭源、走订阅收费。它还通过 Model Context Protocol 在本地暴露一个 MCP server（`http://127.0.0.1:19789/mcp`），让 Claude Code、Cursor 等工具能直接操作剪辑项目。目前仅支持 macOS 26（Tahoe）机型的 Apple Silicon 设备，团队来自 YC S24 批次。

项目 2026 年 4 月创建，四个月内做到 12.3k star，已有一定规模。适合日常使用 macOS 剪辑、希望把 AI 生成素材直接嵌入编辑流程的用户，也适合想了解 MCP 如何接入桌面应用的开发者。

🔗 项目地址：https://github.com/palmier-io/palmier-pro

---

## 3. affaan-m/ECC — 统一多个 AI 编程工具配置的 harness 优化系统

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 233.4k | 377 | JavaScript | MIT |

ECC 面对的问题是：团队里同时用 Claude Code、Cursor、OpenCode、Codex、Gemini、Zed 这几个 AI coding 工具时，各自的 agent 配置、技能库、安全规则互不相通，经验很难复用。ECC 把这些配置统一成一层可跨工具使用的框架。

具体构成上，它打包了 67 个可委派的专职 agent（覆盖规划、架构、代码评审、安全审计等角色）、279 个按领域分类的可复用 skill、基于 hook 的执行前后自动化机制，以及一个内置 1,282 条测试用例、102 条静态规则的 AgentShield 安全审计模块，另有带置信度评分的持续学习机制用于跨会话保留经验，支持 12 种以上编程语言。

仓库创建于 2026 年 1 月，半年时间涨到 23.3 万 star，是三个项目里体量最大的一个，已属头部开源项目。适合同时维护多个 AI coding 工具、想把 agent 与 skill 库标准化管理的团队参考。

🔗 项目地址：https://github.com/affaan-m/ECC

---

## 今日观察

三个入选项目都围绕 Claude 生态展开，但形态完全不同：一份官方教程、一款消费级应用、一套开发者基础设施。这说明 Claude 相关的开源产出已经从"怎么调 API"延伸到具体产品和工具链层面，覆盖了从入门学习到团队工程实践的不同阶段。

---

**Tags**：#GitHub热点 #AI开源 #ClaudeAPI #MCP #AI视频编辑
