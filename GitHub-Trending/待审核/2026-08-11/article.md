<!--
标题候选：
1. 今日GitHub AI热点：从智能体管理到天气预测模型同台
2. paperclip领衔今日GitHub AI三项目，另两个同样值得关注
3. 今日GitHub AI热点：三项目24小时新增均超190 star
当前正在使用：候选 1
-->

# 今日GitHub AI热点：从智能体管理到天气预测模型同台

> 今天的 GitHub Trending 日榜里，AI 相关项目集中在三个不同层面：一个是给多智能体团队做管理后台的编排工具，一个是把 AI 使用习惯沉淀为个人系统的开源框架，还有一个是 Google DeepMind 开源的天气预测模型。三者分别对应"管智能体""用 AI"和"AI 做科研"三种不同场景。

---

## 1. paperclip — 管理一群 AI 智能体干活的调度后台

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 76.6k | 198 | TypeScript | MIT |

paperclip 解决的问题很具体：当一个人同时开着多个 Claude Code、Codex、Cursor 终端跑不同任务时，很容易丢失谁在干什么、花了多少钱。paperclip 用一个 Node.js 服务加 React 面板，把这些智能体统一接进一个仪表盘，可以设定目标、分配任务、查看审批记录和成本。

它的定位不是再造一个智能体，而是给已有智能体搭一层组织架构：README 里用"公司"打比方，把每个智能体当作可雇佣、可分工、可考核的员工，提供任务审批、权限边界、技能训练和跨模型运行时四块能力，支持接入 OpenClaw、Claude Code、Codex、Cursor 等多种智能体。项目目前 76.6k star，24 小时新增 198。

适合需要同时管理多条智能体工作流、并且在意成本与审计追踪的团队和个人开发者。

🔗 项目地址：https://github.com/paperclipai/paperclip

---

## 2. LifeOS — 把个人目标和上下文喂给 AI 的操作系统

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 18k | 315 | TypeScript | MIT |

LifeOS 想解决的是"每次和 AI 对话都要重新解释自己"的问题。它把用户是谁、在乎什么、想去哪里这些信息结构化保存下来,再配合已有的 AI 编程工具(项目基于 Claude Code 构建和运行)使用,让后续的每一次任务都能带着这些上下文去执行。

和直接调用一个 AI 助手不同，LifeOS 本身不提供模型能力，而是在已有的 AI 编程工具（Claude Code、Cursor、Codex 等）之上加一层记忆与技能系统：持久记忆、自定义技能库、意图路由，以及根据使用反馈自我调整的机制。安装方式也比较特殊，是把一条指令交给 AI 编码工具，由 AI 自己读取安装页面并完成配置。

适合已经在日常使用 AI 编码工具、想把零散的目标和习惯沉淀成可复用系统的个人用户。

🔗 项目地址：https://github.com/danielmiessler/LifeOS

---

## 3. WeatherNext — Google DeepMind 开源的天气预测模型

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 7.4k | 325 | Python | Apache-2.0 |

WeatherNext 是 Google DeepMind 与 Google Research 联合开发的全球中期天气与气旋预测模型仓库，最新版本是 WeatherNext 2（WN2），此前的 GraphCast、GenCast 两代模型代码也一并收录在这个仓库中。

技术路线上，WN2 沿用了图神经网络（GraphCast 一代确立的路径）和扩散式集合预报（GenCast 一代确立的路径），仓库里公开了在 ECMWF HRES 数据上微调的 0.25° 分辨率权重文件，也提供了更轻量、适合单张 GPU 或 TPU 跑的 Mini 版本。README 提到 WeatherNext Cyclones 模型在 2025 年大西洋飓风季实际参与了业务化运行。预测结果同时开放在 Google Cloud、WeatherLab、OpenMeteo 等多个平台供直接调用。

适合气象、地球科学领域的研究者，以及想直接调用预测数据而非自己训练模型的开发者。

🔗 项目地址：https://github.com/google-deepmind/weathernext

---

## 今日观察

今天上榜的三个项目分别处于智能体协作、个人 AI 系统和科学计算三条不同的赛道，没有明显的共同主线——某种程度上说明 AI 相关的开源热度已经从单一的"聊天机器人/编程助手"扩散到了更具体的垂直场景。

---

**Tags**：#GitHub热点 #AI开源 #智能体编排 #AI个人助理 #天气预测模型
