<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub 热点：AI 编程工具与设计系统同上榜
2. graphify 登顶今日 Trending，PyTorch 与 astryx 同样值得关注
3. 今日 GitHub 热点：3 个项目 24 小时合计新增超 2,100 star
当前使用：候选 1
-->

# 今日 GitHub 热点：AI 编程工具与设计系统同上榜

> 今天的 GitHub Trending 日榜里，AI 原生的开发工具仍是主力，同时一个来自 Meta 的开源设计系统也挤进了前列。下面这三个项目分别代表"给 AI 用的代码知识图谱""深度学习训练底座"和"人与 AI 共用的设计系统"三个方向。

---

## 1. graphify — 把整个项目变成可查询知识图谱的编程助手技能

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 75.2k | 937 | Python | MIT |

graphify 解决的问题很具体：在 Claude Code、Cursor、Codex、Gemini CLI 等 AI 编程工具里输入 `/graphify`，它会把整个项目——源码、SQL schema、文档、PDF，甚至图片和视频——解析成一张可查询的知识图谱。开发者不再靠满仓库 grep 去找调用关系，而是直接向图谱提问。

技术上，它用 tree-sitter 解析代码结构，再用 Leiden 社区划分算法把节点聚成模块，走的是 GraphRAG 的思路。产出三个文件：可在浏览器里点选筛选的 `graph.html`、给人读的 `GRAPH_REPORT.md`，以及供程序查询的 `graph.json`，也支持推送到 Neo4j 或 FalkorDB。

它适合中大型代码库、需要让 AI 助手快速建立全局理解的团队。项目当前 75.2k star、24 小时新增约 937，在 AI 编程工具圈里已有影响力。

🔗 项目地址：https://github.com/safishamsi/graphify

---

## 2. PyTorch — 深度学习的主流训练框架

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 101k | 290 | Python | BSD-3-Clause |

PyTorch 是目前使用最广的深度学习框架之一，核心是张量运算和动态计算图，配合 autograd 自动求导与 GPU 加速，让研究者用接近写普通 Python 的方式定义和训练神经网络。今天它以 101k 总 star、24 小时新增 290 的成绩继续留在榜上。

与静态图框架相比，PyTorch 的动态图在调试和写研究代码时更直观；近年也补上了 `torch.compile` 这类面向部署的编译优化。它背后是一个庞大生态，视觉、文本、语音等方向的主流库大多构建在它之上。

对做模型训练、微调，或想理解现代 AI 底层机制的人来说，它基本是绕不开的一环。

🔗 项目地址：https://github.com/pytorch/pytorch

---

## 3. astryx — Meta 开源的、面向人与 AI 协作的设计系统

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 6.3k | 943 | TypeScript | MIT |

astryx 是 Meta 开源的设计系统。官方介绍它在 Meta 内部沉淀了约八年、是公司内使用最广的设计系统，曾支撑一万三千多个应用。它基于 React 和 StyleX，提供 150 多个无障碍组件、品牌级主题定制、暗色模式和配套 CLI。

和不少设计系统不同的一点是，astryx 把 API、文档和 CLI 按同一套规范来设计，目标是让开发者和 AI 助手用同样的方式调用组件——这也是它"agent ready"说法的由来。样式用 StyleX 编写，但对使用者透明，仍可用 Tailwind、CSS Module 或原生 CSS 覆盖。

项目目前处于 Beta（最新版本 v0.1.3），24 小时新增约 943 star，适合关注前端设计系统或 AI 辅助开发的团队参考。

🔗 项目地址：https://github.com/facebook/astryx

---

## 今日观察

今天上榜的三个项目里，两个直接服务 AI 编程（graphify、PyTorch），一个是把"给 AI 用"当成设计目标的前端系统（astryx）。"agent ready""让人和 AI 共用一套工具"正在从口号变成具体的工程约束，是值得留意的一个方向。

---

**Tags**：#GitHub热点 #AI开源 #知识图谱 #PyTorch #设计系统
