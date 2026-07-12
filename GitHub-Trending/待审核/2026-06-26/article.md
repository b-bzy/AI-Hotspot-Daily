<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub Trending：文档解析与浏览器 Agent 成关注点
2. MinerU 登上今日 Trending，另两个 AI 项目同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时新增超 1100 star
当前使用：候选 1
-->

# 今日 GitHub AI 热点：3 个值得关注的开源项目

> 今天的 GitHub Trending 日榜上，AI 相关项目集中在"把大模型接进具体工程环节"这个方向。下面三个项目分别覆盖文档数据处理、网页端 agent 和垂直领域投研，形态差异较大，适合一起看。

---

## 1. MinerU — 把 PDF、Office 文档转成 LLM 可用的结构化数据

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 69.7k | 644 | Python | Apache-2.0（附商用条款） |

MinerU 解决的问题是把 PDF、图片、DOCX、PPTX、XLSX 这类排版复杂的文档，转成 Markdown 和 JSON 这类机器可读的格式，供后续的检索、抽取和大模型处理使用。它最早诞生于 InternLM 的预训练过程，最初是为了处理科学文献里的符号转换问题。

和普通 OCR 工具相比，MinerU 采用 VLM 与 OCR 双引擎，会自动去掉页眉、页脚、页码这些干扰信息，按人类阅读顺序输出正文，并保留标题、段落、列表的结构。文档里的公式会转成 LaTeX，表格转成 HTML，OCR 支持 109 种语言的检测与识别。工程上它内置了 CLI、FastAPI 和 Gradio WebUI，可在纯 CPU 环境运行，也支持 GPU/MPS 加速，并提供 MCP Server 以及对 LangChain、Dify、FastGPT 的接入。

这是一个 50k+ star 的明星项目，已有 5.8k fork，并发布过三份 arXiv 技术报告。适合做 RAG 知识库、文档数据清洗、以及需要把大量 PDF 喂给大模型的团队参考。

🔗 项目地址：https://github.com/opendatalab/MinerU

---

## 2. page-agent — 运行在网页里的 GUI agent

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 19.9k | 163 | TypeScript | MIT |

page-agent 来自阿里巴巴，2025 年 9 月开源，解决的是用自然语言控制网页界面的问题。它把自己定位为"住在你网页里的 GUI Agent"——开发者不需要安装浏览器扩展、不需要 Python、也不需要 headless 浏览器，一段页面内的 JavaScript 就能跑起来。

技术路线上，它走的是基于文本的 DOM 操作，而不是截图加多模态模型。这意味着不需要调用多模态 LLM、也不需要额外权限，所用模型由使用方自带（README 给出的示例是 qwen3.5-plus）。它另外提供一个可选的 Chrome 扩展用于跨标签页任务，以及一个处于 Beta 的 MCP Server，让外部 agent 客户端来控制浏览器。

README 列出的场景包括：给 SaaS 产品快速加一个 AI copilot、把 ERP/CRM/后台系统里的多步表单填写简化成一句话，以及通过自然语言提升网页的可访问性。项目当前 npm 版本为 1.10.0，已有一定规模的关注度。

🔗 项目地址：https://github.com/alibaba/page-agent

---

## 3. ai-berkshire — 基于 Claude Code 的价值投资研究框架

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 2.1k | 309 | Python | MIT |

ai-berkshire 是一套基于 Claude Code 的投资研究 Skill 合集，2026 年 4 月开源，目前处于早期阶段。它把巴菲特、芒格、段永平、李录四位投资人的方法论结构化，试图用多个 AI Agent 协作完成一份投研报告，而不是让人直接去问大模型。

它和"直接问 AI"的差异在于流程约束：强制输出"通过 / 不通过 / 灰色地带"的结论并附带价格区间；用四位投资人的视角做对抗式分析；内置信息丰富度评级、逆向检验、快速否决清单等反偏见机制；金融计算用 Python 的 decimal.Decimal 做精确十进制，并要求关键数据至少两个来源交叉验证。它的 /investment-team 命令会并行启动四个 Agent 各自研究同一家公司，再由 Team Lead 汇总。

需要说明的是，项目在 README 里附了一份实盘业绩自述（2024 年 +69.29%、2025 年至今 +66.38%，截图称来自券商账户），并注明历史收益不代表未来表现。这些数据来自作者本人披露，未经独立核验，看的时候保留一份审慎即可。项目适合对 AI 辅助投研、多 Agent 工作流感兴趣的人参考。

🔗 项目地址：https://github.com/xbtlin/ai-berkshire

---

## 今日观察

今天这三个项目方向各异：MinerU 偏底层的文档数据基建，page-agent 把 agent 能力做进网页前端，ai-berkshire 是 agent 在投研这个垂直领域的落地尝试。共同点是都把大模型当成一个组件，去解决某个具体环节的工程问题，而不是停留在通用对话。

---

**Tags**：#GitHub热点 #AI开源 #文档解析 #AIAgent #ClaudeCode
