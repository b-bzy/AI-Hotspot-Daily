<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub AI 热点：agent 的技能、数据与推理层各有一个项目
2. 网络安全技能库登顶今日 AI 榜，firecrawl 与 airllm 同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时合计新增超 1,700 star
当前使用：候选 1
-->

# 今日 GitHub AI 热点：agent 的技能、数据与推理层

> 今天 Trending 日榜上的 AI 项目，集中在 agent 工具链的不同环节。我们挑了三个近 90 天本栏目没写过的：一个给 agent 补网络安全技能，一个给 agent 供干净的网页数据，一个让大模型在小显存上跑推理。

---

## 1. Anthropic-Cybersecurity-Skills — 给 AI agent 装上网络安全技能库

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 18.8k | 956 | Python | Apache-2.0 |

这个项目想解决的问题很具体：让 AI agent 具备一名安全分析师的实操能力。它把 817 个网络安全技能结构化整理出来，覆盖 29 个安全领域，从内存取证、威胁狩猎到云上入侵排查都有对应的技能描述。开发者把仓库指给自己的 agent，agent 就能照着这些技能去执行调查，而不是只会给出泛泛的回答。

和零散的提示词集合相比，它的差异在于把每个技能都映射到六套行业框架——MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF 和 MITRE 反欺诈框架 F3，并遵循 agentskills.io 这套开放标准。技能格式与 Claude Code、GitHub Copilot、Cursor、Gemini CLI 等 26 个以上平台兼容。需要说明的是，README 里明确写了这是社区独立项目，与 Anthropic 公司没有隶属关系，名字里的 Anthropic 指的是其 skill 格式渊源。

适合做安全自动化、想给现有 AI 编程助手补上安全领域知识的团队参考。项目创建于 2026 年 2 月，目前 18.8k star，过去 24 小时新增 956。

🔗 项目地址：https://github.com/mukul975/Anthropic-Cybersecurity-Skills

---

## 2. firecrawl — 把网页转成 agent 能直接用的干净数据

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 137k | 615 | TypeScript | AGPL-3.0 |

firecrawl 解决的是 AI 应用的"数据入口"问题：把任意网页抓下来，转成干净的 Markdown 或结构化 JSON，供大模型和 agent 直接使用。它提供搜索、抓取、交互三类接口，也能解析网页里的 PDF、DOCX 等文件。

按官方 README 的说法，它覆盖了约 96% 的网页（包含重 JS 渲染的页面），P95 延迟为 3.4 秒，省去了轮换代理、绕过反爬、处理限流这些工程麻烦。输出直接面向 LLM，目标是减少 token 消耗。它也支持通过单条命令接入 MCP 客户端，把抓取能力挂到 agent 上。项目以 AGPL-3.0 开源，同时提供托管服务。

适合做 RAG、需要实时网页数据的 agent，以及不想自建爬虫基础设施的团队。作为创建于 2024 年的头部开源项目，目前 137k star，过去 24 小时新增 615。

🔗 项目地址：https://github.com/firecrawl/firecrawl

---

## 3. airllm — 在 4GB 显存上跑 70B 大模型推理

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 21.1k | 193 | Jupyter Notebook | Apache-2.0 |

airllm 针对的是显存不够的场景：在不做量化、蒸馏、剪枝的前提下，让 70B 参数的大模型在单张 4GB 显存的显卡上完成推理；按 README 描述，现在 405B 的 Llama3.1 也能在 8GB 显存上运行。

它的做法是优化推理时的显存占用，按层加载模型，把对显存的峰值需求压下来——代价是推理速度比一次性全量加载慢，更适合算力受限、对延迟不敏感的场景。项目支持 Llama3、Mixtral、ChatGLM、Qwen、Baichuan、Mistral、InternLM 等模型，也支持 MacOS 和 CPU 推理，并提供 4bit/8bit 量化选项。

适合显卡预算有限、想在本地试跑大模型的个人开发者和研究者。项目自 2023 年开源维护至今，目前 21.1k star，过去 24 小时新增 193。

🔗 项目地址：https://github.com/lyogavin/airllm

---

## 今日观察

今天这三个项目分别落在 AI agent 技术栈的不同层：技能层（给 agent 网络安全能力）、数据层（给 agent 喂干净的网页数据）、模型层（让大模型在小显存上跑起来）。共同点是都在降低"让 AI 真正干活"的门槛，而不是停在模型本身。

---

**Tags**：#GitHub热点 #AI开源 #AIAgent #网页数据 #大模型推理
