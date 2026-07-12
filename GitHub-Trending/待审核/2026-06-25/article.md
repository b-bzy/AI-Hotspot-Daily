<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub Trending：AI 编程 Agent 工具集体上榜
2. 谷歌 design.md 登上今日 Trending，另两个 Agent 项目同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时合计新增超 1100 star
当前使用：候选 1
-->

# 今日 GitHub Trending：AI 编程 Agent 工具集体上榜

> 今天的 GitHub 日榜前列被围绕「编程 Agent」的工具占据。下面这三个项目分别从设计规范、并行编排和招聘场景三个角度切入，体现了 Agent 工具链正在往具体工作流里落地。

---

## 1. design.md — 给 AI 编程 Agent 提供设计系统规范的格式标准

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 17.5k | 619 | TypeScript | Apache-2.0 |

design.md 由谷歌 Google Labs 团队维护，要解决的问题很具体：让 AI 编程 Agent 在生成界面时，能稳定遵循一套既定的设计系统，而不是每次都重新猜配色和字号。它定义了一种叫 DESIGN.md 的文件格式，把一个产品的视觉规范写成 Agent 可以反复读取的结构化文档。

和直接把一份设计稿丢给模型不同，DESIGN.md 把内容分成两层：YAML 前置数据里放机器可读的设计 token，也就是颜色、字号、圆角、间距这些精确数值；正文则用 Markdown 写清楚这些取值背后的理由和适用场景。项目还配了命令行工具，`npx @google/design.md lint` 可以校验文件是否符合规范、检查颜色对比度是否达到 WCAG 标准，并把结果以 JSON 形式输出给 Agent 使用；`diff` 命令用于比较两个版本之间 token 的增删改。

它适合已经在用 AI 编程 Agent 生成前端界面、又希望产出保持设计一致性的团队参考。项目创建于 2026 年 4 月，目前 star 数已超过 1.7 万。

🔗 项目地址：https://github.com/google-labs-code/design.md

---

## 2. Orca — 并行运行多个编程 Agent 的开发环境

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 6.9k | 331 | TypeScript | MIT |

Orca 把自己定位为 ADE（Agent 开发环境），针对的是同时使用多个编程 Agent 时的协调问题。它允许用户在一个界面里并行运行 Codex、Claude Code、OpenCode、Pi 等多个编程 Agent，每个 Agent 跑在各自独立的 git worktree 里，互不干扰，进度统一在一处追踪。

和单个编程 Agent 工具的差异在于，Orca 本身不绑定具体模型，而是充当编排层：用户用自己的订阅接入不同 Agent，把同一个需求分发给多个 Agent 同时执行，再对比结果、合并表现最好的那一个。它还提供移动端 App，可以在手机上查看 Agent 运行状态、收到完成通知并补发指令。桌面端支持 macOS、Windows 和 Linux。

它适合需要同时管理多个编程 Agent、并希望横向比较不同 Agent 输出的开发者。项目由 YC 投资，创建于 2026 年 3 月。

🔗 项目地址：https://github.com/stablyai/orca

---

## 3. hiring-agent — 用本地或云端 LLM 给简历打分的流水线

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 2.3k | 203 | Python | MIT |

hiring-agent 是一条「简历到评分」的处理流水线。它先把简历 PDF 解析成 Markdown 文本，再用 LLM 抽取出结构化的 JSON 字段，结合候选人的 GitHub 主页和仓库信号做补充，最后输出一份带分项评分、评分依据、加分项和扣分项的评估结果。

在技术取舍上，它强调可解释和公平：评估环节带有公平性约束，每一项打分都附带证据，而不是只给一个总分。模型后端可以二选一，用 Ollama 跑本地模型，或接入 Google Gemini，前者适合对简历数据隐私敏感的场景。整个流程由 pymupdf、Jinja 模板和 Pydantic 数据模型串起，代码按 PDF 解析、字段抽取、GitHub 补充、评分四步拆分。

它适合想把简历初筛结构化、又希望评分过程可追溯的技术招聘团队。项目创建于 2025 年 7 月，本次重新登上日榜。

🔗 项目地址：https://github.com/interviewstreet/hiring-agent

---

## 今日观察

今天榜单靠前的几个 AI 项目有个共同点：都不是新模型，而是围绕「编程 Agent」的工具层——一个负责喂设计规范，一个负责并行编排，一个把 Agent 用到招聘场景。Agent 能力正在从「能不能用」转向「怎么用得更顺手」。

---

**Tags**：#GitHub热点 #AI开源 #编程Agent #设计系统 #简历评分
