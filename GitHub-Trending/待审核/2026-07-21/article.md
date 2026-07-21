<!--
标题候选：
1. 今日 GitHub Trending：终端智能体与语音工具同时登榜
2. AstrBot 登顶今日 AI Trending，另两个项目聚焦终端与语音场景
3. 今日 GitHub AI 热点：3 个项目 24 小时新增超 1000 star
当前正在使用：候选 1
-->

# 今日 GitHub Trending：终端智能体与语音工具同时登榜

> 今天的 GitHub 日榜里，AI 相关项目集中在两个方向：一是把智能体接入终端和即时通讯平台，二是语音识别工具对 Whisper 类模型的替代尝试。三个项目分别落在开发终端、IM 聊天平台、语音处理三个不同场景。

---

## 1. Kimi CLI — 跑在终端里的 AI 编程智能体

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 10.3k | 410 | Python | Apache-2.0 |

Kimi CLI 由月之暗面（Moonshot AI）开源，定位是一个运行在终端里的 AI 智能体，用来处理软件开发和终端操作任务。它可以读写代码、执行 shell 命令、检索网页内容，并在执行过程中自主规划后续动作，而不需要每一步都由用户下指令。

和其他终端 AI 工具相比，Kimi CLI 把编辑器生态接进来了：既支持通过 VS Code 插件使用，也通过 Agent Client Protocol 兼容 Zed、JetBrains 等 IDE，还内置了 Model Context Protocol（MCP）支持，可以通过 `kimi mcp` 命令接入外部工具。项目目前正在向下一代的 Kimi Code CLI 演进。

适合已经在用终端做开发、想把 AI 辅助和现有编辑器工作流打通的开发者。

🔗 项目地址：https://github.com/MoonshotAI/kimi-cli

---

## 2. AstrBot — 面向即时通讯平台的智能体聊天机器人框架

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 37.2k | 317 | Python | AGPL-3.0 |

AstrBot 解决的问题是把大模型对话能力接进 QQ、微信、飞书、钉钉、Telegram、Discord、Slack 这些即时通讯平台，开发者不用为每个平台单独写一套接入代码。项目已有 37.2k star，社区提供了超过 1000 个插件，覆盖智能客服、个人助理、企业知识库等场景。

技术上，AstrBot 把模型接入、平台适配、插件系统拆成独立模块：既能接 OpenAI、Gemini、Llama 等主流模型，也支持 Dify、Coze、阿里云百炼这类应用平台；同时提供了"Agent 沙箱"，让代码和 shell 调用在隔离环境里执行，避免智能体直接操作宿主机。部署方式覆盖一键云部署、Docker、桌面客户端和源码安装（`uv`）。

适合需要在国内外多个 IM 平台上快速搭建对话机器人、又不想为每个平台重复开发的团队。

🔗 项目地址：https://github.com/AstrBotDevs/AstrBot

---

## 3. Moonshine — 面向语音智能体的实时语音识别与合成工具包

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 9.9k | 282 | Python | MIT |

Moonshine 是一套开源语音工具包，提供语音识别（STT）、语音合成（TTS）、意图识别等能力，目标是让开发者搭建低延迟的语音智能体和语音交互应用。所有处理都在设备本地完成，不需要账号、信用卡或 API key，适合对隐私和离线可用性有要求的场景。

项目 README 中给出的对比是：相比 OpenAI 的 Whisper Large V3，Moonshine 在参数量少 6 倍的情况下识别准确率更高，同时针对流式场景做了专门优化——Whisper 固定 30 秒输入窗口、不支持流式缓存的问题，是 Moonshine 重点解决的部分。项目支持 Python、iOS、Android、macOS、Linux、Windows 和树莓派等多个平台。

适合做实时语音交互、车载或嵌入式设备上的离线语音识别、以及对响应延迟敏感的语音应用开发者。

🔗 项目地址：https://github.com/moonshine-ai/moonshine

---

## 今日观察

三个项目分别代表了 AI 智能体落地的三个不同切口：终端开发场景、即时通讯平台、语音交互设备。它们的共同点是都在做"把大模型能力接入某个已有场景"这件事，而不是自己重新造一个新场景。

---

**Tags**：#GitHub热点 #AI开源 #AI智能体 #语音识别 #MCP
