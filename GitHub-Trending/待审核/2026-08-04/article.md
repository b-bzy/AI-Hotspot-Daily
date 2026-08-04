<!--
标题候选：
1. 今日 GitHub AI 项目：编码 Agent 之外，PDF 解析和语音框架同样值得看
2. DeepSeek-Reasonix 登顶今日 Trending，另两个项目同样值得关注
3. 今日 GitHub 热点：3 个项目 24 小时新增超 2700 star
当前正在使用：候选 1
-->

# 今日 GitHub AI 项目：编码 Agent 之外，PDF 解析和语音框架同样值得看

> 今天的 GitHub Trending 日榜上，真正符合"AI 相关"打分标准且近 90 天没写过的项目只有两个，都在给 Agent 补工具链；第三个补位项目跳出 AI，是 Firecrawl 开源的一个 PDF 解析库。三者合计 24 小时新增 star 超过 2,700。

---

## 1. DeepSeek-Reasonix — 面向终端的 DeepSeek 原生编码 Agent

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 30.1k | 883 | Go | MIT |

DeepSeek-Reasonix 要解决的问题很具体：给终端用户一个绑定 DeepSeek 系模型、且针对长会话 token 成本做过优化的编码 Agent，而不是又一层通用 CLI 套壳。项目由个人开发者 esengine 维护，目前托管在 GitHub 和国内的 AtomGit 两处。

技术上的差异点在于配置方式和成本控制。Provider、Agent 行为、工具和插件全部写在 `reasonix.toml` 里，不写死具体模型——DeepSeek 是内置预设，任何 OpenAI 兼容端点都能作为配置项接入，也可以让两个模型分别当"执行者"和"规划者"同时跑。外部工具通过 stdio JSON-RPC 以子进程方式接入，兼容 MCP 协议。围绕 DeepSeek 的前缀缓存机制做上下文维护，会话变长时自动裁剪过期的工具输出，减少重复计费的 token。整个程序用 Go 编译成禁用 CGO 的单一静态二进制，一条命令可交叉编译出六个平台版本。

适合已经在用 DeepSeek 系模型、需要一个轻量终端编码助手、对长会话 token 消耗敏感的开发者。CLI/TUI、桌面客户端和 VS Code 插件三种形态共用同一个本地引擎，装一次到处用。

🔗 项目地址：https://github.com/esengine/DeepSeek-Reasonix

---

## 2. pdf-inspector — 不依赖 OCR 的 PDF 解析库

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 8.6k | 1,699 | Rust | MIT |

pdf-inspector 由 Firecrawl 团队开源，解决的问题很实际：大约 54% 的 PDF 本身是文本型的，不需要走扫描件才用得上的 OCR 流程，但很多现有工具不分青红皂白地统一用 OCR 处理，既慢又费钱。这个库先判断一份 PDF 是文本型、扫描件、图片型还是混合型，再决定要不要交给 OCR。

技术上的差异点在于速度和结构还原能力。分类阶段只采样内容流，10–50 毫秒内给出判断结果和置信度；提取阶段保留字体信息和 X/Y 坐标，自动处理多栏排版的阅读顺序；转 Markdown 时靠字号比例识别标题层级，靠矩形检测和文本对齐两种方式识别表格，能处理带续页的财务表格和脚注。作者在 opendataloader-bench 的 200 份 PDF 语料上做过评测：整体得分 0.875，处理完 200 份文档用时 0.470 秒，在参与对比的几个本地引擎里分数和速度都排第一。整个库纯 Rust 实现，不带任何机器学习模型，只依赖 `lopdf` 一个包。

适合处理研报、财报、发票、合同这类原生文本 PDF 的场景，提供 Python、Node.js、浏览器 WebAssembly 和 Rust 四种接入方式。

🔗 项目地址：https://github.com/firecrawl/pdf-inspector

---

## 3. livekit/agents — 构建实时语音 AI Agent 的框架

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 12.1k | 148 | Python | Apache-2.0 |

livekit/agents 要解决的是工程拼接问题：把语音识别（STT）、大模型推理、语音合成（TTS）和实时通信这几层组件拼起来，让开发者专注在 Agent 的对话逻辑上，而不必自己从头搭一套 WebRTC 加 STT/TTS 的管线。LiveKit 本身是被广泛使用的开源 WebRTC 媒体服务器，这个框架是其 Agent 层的延伸。

技术上的差异点在于组合的自由度和场景覆盖。STT、LLM、TTS 和 Realtime API 可以自由搭配，不绑定单一供应商；内置任务调度和 dispatch API，把终端用户请求和具体 Agent 实例连接起来；依托 LiveKit 自己的电话网关，Agent 可以直接拨打或接听电话；用一个 transformer 模型做语义级的说话轮次检测，减少对话中的误打断；原生支持 MCP，一行代码就能接入 MCP 服务提供的工具；自带带 judge 机制的测试框架，方便验证 Agent 表现是否符合预期。

适合做客服机器人、语音助手一类实时语音交互产品的团队。`pip install "livekit-agents[openai,deepgram,cartesia]"` 一行命令带上常用插件即可起步。

🔗 项目地址：https://github.com/livekit/agents

---

## 今日观察

今天的榜单不算热闹，三个项目方向各异：一个是终端编码 Agent，一个是不用 OCR 的 PDF 解析库，一个是语音 Agent 框架。共同点是都不追求"大而全"，而是把编码效率、文档解析、实时语音这类具体环节做深，直接拿来当组件用。

---

**Tags**：#GitHub热点 #AI开源 #AIAgent #DeepSeek #PDF解析
