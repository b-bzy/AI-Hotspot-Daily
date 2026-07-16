<!--
标题候选：
1. 今日 GitHub AI 项目：低成本模型的编码代理重新成主线
2. Open Interpreter 用 Rust 重写登顶今日关注，DeepTutor、OpenCut 同样值得看
3. 今日 GitHub AI 热点：3 个项目 24 小时新增超 2100 star
当前正在使用：候选 1
-->

# 今日 GitHub AI 项目：低成本模型的编码代理重新成主线

> 今天的榜单上，编码代理（coding agent）与 AI 原生应用继续占据主流，Open Interpreter 用 Rust 重写核心引擎，HKUDS 的 DeepTutor 把六种学习模式塞进同一个 agent loop。第三个项目 OpenCut 虽非 AI 原生，但 24 小时新增 1,664 star，是今天全榜增长最快的项目。

---

## 1. Open Interpreter — 面向低成本模型优化的编码代理

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 65.6k | 299 | Rust | Apache-2.0 |

Open Interpreter 解决的问题很具体：让开发者用 Kimi、Qwen、DeepSeek 这类价格更低的模型也能跑出接近旗舰模型的编码代理体验。项目 README 里写明这是"a fork of OpenAI's Codex"，专注于打磨能在低成本模型上发挥出最佳效果的 agent harness。

这次更新最大的变化是架构重写：原来的 Python 版本已经转为社区维护的 fork（endolith/open-interpreter），新仓库整体用 Rust 重新实现，代码占比达到 96.6%。它内置了 native、claude-code、qwen-code、deepseek-tui、swe-agent 等多种 harness，用户可以用 `/harness` 命令切换，针对不同模型选择不同的执行策略。最新版本号为 0.0.25，累计发布 56 个 release。

适合已经在用低价模型（如 Kimi、DeepSeek）做编码任务、但希望获得更好 agent 执行效果的开发者，命令行安装一行脚本即可跑起来。

🔗 项目地址：https://github.com/openinterpreter/openinterpreter

---

## 2. DeepTutor — 面向长期学习的 agent 原生学习工作台

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 26.4k | 172 | Python | Apache-2.0 |

DeepTutor 由香港大学 HKUDS 实验室发布，定位是"agent-native learning workspace"：把 Chat、Quiz、Research、Visualize、Solve、Mastery Path 六种学习模式接到同一个 agent 运行时上，而不是各自独立的工具。README 里的说法是"你切换的是目标（objective），不是引擎（engine）"，知识库、笔记、记忆在不同模式之间保持连续。

技术上它接入了多种检索后端，默认用 LlamaIndex 做本地向量+BM25 检索，也支持 GraphRAG、LightRAG 做知识图谱检索，还能直接连 Obsidian 知识库。模型层支持 OpenAI、Anthropic Claude、本地跑的 Ollama/llama.cpp/vLLM 等多种 provider，最新版本 v1.5.1，`pip install -U deeptutor` 即可安装启动。

适合需要长期、跨学科学习场景的学生和自学者，也适合想用 AI agent 做课程内容生成的教育者。

🔗 项目地址：https://github.com/HKUDS/DeepTutor

---

## 3. OpenCut — 开源版 CapCut 替代品

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 72.2k | 1,664 | TypeScript | MIT |

OpenCut 定位是"开源版 CapCut"，目标是提供一个免费、开放的网页 / 桌面 / 移动端视频剪辑工具。它是今天全榜单里 24 小时新增 star 最多的项目，达到 1,664 个，明显高于榜单上其它任何项目。

项目目前正在从零重写：README 提到会用统一的 Rust core 支撑桌面、移动、浏览器三端，取代原有的 opencut-classic 版本，同时计划开放 Editor API 和插件系统。值得关注的一点是，重写版计划加入面向 AI agent 的 MCP server 支持，但目前项目主体仍是一个传统视频剪辑工具，还没有围绕 AI 生成或剪辑做核心功能。当前 issue 数 243 个，处于活跃重构阶段。

适合需要免费、开源视频剪辑工具的内容创作者，以及想在开源项目基础上做二次开发或插件扩展的开发者。

🔗 项目地址：https://github.com/OpenCut-app/OpenCut

---

## 今日观察

今天入选的三个项目里，两个都属于"agent 原生"应用——Open Interpreter 把重写重心放在适配低成本模型上，DeepTutor 则把多种学习场景统一到一个 agent 运行时。第三个项目 OpenCut 虽然定位是传统视频剪辑工具，但增长速度反而是今天最快的，说明开源生产力工具本身仍有很大的关注度，不完全被 AI 话题主导。

---

**Tags**：#GitHub热点 #AI开源 #编码代理 #RAG #开源视频剪辑
