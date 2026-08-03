<!--
标题候选：
1. 今日 GitHub AI 热点：从入门教程到本地推理引擎，三个项目各占一极
2. Generative AI for Beginners 登顶今日 Trending，OpenWork、DwarfStar 同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时新增超 1000 star
当前正在使用：候选 1
-->

# 今日 GitHub AI 热点：从入门教程到本地推理引擎，三个项目各占一极

> 今天的 GitHub Trending 日榜上，AI 相关项目集中在教程、协作工具和推理引擎三个方向。微软的生成式 AI 教程重新进入榜单前列，桌面端 Agent 工作流工具 OpenWork 和专注 DeepSeek 模型的本地推理引擎 DwarfStar 同样登榜，三者分别对应学习、协作、部署三个不同阶段。

---

## 1. Generative AI for Beginners — 面向初学者的生成式 AI 应用开发课程

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 114.9k | 588 | Jupyter Notebook | MIT |

这套教程由微软 Cloud Advocates 团队维护，用 21 节课覆盖 Prompt 工程、RAG、Agent、模型微调等主题，目标是让只有基础 Python 或 TypeScript 经验的开发者能够独立跑通一个可用的生成式 AI 应用，而不是先啃论文再啃框架文档。

和纯理论课程不同，每节课分为"Learn"（讲概念）和"Build"（配代码）两类，代码同时提供 Python 与 TypeScript 版本，可以接 Azure OpenAI、OpenAI API，也可以用 Foundry Local 完全离线运行，不强制绑定单一云厂商。仓库目前支持 50 多种语言的自动翻译。

适合刚接触生成式 AI 开发、想要一套结构化学习路径而非零散教程的开发者。

🔗 项目地址：https://github.com/microsoft/generative-ai-for-beginners

---

## 2. OpenWork — 跨 Agent 共享 AI 工作流的开源桌面应用

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 20.4k | 280 | TypeScript | MIT |

OpenWork 是一个开源桌面应用，定位是 Claude Cowork 和 Codex 的开源替代品。它要解决的问题很具体：团队里每个人给 Claude Code、Cursor 等 Agent 写的 Skill、MCP 配置往往只存在自己电脑上，换一台机器或者交接给同事就要重新配置一遍。

OpenWork 把这些能力封装成一个可安装的 MCP：接入后暴露 `search_capabilities` 和 `execute_capability` 两个工具，Agent 可以直接搜索并调用团队共享的技能。面向组织的 OpenWork Den 提供权限管理、模型供应商配置和技能市场，用来控制谁能用哪些能力。

适合已经在用 Claude Code、Cursor 或 Codex 的团队，想把零散的 Agent 配置沉淀成可复用、可分发的资产。

🔗 项目地址：https://github.com/different-ai/openwork

---

## 3. DwarfStar（仓库名 ds4）— 面向 DeepSeek V4 系列模型的本地推理引擎

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 20.1k | 139 | C | MIT |

DwarfStar 是 Redis 作者 antirez 开发的本地推理引擎，只做一件事：让 DeepSeek V4 Flash、DeepSeek V4 PRO 和 GLM 5.2 这几个模型在消费级硬件上跑起来，不追求做通用的 GGUF 加载器。

它复用了 llama.cpp 和 GGML 的量化格式与内核，但模型加载、KV 缓存、HTTP 服务和编码 Agent 是一起构建和测试的。作者在 8 张 L40S 显卡的服务器上测试，聚合生成速度达到 120 token/s、预填充 2000 token/s；两台 Mac Studio 用 RDMA 做张量并行，也能跑 4-bit 量化的 DeepSeek Flash。README 中说明，代码开发过程里大量使用了 GPT-5.5/5.6 和 Claude Fable 辅助。

适合有 96GB 以上统一内存 Mac、多卡 CUDA 服务器等大内存硬件，想在本地或私有服务器上稳定跑 DeepSeek V4 系列模型的用户。

🔗 项目地址：https://github.com/antirez/ds4

---

## 今日观察

三个项目分别对应学习、协作、部署三个不同环节：结构化教程仍然是 AI 相关仓库里增长最稳的一类，而 Agent 工作流共享工具和垂直化的本地推理引擎，则说明部分开发者的关注点已经从"用哪个模型"转向"怎么把已有模型和 Agent 稳定用起来"。

---

**Tags**：#GitHub热点 #AI开源 #生成式AI #本地推理 #DeepSeek
