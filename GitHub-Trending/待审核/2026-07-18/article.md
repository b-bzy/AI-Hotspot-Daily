<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub AI 项目：效率成为共同主线
2. copilot-sdk 登顶今日 AI 相关 Trending，另两个项目同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时新增合计超 580 star
当前使用：候选 1
-->

# 今日 GitHub AI 项目：效率成为共同主线

> 今天的 GitHub Trending 日榜里，AI 相关项目没有集中在某个新模型或新框架上，而是分散在三个不同层次：Agent 运行时、代码上下文管理、向量检索。三者的共同点是都在解决"用更少的资源做同一件事"，而不是堆功能。

---

## 1. GitHub Copilot SDK — 把 Copilot CLI 的 Agent 运行时暴露成可编程接口

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 9.8k | 233 | Java | MIT |

GitHub Copilot SDK 解决的问题很具体：此前开发者想在自己的应用里嵌入类似 Copilot CLI 的 Agent 能力，只能自己搭一套任务规划、工具调用、文件编辑的编排逻辑。这个 SDK 把 Copilot CLI 背后的同一套 Agent 运行时直接暴露出来，开发者只需要定义 Agent 的行为，规划、工具调用、文件编辑这些环节交给 Copilot 处理。

技术上，SDK 与 Copilot CLI 之间走的是 JSON-RPC：应用调用 SDK 客户端，SDK 负责管理 CLI 进程的生命周期，也支持连接到一个外部运行的 CLI 服务端。目前同时提供 Node.js/TypeScript、Python、Go、.NET、Rust、Java 六种语言的实现，对应发布到 npm、PyPI、NuGet、crates.io、Maven Central 等各自生态的包管理器。

适合已经在用 Copilot 生态、又想把 Agent 能力接进自己产品或内部工具的团队，不用重新造一套编排框架。

🔗 项目地址：https://github.com/github/copilot-sdk

---

## 2. code-review-graph — 给 AI 编程工具建一张代码结构图，减少重复读代码

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 19.8k | 74 | Python | MIT |

AI 编程工具在做代码评审这类任务时，经常要重新读一遍代码库里的大段内容。code-review-graph 想解决的正是这个问题：它用 Tree-sitter 给代码库建一张结构图，增量追踪变更，再通过 MCP 把精确的上下文喂给 AI 助手，让助手只读真正相关的部分。

项目公开的评测数据给出了具体范围：在 6 个真实开源仓库（含 13 次提交）上，单次提问的 token 消耗相比"整仓库喂给模型"这种朴素做法，中位数减少约 82 倍，区间在 38 倍到 528 倍之间——最高的 528 倍出现在 fastapi 这个体量最大的仓库上，官方也特别说明这是最好情况而非典型值。影响范围分析（blast-radius）在 13 次评测提交上的平均 F1 为 0.71。`install` 命令目前能自动识别并配置 Codex、Claude Code、Cursor、Windsurf、Zed、GitHub Copilot 等十余种平台。

适合日常需要让 AI 工具处理大代码库、又在意 token 成本的开发者，一条命令即可接入现有编辑器或 CLI 工具链。

🔗 项目地址：https://github.com/tirth8205/code-review-graph

---

## 3. turbovec — 面向本地 RAG 场景的向量索引

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 13.4k | 280 | Python | MIT |

turbovec 是一个基于 Google Research TurboQuant 算法实现的向量索引，核心用 Rust 编写，同时提供 Python 绑定。项目给出的具体数字是：一个 1000 万文档规模的语料库，用 float32 存储需要 31GB 内存，turbovec 能压缩到 4GB 以内。TurboQuant 是一种数据无关的量化方法，添加向量后即可直接检索，不需要额外的训练步骤。

在搜索速度上，项目给出的对比数据是：手写的 ARM NEON 内核比 FAISS 的 IndexPQFastScan 快 10%–19%；x86 平台上，4-bit 配置领先，2-bit 配置略慢几个百分点。它还支持在检索阶段直接传入 ID 白名单做过滤检索，避免过度取数。目前提供 LangChain、LlamaIndex、Haystack、Agno 四个框架的集成，可以作为这些框架内置向量库的替换项，接口保持不变。

适合对隐私、内存或延迟有要求、希望把 RAG 检索完全跑在本地或私有环境里的团队。

🔗 项目地址：https://github.com/RyanCodrai/turbovec

---

## 今日观察

三个项目分别对应 Agent 运行时、代码上下文管理、向量检索三个不同层次，但都在做同一件事——用更少的计算和存储资源完成同样的工作，而不是简单堆功能或追新模型。这种"效率优先"的取向，在今天的榜单里比任何单一新模型发布都更明显。

---

**Tags**：#GitHub热点 #AI开源 #AgentSDK #MCP #向量检索
