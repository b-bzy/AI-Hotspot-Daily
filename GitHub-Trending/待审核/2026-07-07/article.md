<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub AI 项目：围绕编码 Agent 的工具层继续变厚
2. claude-skills 登顶今日 AI 榜，另两个编码 Agent 工具同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时合计新增超 1.6k star
当前使用：候选 1
-->

# 今日 GitHub AI 项目：围绕编码 Agent 的工具层继续变厚

> 今天日榜上排名靠前的 AI 项目，方向出奇地一致：都在给编码 Agent 补周边。一个做技能库，一个做用量监控，一个给模型加"看视频"的能力。三者都不是新模型，而是围绕 Claude Code、Codex 这类工具搭生态。

---

## 1. claude-skills — 面向多种编码 Agent 的技能与插件合集

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 21.4k | 610 | Python | MIT |

这个项目解决的问题是"技能复用"。它把工程、运维、市场、安全、合规、产品研究等场景，打包成一批可直接安装的 skill、插件和 agent 定义。按仓库自述，目前收录 355 个技能、30 多个 agent、70 多个自定义命令，覆盖从代码开发到 C-level 顾问角色的多类任务。

它和单一工具绑定的技能库的差异在于跨工具兼容。除了 Claude Code，仓库还声明可用于 OpenAI Codex、Gemini CLI、Cursor、Aider、Windsurf、Kilo Code、OpenCode 等共 13 种编码 Agent，靠的是统一的 SKILL.md 格式，避免为每个工具单独改写。安全类技能用 PreToolUse hook 做拦截，研究类技能则组织成 litreview、grants、deep-research 等一条链路。

项目创建于 2025 年 10 月，目前 21.4k star，已有一定规模。适合想快速给编码 Agent 补齐特定领域能力、又不想从零写 skill 的开发者参考。

🔗 项目地址：https://github.com/alirezarezvani/claude-skills

---

## 2. CodexBar — 在 macOS 菜单栏查看 AI 编码工具用量的小工具

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 16.8k | 598 | Swift | MIT |

CodexBar 针对的是一个很具体的痛点：用多个 AI 编码工具时，很难随时知道各家的额度还剩多少、下一个计费窗口什么时候重置。它把这些信息放到 macOS 菜单栏，每个服务商一个状态项，并显示各自额度的重置时间。

它的取舍是"不登录也能看"。按自述，工具覆盖 Codex、OpenAI、Claude、Cursor、Gemini、Copilot、Grok、OpenRouter、AWS Bedrock 等 57 家服务商的用量口径，通过读取本地已有的凭据或接口来拉数据，而不要求用户在应用里再走一遍各家的登录流程。它是原生 Swift 应用，要求 macOS 14 及以上，提供 Homebrew 安装。

项目创建于 2025 年 11 月，目前 16.8k star，已有规模。适合同时订阅多家编码工具、需要盯着额度用量的开发者。

🔗 项目地址：https://github.com/steipete/CodexBar

---

## 3. claude-video — 让 Claude 具备"看视频"能力的插件

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 4.6k | 427 | Python | MIT |

这个项目补的是模型的一个盲区：Claude 能读网页、能跑脚本，但默认无法真正"看"一段视频，往往只能靠标题猜，或读一份缺失大量画面信息的字幕。claude-video 提供的 `/watch` 命令，让用户粘贴一个 URL 或本地路径、提出问题，工具再去处理后续步骤。

它的工作流是先字幕、后下载。按自述，命令会先尝试免费字幕，按需下载视频，再做抽帧（支持场景感知抽帧或更快的关键帧模式），生成带时间戳的转录（无字幕时用 Whisper API 兜底），最后把每一帧当作图片交给模型读取。依赖 yt-dlp 和 ffmpeg，首次运行时自动安装，起步阶段基本零配置。除 Claude Code 外，也可通过 agentskills 装到 Codex、Cursor、Copilot、Gemini CLI 等宿主里。

项目创建于 2026 年 4 月，目前 4.6k star，已有一定关注度。适合需要让 Agent 处理视频内容、做视频问答或内容提取的场景。

🔗 项目地址：https://github.com/bradautomates/claude-video

---

## 今日观察

今天上榜的三个 AI 项目，指向的是同一件事：编码 Agent 本身的能力已经不是唯一焦点，围绕它的工具层——技能分发、用量监控、能力扩展——正在快速补齐。三者形态各异，但都默认要兼容 Claude Code、Codex、Cursor 等多个宿主，跨工具适配正在成为这类周边项目的共同前提。

---

**Tags**：#GitHub热点 #AI开源 #ClaudeCode #编码Agent #开发者工具
