<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub AI 项目：Agent 技能生态从扩张走向安全治理
2. PM Skills 登顶今日 AI Trending，医疗本地推理与技能安全扫描同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时新增超 2.7k star
当前使用：候选 1
-->

# 今日 GitHub AI 项目：Agent 技能生态从扩张走向安全治理

> 今天的 Trending 日榜上，AI agent 技能相关项目占了近一半席位。入选的三个项目正好覆盖这条生态链的两端——技能市场和安全扫描——外加一个在垂直行业落地的本地推理工具链。

---

## 1. pm-skills — 面向产品经理的 Claude 技能市场

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 16.3k | 1,978 | — | MIT |

pm-skills 解决的问题是：产品经理用通用 AI 助手时，得到的往往是泛泛的文本，而不是结构化的产品决策流程。它把 68 个 PM 技能和 42 条链式工作流打包成 9 个插件，覆盖从需求发现、战略制定、PRD 撰写到发布和增长的完整链路，主要面向 Claude Code 和 Cowork，也兼容其他 AI 助手。

它的差异点在于"框架内置"：每个技能都编码了一套具体的产品方法论——比如 Teresa Torres 的持续发现、Marty Cagan 的产品策略——并以分步引导的方式执行。命令则把多个技能串成端到端流程，例如 `/discover` 会依次调用头脑风暴、假设识别、假设排序、实验设计四个技能。

项目创建于 2026 年 3 月，三个月累计 16.3k star，过去 24 小时新增 1,978，是今日 AI 类项目里涨幅最高的。适合日常用 Claude 做产品工作的 PM，以及想参考"技能市场"组织方式的团队。

🔗 项目地址：https://github.com/phuryn/pm-skills

---

## 2. OpenMed — 全程在本地设备运行的医疗 NLP 工具链

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 2.8k | 426 | Python | Apache-2.0 |

OpenMed 针对的是医疗行业的一个硬约束：患者数据不能离开本地网络。它提供临床文本的实体抽取和 PII 去标识化能力，配套 1,000 多个托管在 HuggingFace 上的专科医疗模型，支持 12 种语言、247 个 PII 检查点，全部在自有硬件上运行，不依赖云端。

技术路线上，它同时覆盖 Python 和 Apple 生态：Python 侧一行代码调用；Swift 侧提供 OpenMedKit 包，基于 Apple MLX 在 iPhone、iPad 和 Mac 上做原生推理。模型方法有 arXiv 论文（2508.01630）支撑。项目 2025 年 10 月开源，目前 2.8k star，已有一定关注度。

适合医院、医疗 ISV 等对数据合规敏感的团队，以及关注端侧推理在垂直行业落地的开发者。

🔗 项目地址：https://github.com/maziyarpanahi/openmed

---

## 3. SkillSpector — NVIDIA 开源的 agent 技能安全扫描器

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 2.8k | 319 | Python | Apache-2.0 |

agent 技能生态扩张带来一个被低估的问题：技能以隐式信任的方式在 Claude Code、Codex CLI、Gemini CLI 等工具里执行，安装前几乎没有审查环节。README 引用的研究数据是：26.1% 的技能存在漏洞，5.2% 表现出疑似恶意意图。SkillSpector 要回答的就是"这个技能装了安不安全"。

它内置 64 种漏洞模式，覆盖提示注入、数据外泄、权限提升、供应链攻击等 16 个类别，采用两段式分析：先跑快速静态分析，再可选接入 LLM 做语义评估，并通过 OSV.dev 实时查询 CVE 数据。输出支持终端、JSON、Markdown 和 SARIF 四种格式，能直接接入 CI/CD，最终给出 0–100 的风险评分。

项目创建于 2026 年 3 月，目前 2.8k star。适合在团队里引入第三方技能前做安全把关的工程师，以及 agent 平台的维护者。

🔗 项目地址：https://github.com/NVIDIA/SkillSpector

---

## 今日观察

技能市场（pm-skills）和技能安全扫描（SkillSpector）同日上榜，说明 agent 技能生态在快速扩张的同时，安全治理工具也开始跟进。OpenMed 则代表另一条线：本地推理在医疗这类合规敏感行业的落地。

---

**Tags**：#GitHub热点 #AI开源 #AgentSkills #本地推理 #医疗AI
