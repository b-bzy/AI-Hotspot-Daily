<!--
标题候选：
1. 今日 GitHub AI 热点：智能体安全与工程流程插件成为主线
2. EveryInc 复合工程插件登顶今日 AI 类 Trending，另两个项目同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时新增合计超 700 star
当前使用：候选 1
-->

# 今日 GitHub AI 热点：智能体安全与工程流程插件成为主线

> 今天的 GitHub Trending 日榜上，AI 相关的新鲜选题集中在两个方向：给企业里的 AI 编程智能体做安全检测，以及把"先规划后动手"的工程流程打包成插件。这两个项目分别对应了 AI 智能体从"能用"到"敢用"的两道关卡。第三个入选项目是一个走极简路线的自托管项目管理工具。

---

## 1. EveryInc/compound-engineering-plugin — 给 Claude Code 装上"先规划后动手"的工程流程

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 23.9k | 40 | TypeScript | MIT |

传统开发习惯把大部分精力放在写代码上，遇到问题临时想方案，容易返工、留技术债。这个插件把这个比例倒过来：官方给出的原则是 80% 时间用在规划和评审，20% 用在执行，让每一次开发的产出都能降低下一次的成本。

它不是一个单独的 prompt，而是由 32 个技能（skill）组成的工作流。核心循环是 `/ce-brainstorm`、`/ce-plan`、`/ce-work`、`/ce-simplify-code`、`/ce-code-review`、`/ce-compound` 六步，每一步的产出写进 `docs/solutions`、`docs/plans` 目录，供后续开发复用。旗舰命令 `/lfg` 能把整套流程自动跑完：规划、实现、简化、评审、提交、开 PR、盯 CI、修复失败直到通过。

适合已经在用 Claude Code、Cursor 或 Codex 做日常开发、想把零散 prompt 习惯升级成可复用工作流的团队；项目同时支持 Cline、Devin CLI、GitHub Copilot 等十余种工具。

🔗 项目地址：https://github.com/EveryInc/compound-engineering-plugin

---

## 2. uber/ADR — 给企业里的 AI 编程智能体做安全检测

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 731 | 148 | Python | Apache-2.0 |

ADR（Agentic AI Detection and Response）要解决的问题很具体：当 Cursor、Claude Code、Codex 这些 AI 编程智能体在企业内部大规模使用时，谁来记录它们到底执行了哪些操作，有没有被提示词注入（prompt injection）劫持。ADR 把智能体的意图、工具调用和执行轨迹记录下来，供安全团队复盘。

检测部分用了双智能体架构：一层做高召回率的初筛，另一层对可疑会话做更深入的推理判断。配套的 ADR-Bench 基准包含 300 多个任务、覆盖 133 个 MCP server 和 17 种已知攻击手法，用来测试防御方案是否顶用。这套系统已经在 Uber 内部生产环境运行，相关研究被 MLSys 2026 收录。

适合已经把 AI 编程智能体接入企业内部流程、需要审计和威胁检测能力的安全团队参考；目前开源版本只做观测和检测，不含拦截阻断能力。

🔗 项目地址：https://github.com/uber/ADR

---

## 3. usekaneo/kaneo — 一个走极简路线的自托管项目管理工具

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 7.3k | 559 | TypeScript | MIT |

Kaneo 想解决的是市面上项目管理工具功能越堆越多、界面越用越重的问题。它把自己定位成 Jira 或 Linear 的轻量替代品，核心诉求是只保留真正需要的功能，看板和任务追踪走极简界面。

部署上它支持 Docker Compose 或自带的命令行工具一键起服务，后端用 PostgreSQL，项目用 pnpm workspaces 加 Turborepo 管理 monorepo，也提供 Kubernetes/Helm 方案给需要私有化部署的团队。一个值得一提的细节是它内置了 MCP server，能让 Claude 这类 AI 助手直接读写任务看板。

适合想要自托管、不愿意把项目数据交给第三方 SaaS 的小团队，以及已经在用 AI 助手辅助项目管理的开发者。

🔗 项目地址：https://github.com/usekaneo/kaneo

---

## 今日观察

今天候选池里真正新鲜的 AI 项目不多——不少高星 AI 项目在过去 90 天内已经写过。今天留下来的两个 AI 选题都偏工具链：一个管"智能体怎么写代码更规范"，一个管"智能体写代码安全不安全"，而不是模型或应用本身；补位的 Kaneo 则说明开发者对轻量自托管工具的需求一直都在。

---

**Tags**：#GitHub热点 #AI开源 #AI智能体安全 #ClaudeCode插件 #MCP
