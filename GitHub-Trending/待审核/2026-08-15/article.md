<!--
标题候选：
1. 今日 GitHub AI 热点：AI 工具正从聊天窗口走进具体工作流
2. diagram-design 登顶今日 Trending，另两个项目同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时新增超 4600 star
当前使用：候选 1
-->

# 今日 GitHub AI 热点：AI 工具正从聊天窗口走进具体工作流

> 今日 GitHub Trending 日榜由一个 Claude Code 图表生成技能领跑，24 小时新增 3.6k star。团队协作工具、本地生成模型应用同样上榜，方向各异，但都指向同一件事：AI 正在被嵌进具体的工作环节，而不是停留在对话框里。

---

## 1. diagram-design — 给 Claude Code 生成品牌化编辑级图表的技能

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 17.4k | 3.6k | HTML | MIT |

diagram-design 解决的是一个具体问题：写文档、做架构图时，通用绘图工具生成的方框千篇一律，和网站品牌不搭；手动在 Figma 里画一张图往往要花 30 分钟以上。它作为 Claude Code、Codex、Pi 等 Anthropic 系代理平台的技能安装后，输入一句指令就能在一分钟内生成贴合品牌视觉的图表。

它提供 27 种图表类型，涵盖流程图、架构图、时间线、象限图等，统一输出成不依赖 JavaScript 运行时的纯 HTML/SVG 文件。和基于文本语法、常需要渲染服务的 Mermaid 相比，它多了一步"品牌提取"：分析目标网站后自动抽取主色、字体和语义配色，并做 WCAG AA 对比度校验，同时支持从 draw.io 和 Mermaid 文件导入迁移。

适合技术文档团队、需要频繁产出品牌化图表的产品经理和咨询顾问，以及不想为单张图表打开 Figma 的独立开发者。

🔗 项目地址：https://github.com/cathrynlavery/diagram-design

---

## 2. macro — 把邮件、聊天、任务和 CRM 整合进一个共享 AI 记忆的团队工作空间

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 3,060 | 436 | Rust | AGPL-3.0 |

macro 想解决的是团队工具割裂的问题：一家公司同时用 Slack、Linear、Notion、HubSpot，信息分散在四五个系统里，互相不通。macro 把邮件、聊天、任务、文档、通话和 CRM 放进同一个由图数据库驱动的后端，内容之间可以直接用 @ 互相引用和搜索。

差异化的地方在于它把 AI Agent 当作一等公民：平台维护一份每晚更新的团队级共享记忆，由邮件、消息、任务和通话内容组成，Agent 通过 MCP 协议或外部 API 访问这份记忆。模型层不锁定单一供应商，OpenAI、Google、Anthropic 和 Claude Code 都可以通过模型选择器接入，官方称这是为了保证"最大可迁移性"。

项目基于 AGPL-3.0 协议，提供 Docker Compose 自托管方案，目前面向 15–20 人规模的小团队，用来替换手上散落的多个 SaaS 工具。

🔗 项目地址：https://github.com/macro-inc/macro

---

## 3. Modly — 本地跑开源生成模型，把照片转成 3D 模型的桌面应用

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 6.0k | 579 | TypeScript | MIT |

Modly 解决的问题是把图生 3D 这类生成式 AI 能力从云端搬到本地：上传一张照片或输入一段提示词，模型直接在用户自己的 GPU 上把它转换成 3D 网格，数据不用传到第三方服务器。

它内置的扩展包括 Hunyuan3D 2 Mini（及 Turbo / Fast 变体）、TripoSG 和 Trellis2 GGUF 等开源图生 3D 模型，用户也可以从 GitHub 仓库安装额外的模型清单进行扩展。客户端原生支持 Windows、Linux 和 Apple Silicon 版 macOS（不支持 Intel 芯片），界面里带一个实时 RAM 占用指示器，方便监控本地推理时的资源消耗。

适合需要批量生成 3D 资产、又对数据隐私敏感的开发者和小工作室，也适合把它接入自动化流水线做批处理。

🔗 项目地址：https://github.com/lightningpixel/modly

---

## 今日观察

今天三个项目代表了 AI 落地的三种不同路径：一个是给 AI 编程助手做配套技能，一个是把 Agent 嵌进团队协作系统当"数字同事"，一个是把生成模型完全放到本地跑。共同点是，AI 正从对话框走进具体工作流的某个环节，而不是只停留在聊天窗口里。

---

**Tags**：#GitHub热点 #AIAgent #生成式AI #本地推理 #ClaudeCode
