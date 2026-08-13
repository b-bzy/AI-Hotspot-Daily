<!--
标题候选：
1. 今日 GitHub AI 热点：RAG 引擎与 Agent 框架各自往前走了一步
2. RAGFlow 登顶今日 AI 热榜，另两个项目分别瞄准 JVM Agent 与端侧模型
3. 今日 GitHub AI 热点：3 个项目 24 小时新增近 500 star
当前正在使用：候选 1
-->

# 今日 GitHub AI 热点：RAG 引擎与 Agent 框架各自往前走了一步

> 今天的 GitHub AI 热榜里，三个项目分别落在检索增强生成、Agent 框架和端侧小模型三个不同方向。它们解决的是同一件事的三个环节：把外部知识接进大模型、让 Agent 具备规划能力、把模型本身做小做省。

---

## 1. RAGFlow — 把检索增强生成和 Agent 编排打包成一套现成流程

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 87.6k | 139 | Go | Apache-2.0 |

做检索增强生成（RAG）的团队，通常要自己在"如何把杂乱文档变成可用知识"和"怎么把检索结果精确喂给大模型"之间写大量胶水代码。RAGFlow 提供的是一条从文档解析、分块、检索到 Agent 编排的完整流程，覆盖 Word、Excel、PDF、扫描件等异构数据源。

它把"上下文引擎"和预置 Agent 模板做成默认能力，而不是留给开发者自己拼装：模板化分块、多路召回配合重排序、以及可视化的分块结果，方便追溯引用来源。项目累计 8,000 余次提交，README 提供中、日、韩、法、俄等十种语言版本，社区维护活跃。

适合需要把内部文档接入大模型问答、且对答案可追溯性有要求的团队。

🔗 项目地址：https://github.com/infiniflow/ragflow

---

## 2. Embabel Agent — 给 JVM/Spring 技术栈做的带规划能力的 Agent 框架

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 4.2k | 40 | Kotlin | Apache-2.0 |

多数 Agent 框架要么是有限状态机，要么是写死的顺序执行链，遇到没预设过的任务组合就无法应对。Embabel 想解决的是让 Agent 在执行过程中动态规划路径，而不是按固定流程走。

它引入了游戏 AI 里常见的目标导向行动规划（GOAP）算法作为默认规划器，同时支持 Utility AI 用于开放式探索任务；每执行一步都会重新评估条件并重新规划，类似 OODA 循环。框架基于 Spring，用 Kotlin 编写但对 Java 同样友好，可以直接复用企业已有的依赖注入和事务管理能力。

适合已经跑在 JVM/Spring 技术栈上、想把 Agent 能力嵌进现有企业系统的团队。

🔗 项目地址：https://github.com/embabel/embabel-agent

---

## 3. Needle 2 — 装进手机和机器人的 14MB 工具调用模型

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 4.3k | 315 | Python | MIT |

工具调用（tool calling）类任务通常依赖云端大模型。Needle 2 想把这类能力压缩到能装进手机、手表甚至机器人里的体积：一个 45M 参数、14MB 的二进制文件，运行一次会话只占用约 28MB 内存。

它基于团队自研的 Simple Attention Network 架构——用 Hadamard MLP 替代前馈层、结合 GQA 注意力和键值记忆，并把权重压缩到 2-bit。README 给出的基准对比显示，在与 FunctionGemma 270M、LFM2.5 230M 等同类小模型的测试中战绩相当，体积却小 5 到 70 倍。

适合做离线设备端工具调用、结构化信息抽取的开发者，`pip install cactus-needle` 即可接入。

🔗 项目地址：https://github.com/cactus-compute/needle

---

## 今日观察

今天入选的三个项目分别代表 AI 应用落地的三个环节：RAGFlow 负责把外部知识接进大模型，Embabel Agent 负责让 Agent 具备动态规划能力，Needle 2 负责把模型本身做小做省、塞进终端设备。三者技术栈完全不同（Go、Kotlin、Python），但都在往"让 AI 系统更好用"这同一个目标上推进。

---

**Tags**：#GitHub热点 #AI开源 #RAG #Agent框架 #端侧模型
