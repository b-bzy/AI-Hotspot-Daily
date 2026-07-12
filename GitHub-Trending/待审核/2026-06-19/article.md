<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub AI 热点：大模型、编码 agent 与音视频生成同台
2. kilocode 领跑今日 Trending，GLM-5 与 LTX-2 同样值得关注
3. 今日 GitHub AI：3 个开源项目 24 小时合计新增约 1,600 star
当前使用：候选 1
-->

# 今日 GitHub AI 热点：大模型、编码 agent 与音视频生成同台

> 今天 GitHub Trending 日榜上的 AI 项目方向比较分散，没有集中在某一个细分赛道。我们从中挑了三个信息量较足的项目：一个开源大模型系列、一个 AI 编码 agent、一个音视频生成模型，分别代表当前开源 AI 的三条主线。

---

## 1. GLM-5 — Z.ai 面向长程 agentic 任务的开源大模型系列

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 4.2k | 202 | 无（模型仓库） | Apache-2.0 |

GLM-5 是一个面向复杂系统工程和长程 agentic 任务的开源大模型，仓库里同时收录了 GLM-5、GLM-5.1、GLM-5.2 三个版本的说明与权重入口。它想解决的是模型在长任务里"开局发力、很快见顶"的问题，README 里把"在数百轮、数千次工具调用中持续优化"作为主要设计目标。

技术路线上，相比 GLM-4.5，GLM-5 的参数量从 355B（激活 32B）扩到 744B（激活 40B），预训练数据从 23T tokens 增加到 28.5T，并引入 DeepSeek Sparse Attention 来降低部署成本。最新的 GLM-5.2 把上下文长度做到 1M token，官方给出的 Terminal-Bench 2.1 得分为 81.0，高于 GLM-5.1 的 62.0，并称在该项上接近 Claude Opus 4.8 的 85.0。这些数字来自项目自述，尚未经第三方复测。

适合关注开源模型在编码、终端操作和多轮工具调用方向进展的开发者与研究者。模型以 Apache-2.0 协议发布。

🔗 项目地址：https://github.com/zai-org/GLM-5

---

## 2. kilocode — 覆盖 VS Code / JetBrains / CLI 的开源 AI 编码 agent

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 22.3k | 1,345 | TypeScript | MIT |

Kilo Code 是一个开源 AI 编码 agent，目标是在 VS Code、JetBrains 和命令行三种环境里都能用。它主打"开放定价"：用户可以从 500 多个模型里挑选，按模型供应商的原价付费、不额外加价，起步阶段也不需要自带 API key。

和单一绑定某个模型的编码工具相比，kilocode 的差异在于把"模型选择"做成了可随时切换的能力，并按职责拆出 Code、Plan、Ask、Debug、Review 五种预设 agent，分别负责写代码、做架构规划、回答代码库问题、排查问题和审查改动，也支持自定义 agent。功能上提供跨文件代码生成、ghost-text 行内补全、终端与浏览器控制，以及一个用于接入 MCP server 的 marketplace；README 里列出的可调用模型包括 GPT-5.5、Claude Opus 4.7、Gemini 3.1 Pro Preview 等。

适合希望在多个 IDE 之间统一 AI 编码工作流、又想自己掌控模型选择和成本的开发者。MIT 协议。

🔗 项目地址：https://github.com/Kilo-Org/kilocode

---

## 3. LTX-2 — Lightricks 的开源音视频生成基础模型

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 7.5k | 51 | Python | 自定义 |

LTX-2 是 Lightricks 推出的音视频生成模型，这个仓库提供官方的 Python 推理代码和 LoRA 训练工具。README 称它是"首个基于 DiT 的音视频基础模型"，可以在同一个模型里同时生成相互同步的音频和视频，并提供多种性能模式。

工程实现上，配套的 LTX-2.3 权重托管在 HuggingFace，主检查点为 22B 参数，另提供蒸馏版本、空间与时间超分模块以及蒸馏 LoRA，文本编码器用的是 Google 的 Gemma 3（12B）。当前仓库里的推理流程采用两阶段管线：先生成，再做空间超分。

适合做文本到音视频生成、需要在本地跑生成管线或训练自定义 LoRA 的团队。需要注意的是，该项目采用自定义协议（非标准 OSI 许可），商用前应先查看仓库 LICENSE。

🔗 项目地址：https://github.com/Lightricks/LTX-2

---

## 今日观察

今天上榜的三个 AI 项目方向各异：一个基础大模型、一个编码 agent、一个音视频生成模型。如果说有共同点，那就是 GLM-5 和 kilocode 都把重心放在了"agentic 编码"上——一个在模型层做长程任务能力，一个在工具层做多模型调度，反映出代码场景仍是当前开源 AI 较主要的落地方向之一。

---

**Tags**：#GitHub热点 #AI开源 #大模型 #AI编程 #视频生成
