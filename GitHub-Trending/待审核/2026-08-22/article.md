<!--
标题候选：
1. 今日 GitHub AI 热点：Agent 基础设施同台亮相
2. ruflo 登顶今日 AI 相关 Trending，另两个项目同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时新增合计超 290 star
当前正在使用：候选 1
-->

# 今日 GitHub AI 热点：Agent 基础设施同台亮相

> 今天的 GitHub Trending 日榜上，三个 AI 相关项目分别代表 Agent 生态的三种路径：面向协作的运行时框架、Apache 旗下的本地优先工作台，以及维护多年的跨平台推理引擎。三者定位不同，但都指向同一个问题——如何让模型真正落地成可用的系统。

---

## 1. ruflo — 让 Claude Code 具备多 Agent 协作能力的运行时

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 68.7k | 140 | TypeScript | MIT |

ruflo 想解决的问题很具体：Claude Code、Codex 这类编码 Agent 只有模型，却缺少统一的执行基础设施。项目把这一层定位为"Harness"，负责工具调用、记忆和任务路由，执行 `npx ruflo init` 即可接入，不需要改变原有的使用习惯。

项目内置 98 个专用 Agent、30 个技能模块和一个 MCP Server，并提供 35 个插件覆盖编排、记忆检索、安全扫描等场景。作者公开的基准测试显示，向量记忆检索在 5 千条数据规模下比暴力搜索快 3.2 至 4.7 倍，recall@10 维持在 0.99；任务路由准确率为 89%。

适合已经在用 Claude Code 或 Codex、想把单次对话升级成多 Agent 协作流程的开发团队参考。

🔗 项目地址：https://github.com/ruvnet/ruflo

---

## 2. Maka — Apache 基金会旗下的本地优先 Agent 工作台

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 2.1k | 148 | TypeScript | Apache-2.0 |

Maka 解决的是"Agent 执行过程不可回溯"的问题。项目把每一次模型消息、工具调用和结果都写入一份可恢复的运行时事件日志（Runtime Event Log），会话、界面和上下文全部从这份日志派生，而不是临时状态。

和多数托管优先的 Agent 产品不同，Maka 坚持本地优先：会话、配置和执行记录默认留在本机，可以自由切换云端 API、本地模型或兼容网关。它内置 Read、Write、Edit、Bash、Glob、Grep 等本地工具，并用权限策略控制每一次操作。项目挂在 Apache 这个 GitHub 组织下，是少见的由基金会背书的 Agent 工作台。

适合注重数据本地留存、需要审计 Agent 执行过程的开发者或团队试用。

🔗 项目地址：https://github.com/apache/maka

---

## 3. ONNX Runtime — 跨平台的机器学习推理与训练加速器

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 21.5k | 5 | C++ | MIT |

ONNX Runtime 要解决的问题是模型"训练一次，哪里都能跑"。它同时支持 PyTorch、TensorFlow/Keras 等深度学习框架，以及 scikit-learn、LightGBM、XGBoost 等传统机器学习库导出的模型，在不同硬件和操作系统上提供统一的推理入口。

除了推理，项目的训练组件专门针对多节点 NVIDIA GPU 上的 Transformer 模型训练做了加速，官方文档介绍只需要在现有 PyTorch 训练脚本中加入一行代码即可接入。项目由微软长期维护，在 ONNX 生态里已有规模，被多个团队用作生产环境的推理实现。

适合需要跨框架部署模型、且已经有一定生产环境经验的机器学习工程团队。

🔗 项目地址：https://github.com/microsoft/onnxruntime

---

## 今日观察

今天入选的三个项目分别对应 Agent 基础设施的两端：面向协作的运行时框架、注重本地留存的工作台，以及支撑 ONNX 生态多年的推理引擎。围绕大模型的工程重心，正从模型本身扩展到执行与可回溯性这类基础能力。

---

**Tags**：#GitHub热点 #AI开源 #Agent工程 #本地优先 #模型推理
