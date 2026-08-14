<!--
标题候选：
1. 今日 GitHub AI 热点：训练、路由、智能体工作空间三线并进
2. Unsloth 登顶今日 AI 热点，另两个项目补齐大模型基础设施拼图
3. 今日 GitHub AI 热点：3 个项目 24 小时新增超 900 star
当前正在使用：候选 1
-->

# 今日 GitHub AI 热点：训练、路由、智能体工作空间三线并进

> 今天的 GitHub Trending 日榜上，AI 相关项目集中在大模型应用链条的三个不同环节：本地训练部署、多模型路由、以及面向终端用户的智能体工作空间。三个项目都不是新面孔，但过去 24 小时都获得了数百新增 star。

---

## 1. Unsloth — 本地训练和运行大模型的桌面工具

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 71.1k | 328 | Python | Apache-2.0 / AGPL-3.0 |

Unsloth 最早是一个专注"更快、更省显存"的 LLM 微调库，现在已经扩展成一套本地运行、训练大模型的桌面应用和 Web UI，覆盖 Qwen、DeepSeek、Gemma、FLUX 等模型的推理与微调，目标是让开发者不依赖云端算力也能跑通完整训练流程。

README 给出的具体数据包括：标准微调训练速度提升 1.5–2 倍，显存占用减少 50%–80%；MoE 模型训练最高提速 12 倍、显存降低 35%；同时支持 LoRA、QLoRA、全参微调、GRPO/DPO 强化学习和 FP8 训练，导出格式覆盖 GGUF、NVFP4，并可通过 OpenAI 兼容 API 直接对接 Claude Code、Codex 等智能体。

适合需要在本地或单机多卡环境完成模型微调、又不想为训练、导出、部署各环节切换不同工具链的开发者。

🔗 项目地址：https://github.com/unslothai/unsloth

---

## 2. Switchyard — 在多个模型和供应商之间路由 LLM 流量

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 1.3k | 408 | Rust | Apache-2.0 |

Switchyard 解决的是一个具体场景：应用已经接入 OpenAI 或 Anthropic 的 API，但想换成 vLLM、Ollama 或其他供应商的模型。它在客户端和后端模型之间加一层路由，协议层继续保持 OpenAI Chat 或 Anthropic Messages 格式不变，业务代码不用改写。

技术实现上，它提供多种路由策略：按内容分类的 LLM Classifier、依赖对话上下文的 Stage Router、先用弱模型再按需升级的 Escalation Router，以及用于 A/B 测试的固定流量分配策略；后端已支持 vLLM、NVIDIA NIM、Ollama 和 OpenRouter，并输出 Prometheus 指标监控延迟、Token 用量和路由开销。项目由 NVIDIA-NeMo 团队维护，README 中明确标注目前处于 pre-alpha 阶段，暂不建议用于生产环境。

适合正在评估多模型、多供应商方案，希望在不改动客户端代码的前提下做成本和性能对比的团队。

🔗 项目地址：https://github.com/NVIDIA-NeMo/Switchyard

---

## 3. holaOS — 把多个智能体放进同一个工作空间

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 6.7k | 241 | TypeScript | Apache-2.0（附加条款） |

holaOS 想解决的是智能体工具链碎片化的问题：开发者常常要在 Claude Code、Codex 等不同智能体之间切换，每切换一次就要重新搭建上下文。holaOS 提供一个桌面工作空间，让这些智能体共享同一套记忆和工具集成。

记忆以本地纯文本文件存储，可跨会话、跨智能体读取；README 中提到已接入 100 多个第三方服务（Gmail、Notion、Slack、GitHub 等）的一键 OAuth 授权，并支持 Model Context Protocol（MCP）扩展工具能力。内置模型包括 Kimi K3、GLM 5.2、GPT 5.6、Claude Opus 5 等，也支持自带 API Key 接入 OpenAI、Anthropic 的模型。

适合日常需要在多个智能体之间切换、又想保留统一上下文和工具授权的开发者试用，目前主要面向 macOS、Windows、Linux 桌面场景。

🔗 项目地址：https://github.com/holaboss-ai/holaOS

---

## 今日观察

今天的三个项目恰好对应大模型应用链条的三个环节：Unsloth 负责训练与本地部署，Switchyard 处理多模型路由，holaOS 面向终端用户提供智能体工作空间。三者都不是全新项目，但都在过去 24 小时内新增了数百 star，说明"训练—路由—使用"这条链路上，每一层仍在持续迭代。

---

**Tags**：#GitHub热点 #AI开源 #LLM微调 #模型路由 #智能体工作空间
