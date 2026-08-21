<!--
标题候选：
1. 今日 GitHub AI 项目：AI 基础设施与安全工具成为焦点
2. Modular 平台登顶今日 Trending，另两个 AI 项目同样值得关注
3. 今日 GitHub AI 热点：3 个项目覆盖开发、部署与安全全链路
当前正在使用：候选 1
-->

# 今日 GitHub AI 项目：AI 基础设施与安全工具成为焦点

> 今天的 GitHub Trending 日榜上，AI 相关项目集中在基础设施层：一个统一的 AI 开发与部署平台、一个面向大规模 agent 部署的运行时，以及一个专门给 AI 系统做安全自检的红队平台。三者分别对应 AI 应用从开发、部署到上线审计的不同环节，值得放在一起看。

---

## 1. Modular — 统一的 AI 开发与部署平台

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 28.1k | 268 | Mojo | Apache-2.0 |

Modular 想解决的是 AI 开发链路碎片化的问题：从底层编程语言到模型推理服务，过去分散在不同工具里。这个仓库开源了 Modular Platform 的核心组件，包括自研的 Mojo 编程语言和 MAX 框架，把编译到 GPU 推理的链路整合到一套系统里。

和依赖 PyTorch、ONNX Runtime 的项目不同，Modular 走自建编译器基础设施的路线：Mojo 编译器负责语言层，MAX 加速库负责硬件适配，MAX 推理服务器提供 OpenAI 兼容的 API 端点，接 OpenAI 接口的应用可直接切换到自部署模型。README 未给出具体推理速度或硬件覆盖数据。

适合需要自建模型推理服务、不想被单一硬件厂商绑定的团队参考。

🔗 项目地址：https://github.com/modular/modular

---

## 2. Agent Substrate — 面向大规模 agent 部署的运行时

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 1.4k | 22 | Go | Apache-2.0 |

Agent Substrate 解决的是一个具体问题：agent 类应用大部分时间处于空闲状态，按传统容器或虚拟机一对一分配资源成本很高。项目提供一套运行时，把大量 agent 实例映射到少量常驻 worker 上，实现高密度复用。

核心机制是 suspend/resume：对内存、文件系统和运行状态做完整快照，agent 挂起后可亚秒级恢复，不丢失上下文。隔离层支持 gVisor 和 microVM，项目不绑定具体 agent 框架，可承载基于 LangChain、Claude Code 或 MCP 构建的 agent。官方演示中，250 个有状态 actor 被调度到 8 个 Kubernetes pod 上运行。

适合需要同时运行大量 agent 实例、又想控制基础设施成本的团队参考。

🔗 项目地址：https://github.com/agent-substrate/substrate

---

## 3. AI-Infra-Guard — 腾讯朱雀实验室的 AI 红队安全平台

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 5k | 50 | Python | Apache-2.0 |

AI-Infra-Guard（简称 A.I.G）由腾讯朱雀实验室开源，解决企业部署 AI agent 及相关基础设施后缺乏统一安全自检工具的问题——从底层框架漏洞到 agent 执行环节的权限滥用，此前要分别用不同工具排查。

项目把检测能力拆成五个模块：Agent Scan 评估 Dify、Coze 等平台上的多 agent 工作流风险；Skill Scan 按 SkillTrustBench 分类法检测 AI agent 技能的 9 类风险，官方给出的 F1 分数为 0.9848；MCP Scan 覆盖 MCP Server 的 14 类安全风险；AI Infra Scan 对 Ollama、ComfyUI、vLLM 等 100 多个框架组件做指纹识别，比对超过 2000 个已知 CVE；此外还有 prompt 越狱评估模块。

适合企业安全团队和 AI 基础设施运维人员，在把 agent 或模型服务推上生产环境前做自查。

🔗 项目地址：https://github.com/Tencent/AI-Infra-Guard

---

## 今日观察

今天的三个项目分别落在 AI 应用链路的三个不同环节：Modular 做的是底层编译与推理平台，Agent Substrate 做的是 agent 的运行时基础设施，AI-Infra-Guard 做的是上线前的安全自检。三者没有直接竞争关系，合在一起大致勾勒出"AI agent 从开发到部署再到安全审计"这条链路上，工具链正在变得更专业化的一个侧面。

---

**Tags**：#GitHub热点 #AI开源 #AI基础设施 #Agent运行时 #AI安全
