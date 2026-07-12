<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub AI 热点：从造 agent 到接模型，工具链成为主线
2. Google agents-cli 登上今日 Trending，另两个 AI 项目同样值得关注
3. 今日 GitHub AI 三连：新增 445 / 387 / 252 star 的三个方向
当前使用：候选 1
-->

# 今日 GitHub AI 热点：从造 agent 到接模型，工具链成为主线

> 今天日榜上 AI 相关项目集中在"工具链"这一层：一个帮你造 agent，一个帮你接模型，还有一个帮你从头学 AI。三者面向的不是同一批用户，但都在解决"怎么把大模型用起来"的具体环节。下面按今日新增 star 排序介绍。

---

## 1. agents-cli — 让编码助手学会在 Google Cloud 上造 agent 的命令行工具

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 4.3k | 445 | Python | Apache-2.0 |

这是 Google 官方在 4 月开源的项目，解决的问题很具体：在 Gemini Enterprise Agent Platform（Google Cloud 的 agent 平台）上构建、评测和部署 agent 时，开发者原本要自己摸清一整套 CLI 和云服务。agents-cli 把这些环节封装成"技能"，让 Claude Code、Codex、Antigravity CLI 等编码助手直接调用。

它的做法是给编码助手补上一组 skills 和命令，安装用 `uvx google-agents-cli setup` 或 `npx skills add google/agents-cli` 一行完成。用户在对话里描述需求，由编码助手代为调用底层平台，而不用逐个记服务名和参数。换句话说，它把"人去学一整套云上 agent 工具"改成了"让编码助手替你学"，思路上和当下流行的 skills 生态一致。

适合已经在用 Google Cloud、并且日常靠编码助手写代码的团队参考。项目开源约 3 个月，来自 Google 官方仓库，已有一定关注度。

🔗 项目地址：https://github.com/google/agents-cli

---

## 2. OmniRoute — 把多家模型聚合到单个端点的 AI 网关

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 8.6k | 387 | TypeScript | MIT |

OmniRoute 是一个 AI 网关，把多家模型服务商聚合到一个统一端点。按项目说明，它接入了 200 多个 provider、其中 50 多个带免费额度，Claude Code、Cursor、Cline、Copilot 这类工具改一下接入地址就能切换到不同的 Claude / GPT / Gemini 模型，并在某个服务不可用时自动回退。

技术上它支持 MCP 与 A2A 协议、多模态 API，并提供桌面端和 PWA。项目还宣称通过一套压缩策略能减少 15%–95% 的 token 消耗——这一数字来自项目自述，具体效果取决于使用场景，需实测验证。

适合需要在多家模型间灵活切换、或想统一管理接入方式的开发者。项目今年 2 月创建，已有一定关注度。

🔗 项目地址：https://github.com/diegosouzapw/OmniRoute

---

## 3. AI-For-Beginners — 微软的 12 周 AI 入门课程

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 49k | 252 | Jupyter Notebook | MIT |

这是微软维护的一套 AI 入门课程，结构为 12 周、24 节课，包含讲解、测验和动手实验。内容覆盖神经网络、计算机视觉（CNN）、自然语言处理（RNN、NLP）、生成模型（GAN）以及 AI 伦理，代码同时用 TensorFlow 和 PyTorch 演示，并提供多语言自动翻译版本。

它 2021 年开源、目前总 star 接近 5 万，属于已有规模、被多个团队和学习者使用的教学项目。相比追新的 agent 框架，这类课程的价值在于把基础概念讲清楚。

适合刚入门、想按周有节奏地系统学一遍 AI 基础的读者。

🔗 项目地址：https://github.com/microsoft/AI-For-Beginners

---

## 今日观察

今天三个项目正好落在 AI 使用链条的三个环节：造 agent（agents-cli）、接模型（OmniRoute）、学基础（AI-For-Beginners）。前两个都在围绕"让编码助手接入更多能力"做文章，一个补平台技能、一个补模型入口，反映出 agent 工具化仍是当前的热点方向；第三个是维护多年的老项目重新出现在日榜，说明 AI 入门教育始终有稳定关注，并非只有追新的框架才能上榜。

---

**Tags**：#GitHub热点 #AI开源 #AIAgent #AI网关 #开源课程
