<!--
标题候选：
1. 今日 GitHub AI 项目：Claude 技能生态成关注焦点
2. ComposioHQ 千款 Claude Skills 清单登顶今日 Trending，另两个项目同样值得关注
3. 今日 GitHub AI 热点：一个项目 24 小时新增超 1.6k star
当前使用：候选 1
-->

# 今日 GitHub AI 项目：Claude 技能生态成关注焦点

> 今天的 GitHub 日榜上，AI 相关项目集中在 Claude Code 的技能（Skills）生态本身：一份收录千款技能的清单和一个专门优化输出格式的技能同时登上榜单。日榜前列另有一个自动化部署平台，24 小时新增超 1.3k star，一并列入观察。

---

## 1. ComposioHQ/awesome-claude-skills — 收录千款 Claude Skills 的资源清单

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 68.9k | 163 | Python | Apache-2.0 |

这份清单解决的是一个具体问题：Claude 这类 AI 助手默认只输出文本，遇到"发邮件""建 Issue""发 Slack 消息"这类需要真正执行动作的任务就无能为力。项目收录了 1,000 多个可直接使用的 Claude Skills，每个技能打包了指令、脚本和参考资料，让 Agent 具备跨系统执行任务的能力。

技术上，Skills 采用统一的 `SKILL.md` 格式（YAML frontmatter + Markdown 指令），并使用了一种分层加载机制：Agent 一开始只加载技能名称和简介（约 100 token），只有命中相关任务时才加载完整内容（约 5,000 token），借此控制上下文消耗。项目也特别说明了 Skills 和 MCP 的边界：MCP 负责鉴权与传输，Skills 负责定义工作流，两者不是同一层的东西。目前兼容 Claude.ai、Claude Code、Claude API，以及 OpenAI Codex、Cursor、Gemini CLI 等第三方 Agent 工具。

适合已经在用 Claude Code 或类似 Agent 工具、想快速接入文档处理、数据分析、CRM 或工单系统等具体场景的开发者参考。

🔗 项目地址：https://github.com/ComposioHQ/awesome-claude-skills

---

## 2. ayghri/i-have-adhd — 让编码 Agent 少说废话、直接给答案的技能

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 8.5k | 1.7k | Python | MIT |

这个技能解决的是编码 Agent 常见的一个体验问题：面对一个具体问题，Agent 往往先来一段"好问题，让我想想……"的铺垫，再绕几圈才给出可执行的步骤，关键信息被埋在冗长的解释里。项目把这类输出重新组织成"先给动作，后给解释"的结构。

具体做法是一套 10 条格式规则：优先给出可执行的下一步、多步骤任务按编号排列、结尾落在具体行动上、压缩无关信息、每轮对话重申上下文、给出具体的时间估算、让进度可见、遇到错误直接说明而不做过度铺垫、列表最多保留 5 项、砍掉开场白与总结性套话。项目说明这套规则借鉴自《The Adult ADHD Tool Kit》一书中面向成人 ADHD 患者的任务管理方法，改造后用于规范 LLM 的输出模式。目前通过 Claude Code 插件市场分发，同时支持 Claude 和 Codex 两类 Agent，用户也可以 fork 后自行修改 `SKILL.md`。

适合日常高频使用编码 Agent、觉得当前回复太啰嗦、想要更快拿到可执行步骤的开发者。

🔗 项目地址：https://github.com/ayghri/i-have-adhd

---

## 3. oblien/openship — 自托管的一体化部署平台

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 7.4k | 1.3k | TypeScript | Apache-2.0 |

Openship 解决的是自托管部署里配置繁琐的问题：项目描述里写的是"推代码、发容器、管基础设施"，不需要手写流水线文件或 YAML 配置。它会自动识别应用技术栈，覆盖 Node、Python、Go、Rust、PHP、Ruby、Java、.NET、Docker 以及 monorepo 结构，并处理后续的部署编排。

和需要自己拼装 CI/CD 流程的方案相比，Openship 把数据库管理（Postgres、MySQL、MongoDB、Redis）、Let's Encrypt 自动签发的 SSL 证书、支持 HTTP/3 的 CDN、邮件服务、定时备份与恢复、实时监控面板这些基础设施能力内置到了同一套系统里。项目提供桌面客户端（面向个人开发者）、Web 控制台（面向团队协作）和 CLI（面向服务器端部署）三种入口，界面在托管云、Hetzner/DigitalOcean/Linode/OVH 等 VPS、独立服务器和多服务器集群之间保持一致，底层用标准 Docker 容器封装，理论上可以在不同服务商之间迁移而不被锁定。项目用 TypeScript 编写，采用 Bun 作为包管理器的 monorepo 结构。

适合不想为每个项目单独搭 CI/CD、又希望能随时更换服务器提供商的独立开发者和小团队。

🔗 项目地址：https://github.com/oblien/openship

---

## 今日观察

今天能进入候选池的 AI 项目只有两个，且都围绕 Claude Code 的技能（Skills）生态展开——一个是技能清单，一个是技能本身，说明这套生态目前的活跃度更多体现在"围绕 Agent 怎么用"上，而不是底层模型或训练方法的更新。日榜的其余位置被部署平台、窗口管理器、通信框架这类基础设施类项目占据，今天的补位项目 Openship 24 小时新增 star 数反而超过两个 AI 项目之和。

---

**Tags**：#GitHub热点 #AI开源 #ClaudeSkills #Agent工具 #自托管部署
