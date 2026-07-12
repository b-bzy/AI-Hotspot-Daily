<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub Trending：agentic skills 框架继续占据日榜前列
2. Superpowers 登上今日 Trending，另两个 AI 项目同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时合计新增超 2,300 star
当前使用：候选 1
-->

# 今日 GitHub Trending：agentic skills 框架继续占据日榜前列

> 今天日榜上的 AI 热度，集中在"给编码代理装技能"这件事上。三个入选项目里，两个是面向 Claude Code 等工具的 agentic skills 框架，一个是 LLM 推理的 KV 缓存基础设施。

---

## 1. Superpowers — 给编码代理装一套软件开发方法论的技能框架

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 226k | 1,275 | Shell | MIT |

Superpowers 解决的问题是：让编码代理（Claude Code、Codex、Cursor 等）不要一上来就写代码，而是先把需求聊清楚、产出规格、再做实现计划。它把这一整套流程拆成可组合的"技能"（skills），代理识别到你在构建东西时会自动触发，无需手动调用。

与单纯的提示词集合不同，Superpowers 把开发方法论固化进了流程：强调红绿 TDD、遵循 YAGNI 和 DRY，再用"子代理驱动开发"让多个代理分别完成并互相审查各自的工程任务。作者称代理可按既定计划自主工作数小时。项目通过 Anthropic 官方插件市场和自建 marketplace 分发。

适合已经在用编码代理、但希望约束其行为、减少跑偏的开发者。项目 2025 年 10 月开源，目前已积累约 226k star。

🔗 项目地址：https://github.com/obra/superpowers

---

## 2. LMCache — 为大模型推理提供 KV 缓存复用的基础设施

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 8.7k | 28 | Python | Apache-2.0 |

LMCache 针对的是 LLM 推理里的一个具体瓶颈：每次请求都要重新计算 KV cache，在长上下文和多轮对话场景下浪费明显。它把 KV cache 在 GPU、CPU 内存乃至多节点之间存储和复用，让相同或重复的上下文不必重复计算。

它与 vLLM、NVIDIA Dynamo 等推理框架做了集成，topics 中列出 cuda、rocm、vllm，覆盖 N 卡和 AMD 两条硬件路线。据其官方博客，2026 年 4 月发布的多进程架构把 MoE 推理性能提升约 10 倍（具体口径以官方博客为准），项目已加入 PyTorch 基金会生态。相比上面两个上线半年多的热门项目，LMCache 创建于 2024 年 5 月，节奏更平稳。

适合需要部署大模型推理服务、关注吞吐和显存成本的团队参考。

🔗 项目地址：https://github.com/LMCache/LMCache

---

## 3. agency-agents — 一组带人设的 AI subagent 集合

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 113k | 1,026 | Shell | MIT |

agency-agents 提供的是一批"带人设"的 AI 代理角色——前端开发、社区运营、文案等不同岗位各一个。每个代理是一个 markdown 定义文件，包含身份设定、工作流程、交付物示例和成功指标，可以放进 Claude Code 的 agents 目录直接调用。

与 Superpowers 偏"方法论"不同，agency-agents 偏"角色库"：它不约束开发流程，而是按职能把专家拆成可调用的子代理，并提供转换脚本，适配 Copilot、Gemini CLI、Cursor、Aider、Windsurf、Codex 等多种工具。项目起源于一个 Reddit 讨论帖，经过数月迭代。

适合想给编码代理快速补上某类岗位能力、又不想从零写 prompt 的用户。项目 2025 年 10 月开源，已积累约 113k star。

🔗 项目地址：https://github.com/msitarzewski/agency-agents

---

## 今日观察

今天三个项目里有两个是面向编码代理的 agentic skills / subagent 框架，延续了最近日榜上"给 AI 代理装技能"的热度；LMCache 则代表另一条线——把大模型推理的工程成本降下来。一个偏应用层封装，一个偏底层基础设施，方向不同，但都围绕"让大模型真正用起来"展开。

---

**Tags**：#GitHub热点 #AI开源 #AgenticSkills #ClaudeCode #LLM推理
