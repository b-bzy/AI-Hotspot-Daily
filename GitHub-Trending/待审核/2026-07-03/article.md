<!--
标题候选：
1. 今日 GitHub AI 项目：AI Agent 工具链持续走热
2. usestrix/strix 登顶今日 Trending，另两个 AI 工具同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时新增超 3600 star
当前正在使用：候选 1
-->

# 今日 GitHub AI 项目：AI Agent 工具链持续走热

> 今天的 GitHub Trending 日榜上，AI 相关项目集中在给现有 Agent 配专用工具这个方向。安全测试、Token 压缩、视频剪辑三个具体场景各有一个项目挤进日增星榜前列，值得关注。

---

## 1. usestrix/strix — 用自主 AI Agent 做渗透测试的开源工具

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 32.4k | 2,137 | Python | Apache-2.0 |

Strix 要解决的问题是把渗透测试自动化。它让多个 AI Agent 组队，像真实攻击者一样运行目标代码、寻找漏洞，并通过可运行的漏洞利用（PoC）验证问题是否真实存在，而不是像传统静态扫描工具那样给出大量误报。

和常见的静态代码扫描器相比，Strix 的核心差异在"验证"环节——每个发现的漏洞都配一份可运行的 PoC，同时给出修复补丁和合规格式的测试报告。项目支持接入 OpenAI、Anthropic、Google 等主流 LLM 服务商，也可以直接嵌入 CI/CD 流水线，在 Pull Request 阶段拦截存在漏洞的代码。仓库创建于 2025 年 8 月，运行近一年后积累到 3.2 万 star，已有一定规模。

适合需要频繁做安全测试、又没有专职渗透测试团队的开发团队，也可用于自动化 Bug Bounty 场景下的漏洞验证与报告生成。

🔗 项目地址：https://github.com/usestrix/strix

---

## 2. caveman — 让 Claude Code 少说话、多干活的开源 skill

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 81.2k | 926 | JavaScript | MIT |

caveman 解决的是编码 Agent 输出太啰嗦的问题。它是一个可以装进 Claude Code、Codex、Cursor 等 30 多种编码工具的 skill/插件，让模型用更简短的表达方式回答问题，官方给出的数据是单次回复的输出 Token 减少约 75%，同时保持技术信息不丢失。

具体做法是压缩表达风格而不是压缩内容本身——用户用什么语言提问，caveman 就用同一种语言的精简版本作答，代码、命令、报错信息保持原样不做压缩。项目还提供 lite / full / ultra / wenyan 四档压缩强度，供用户按场景切换。仓库创建于 2026 年 4 月，三个月内积累到 8.1 万 star。

适合日常高频使用 AI 编码助手、对 Token 花费敏感的开发者，也适合团队内需要长时间保持上下文对话的场景。

🔗 项目地址：https://github.com/JuliusBrussee/caveman

---

## 3. video-use — 用 Claude Code 剪辑视频的开源工具

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 13.9k | 554 | Python | MIT |

video-use 把剪视频这件事变成一句自然语言指令。用户把原始素材丢进一个文件夹，在 Claude Code 里说一句"把这些剪成一条发布视频"，Agent 就会输出成片，覆盖 Vlog、访谈、教程、旅行记录等常见类型，不需要打开传统剪辑软件的时间线和菜单。

技术实现上，模型不直接"看"视频，而是靠 ElevenLabs Scribe 生成的带时间戳文字转录、说话人分离和音频事件标注来定位剪辑点，这些信息打包成一份约 12KB 的文本文件供模型阅读。项目还支持通过 HyperFrames、Remotion、Manim 等工具生成动画贴图，并在每次剪辑后做自检，确认输出内容再展示给用户。仓库由 browser-use 团队维护，2026 年 4 月开源。

适合需要批量处理访谈或教程类素材、又不想学习专业剪辑软件的内容创作者。

🔗 项目地址：https://github.com/browser-use/video-use

---

## 今日观察

今天入选的三个项目有一个共同点：都不是在做更强的模型，而是在给已有的 AI Agent 配专用工具——测漏洞、省 Token、剪视频，三个具体场景各自落地，方向差异明显。

---

**Tags**：#GitHub热点 #AI开源 #AIAgent #ClaudeCode #渗透测试
