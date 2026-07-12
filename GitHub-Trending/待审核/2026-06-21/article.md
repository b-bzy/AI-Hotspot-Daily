<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub AI 热点：上榜项目集中在工具与应用层
2. mattpocock/skills 24 小时新增近 1,400 star，另两个 AI 应用同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时合计新增约 2,400 star
当前使用：候选 1
-->

# 今日 GitHub AI 热点：上榜项目集中在工具与应用层

> 今天 GitHub Trending 日榜上的 AI 项目都不在模型层，而落在工具与应用层：一个把 coding agent 的日常技能整理成可复用模块，两个把生成式模型装进桌面应用。其中后两个都通过 MCP 与 Claude、Cursor 等 agent 打通。

---

## 1. mattpocock/skills — 面向工程实践的 coding agent 技能集

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 138k | 1,395 | Shell | MIT |

skills 是 TypeScript 教育者 Matt Pocock 公开的个人 `.claude` 技能目录，定位是"给真正写应用的工程师用的 agent 技能，而不是 vibe coding"。它想解决 coding agent 的两类常见失败：一是 agent 没按预期做（需求没对齐），二是 agent 输出过于啰嗦。

与 GSD、BMAD、Spec-Kit 这类"接管整个开发流程"的方案不同，作者把能力拆成小而可组合的技能，强调可改写、与具体模型无关。最典型的是 `/grill-me` 和 `/grill-with-docs`——在动手前让 agent 反过来追问你究竟要做什么，先对齐再开工；另有 `/triage` 等围绕 issue 管理的技能。安装走 `npx skills@latest add mattpocock/skills`，再运行 `/setup` 选择 issue tracker（GitHub / Linear / 本地文件）。

适合已经在用 Claude Code、Codex 等 coding agent、想把协作流程规范化的工程师。项目创建于 2026 年 2 月，以 MIT 协议发布，star 数已超过 13 万，在 coding agent 技能这个细分方向里属于头部。

🔗 项目地址：https://github.com/mattpocock/skills

---

## 2. Palmier Pro — 把生成式 AI 接进时间线的 Mac 视频编辑器

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 3.5k | 902 | Swift | GPL-3.0 |

Palmier Pro 是一个用 Swift 从零写的 macOS 开源视频编辑器，对标 Premiere Pro，区别在于把 AI 放进了剪辑流程：用户和 agent 可以在同一条时间线上一起生成、编辑视频。

它有两条接入路径。一是内置生成式 AI，可在时间线里直接调用 Seedance、Kling、Nano Banana Pro 等模型生成视频和图像；二是通过 MCP 与外部 agent 打通——应用打开后会在本地 `127.0.0.1:19789` 暴露一个 MCP server，可接入 Claude Code、Codex、Cursor，让 agent 直接操作工程。开源范围上，编辑器本体、MCP server 和 agent 对话都开源，只有生成式 AI 的处理是闭源的；编辑器免费、无需登录，生成式功能则需要登录订阅。

适合 Apple Silicon Mac 用户（需 macOS 26 Tahoe）、想把 AI 生成接进正式剪辑流程的创作者。项目来自 YC S24 团队，开源约两个月，今日新增 902 star 在榜单里居前。它以 GPL-3.0 协议发布，商用前需注意合规。

🔗 项目地址：https://github.com/palmier-io/palmier-pro

---

## 3. Voicebox — 本地优先的开源 AI 语音工作站

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 31k | 145 | TypeScript | MIT |

Voicebox 把语音的输入和输出合并到一个本地应用里，定位是 ElevenLabs（偏合成输出）和 WisprFlow（偏听写输入）的开源替代。它能从几秒钟参考音频做零样本音色克隆，用全局快捷键把语音听写进任意输入框，也能给支持 MCP 的 AI agent 配一个用户自己的音色。

README 称它内置 7 个 TTS 引擎（Qwen3-TTS、Qwen CustomVoice、LuxTTS、Chatterbox Multilingual 与 Turbo、HumeAI TADA、Kokoro），支持 23 种语言，并自带 50 多个预置音色。模型、语音数据和录音都留在本机（local-first），同时捆绑了一个本地 LLM，用于文本润色和按 profile 切换的人格设定。

适合对隐私敏感、不想把语音数据上传云端，又需要克隆、合成、听写一整套能力的个人用户。项目创建于 2026 年 1 月，star 数已有规模，以 MIT 协议发布。

🔗 项目地址：https://github.com/jamiepine/voicebox

---

## 今日观察

今天的三个项目都不在模型层，而在工具与应用层：一个把 coding agent 的技能整理成可复用的小模块，两个把生成式视频和语音模型包进桌面应用。值得注意的是，Palmier Pro 和 Voicebox 都选择通过 MCP 与 Claude、Cursor 等 agent 打通，"模型能力 + 本地应用 + agent 接口"正在成为一种常见组合。

---

**Tags**：#GitHub热点 #AIagent #MCP #生成式视频 #AI语音
