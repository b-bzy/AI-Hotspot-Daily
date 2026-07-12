<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub AI 项目：搜索、检索、选型，工具层占据日榜
2. last30days-skill 登顶今日 Trending，另两个项目同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时合计新增超 5.6k star
当前使用：候选 1
-->

# 今日 GitHub AI 项目：搜索、检索、选型，工具层占据日榜

> 今天的日榜前列被"工具层"项目占据：社交信息检索、向量索引、本地模型选型各占一席。三个项目都不做模型本身，而是各自解决 AI 落地链路上的一段具体工程问题。

---

## 1. last30days-skill — 让 AI agent 检索全网近 30 天真实热度的研究 skill

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 37.6k | 3,191 | Python | MIT |

它针对的问题是搜索的数据盲区：Google 按编辑权重聚合网页，各家 AI 助手又各有围墙——ChatGPT 接了 Reddit 但搜不了 X，Gemini 有 YouTube 没有 Reddit。last30days-skill 的做法是让用户自带各平台的 API key 和浏览器会话，由 agent 并行检索 Reddit、X、YouTube、Hacker News、Polymarket 等来源，按点赞、转发和预测市场的真金白银赔率打分，最后合成一份带依据的摘要。

分发方式是它的另一个差异点：以 Claude Code 插件和 Agent Skills 标准格式发布，一条 `npx skills add` 可以装进 Codex、Cursor、Copilot 等 50 多个 agent 宿主。零配置状态下 Reddit、HN、Polymarket、GitHub 即开即用，其余平台跑一次设置向导接入。

项目创建于 2026 年 1 月，目前 37.6k star，24 小时新增 3,191，居日榜第一。适合做内容选题、市场调研、趋势跟踪的用户。

🔗 项目地址：https://github.com/mvanhorn/last30days-skill

---

## 2. turbovec — 基于 TurboQuant 量化算法的 Rust 向量索引

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 10.3k | 1,801 | Python | MIT |

turbovec 解决的是向量检索的内存账：按 README 的数据，1,000 万文档的 float32 向量要占 31 GB 内存，turbovec 把它压到 4 GB，检索速度还高于 FAISS。底层是 Google Research 今年发表的 TurboQuant 量化算法（arXiv:2504.19874），特点是不依赖数据分布、无需码本训练，向量写入即完成索引，语料增长也不用重建。

工程上它用 Rust 实现并提供 Python 绑定，手写了 NEON（ARM）和 AVX-512BW（x86）两套内核，在 ARM 上对比 FAISS IndexPQFastScan 快 12–20%。搜索时可直接传入 id 允许列表做过滤，不需要过量召回。

3 月底开源，刚过 10k star，24 小时新增 1,801。适合在内存受限或数据不能出本机的环境里搭 RAG 检索层的团队。

🔗 项目地址：https://github.com/RyanCodrai/turbovec

---

## 3. whichllm — 按硬件和实测 benchmark 推荐本地 LLM 的命令行工具

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 4.2k | 633 | Python | MIT |

它回答的问题是"我这台机器到底该跑哪个本地模型"。常见做法是按显存算哪个模型放得下，但放得下不等于最值得跑。whichllm 自动检测本机 GPU、CPU 和内存，从 HuggingFace 拉取实时数据，按带时效权重的 benchmark 得分排序而不是按参数量。README 给的例子：RTX 4090 上 32B 模型放得下，它仍把新一代的 27B 排在第一，因为实测得分更高。

除了本机推荐，它还能用 `--gpu "RTX 4090"` 模拟一块没买的显卡、对比多个升级候选，以及反查"跑 Llama 3 70B 需要什么卡"。`uvx whichllm@latest` 一条命令即可运行，无需安装。

项目创建于 2026 年 3 月，4.2k star，已有一定关注度。适合想在自己硬件上跑本地模型、又不想逐个试错的开发者。

🔗 项目地址：https://github.com/Andyyyy64/whichllm

---

## 今日观察

三个项目方向各异，但有一个共同点：都不碰模型训练，而是把 AI 工作流里某个具体环节的工程做细——信息怎么搜、向量怎么省内存、模型怎么选。工具层项目持续吃下日榜头部位置，是近期 Trending 的一个稳定模式。

---

**Tags**：#GitHub热点 #AI开源 #向量检索 #本地LLM #AIAgent
