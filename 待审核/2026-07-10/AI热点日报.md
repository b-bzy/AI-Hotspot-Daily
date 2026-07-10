# AI 热点日报 · 2026-07-10（前 24h，共 161 条原始条目，14/14 源正常）

> 整理说明：本日报基于首跑的 161 条整理；剔除关键词误入的非 AI 条目 4 条（HN 医疗吐槽帖、SpaceX 员工造富、私人飞机行业、航空创业大赛）。首跑后脚本修复了 HN 全文误命中和 HF 论文跨天重复问题并重抓，当前 items.json 为修复后的 136 条干净版（HF 论文收敛为最新一批 4 篇——本日报的 26 篇论文列表来自首跑快照，仍然有效）。微博热搜今日无 AI 条目（台风/社会新闻刷屏），属正常情况非源故障。

## 🔥 今日焦点

- **【4源同报】OpenAI 发布 GPT-5.6，同步推出办公 Agent「ChatGPT Work」** — GPT-5.6 即日全量上线 ChatGPT/Codex/API，三档定价：Sol $5/$30、Terra $2.5/$15、Luna $1/$6（每百万 token 输入/输出）；ChatGPT Work 是基于 Codex + GPT-5.6 的跨应用办公 agent，可连续工作数小时，Pro/企业/教育版先行；Codex 与 ChatGPT 桌面端合并为新 App，独立浏览器 ChatGPT Atlas 同日停服 | HN 头条 718分/511评论 + Techmeme 7 条头条 + @sama/@OpenAI 十余条推文 + 掘金热榜
  [HN](https://openai.com/index/gpt-5-6/) [Techmeme](https://www.techmeme.com/260709/p27#a260709p27) [定价](https://www.techmeme.com/260709/p28#a260709p28) [sama推文](https://zpravobot.news/@sama/116891141627278381)
- **【smol.ai 头条】xAI 发布 Grok 4.5：与 Cursor 合训的 coding/agents 模型** — 官方定位"Opus 级但更快、更省 token、更便宜"，是 xAI 首个专为编程和智能体训练的模型；Cursor 称其"我们最强模型"，首周双倍用量；马斯克称上下文窗口下周从 500k 回到 1M；OpenRouter/Hermes Agent 等 day-0 支持 | smol.ai 每日综述头条（前一天 X 圈最大事件）
  [smol.ai](https://news.smol.ai/issues/26-07-08-grok-45/)
- **【2源同报】智谱 GLM-5.2 开源发布即冲榜** — HuggingFace 趋势榜第 3（趋势分 364、3718 赞）；HN 上"GLM 5.2 记账准确率接近人类会计"实测帖 105 分/55 评论，社区对其性价比讨论热烈 | HF trending + HN
  [HF](https://huggingface.co/zai-org/GLM-5.2) [HN实测帖](https://toot-books.pages.dev/blog/glm-5-2-vat-benchmark)
- **【2源·中英同热】Meta 开放模型 API，发布 Muse Spark 1.1** — Meta 正式加入模型商业化竞争：Muse Spark 1.1 定价 $1.25/$4.25（每百万 token），Zuckerberg 称定价"约为 OpenAI/Anthropic 的 25%"；Alexandr Wang 称重点优化编程与 agentic 能力 | Techmeme 2 条 + IT之家
  [Techmeme](https://www.techmeme.com/260709/p21#a260709p21) [IT之家](https://www.ithome.com/0/974/775.htm)
- **【2源同报】Meta 自研 AI 芯片 Iris 最早 9 月量产** — 路透获取的内部备忘录：明年整体算力翻倍至 14GW；已与三星（内存）、闪迪（闪存）、住友电工（光纤）签长期供应协议 | IT之家 + 36氪
  [IT之家](https://www.ithome.com/0/974/723.htm) [36氪](https://36kr.com/newsflashes/3888342478748160?f=rss)

## 🚀 模型与产品发布

- **蚂蚁灵波开源 LingBot-World 2.0：世界模型首次"小时级"生成【2源同报】** — 支持 AI 原生多人交互、无界交互时长；HF Daily Papers 同步上榜（21 赞） | [量子位](https://www.qbitai.com/2026/07/446548.html) [HF论文](https://huggingface.co/papers/2607.07534)
- **蚂蚁灵波开源 LingBot-Video：全球首个面向具身的视频基模** | [量子位](https://www.qbitai.com/2026/07/446458.html)
- **原力灵机 DM0.5 发布：Zero-Shot 提升 31%，15 万小时数据训练**，称"已出现泛化涌现" | [量子位](https://www.qbitai.com/2026/07/447508.html)
- **AlphaEvolve 在 Google Cloud 正式 GA** — DeepMind 与 Google Cloud 合作的 Gemini 驱动进化式算法设计 agent | [@googledeepmind](https://zpravobot.news/@GoogleDeepMind/116891016077037833)
- **Character.AI 上线三部真人编剧 + AI 生成的微短剧**，角色可对话，未来开放用户自制 | [Techmeme](https://www.techmeme.com/260709/p23#a260709p23)

## 🏢 公司与行业动态

- **PitchBook：2026 上半年美国 VC 融资 $412.7B，AI 占 86%（$355.9B）**，超 2025 全年 30%，Q2 有 7 笔 $1B+ 轮次 | [Techmeme](https://www.techmeme.com/260709/p34#a260709p34)
- **Anthropic 宣布 7 月 12 日起 Fable 5 改按量计费**，称"容量充足时"将回归订阅套餐 | [Techmeme](https://www.techmeme.com/260709/p33#a260709p33)
- **Bun 作者用 Claude Fable 5 预发布版 11 天把 Bun 从 Zig 重写成 Rust**，称三名工程师"约需一年" | [Techmeme](https://www.techmeme.com/260709/p24#a260709p24)
- **NYT 诉讼文件：OpenAI 被指假装无法检索训练数据、隐藏数十亿条日志** | 26分 [HN](https://arstechnica.com/tech-policy/2026/07/openai-faked-inability-to-search-training-data-hid-billions-of-logs-nyt-says/)
- **OpenAI 首席未来学家离职**，曾被马斯克公开嘲讽，去向 "To safe AGI" | [量子位](https://www.qbitai.com/2026/07/446658.html)
- **AI 外包市场 Mercor 洽谈新融资，估值约 $20B**——不到一年前估值还是 $10B | [Techmeme](https://www.techmeme.com/260709/p30#a260709p30)
- **微软总裁 Brad Smith：美国现状是"没有透明完整规则的 AI 监管"**，"没有规则企业无法规划" | [Techmeme](https://www.techmeme.com/260709/p26#a260709p26)
- **Anthropic 长期利益信托（LTBT）任命前美联储主席伯南克为新成员** | [@AnthropicAI](https://zpravobot.news/@AnthropicAI/116891000696749220)
- **Anthropic 与 AE Studio 合作发布 off-switch 双用途研究** | [@AnthropicAI](https://zpravobot.news/@AnthropicAI/116887067829201224)
- **李开复回应"没了李开复，零一万物还有什么"** | [量子位](https://www.qbitai.com/2026/07/446778.html)
- **特斯拉三代擎天柱初步定型**：晚点报道，要求供应商 9 月周产 1000 台、年底 2000–2500 台，马斯克放话达不成就换掉采购团队 | [IT之家](https://www.ithome.com/0/974/782.htm)
- **全球首例：宇树 G1 人形机器人远程操控完成活体动物外科手术**（UCSD，两例胆囊切除） | [IT之家](https://www.ithome.com/0/974/777.htm)
- **星巴克用 AI 自研内部工具，欲替代微软、IBM 采购方案** | [IT之家](https://www.ithome.com/0/974/750.htm)
- 芯片与算力：**法国对英伟达反垄断调查接近尾声【2源】**，聚焦 CUDA 生态，最高可罚全球年营收 10%（[IT之家](https://www.ithome.com/0/974/744.htm)/[36氪](https://36kr.com/newsflashes/3888377221364232?f=rss)）；**AMD 确认 7/22–23 发布 Zen 6**（[IT之家](https://www.ithome.com/0/974/769.htm)）；**三星重返 PC 芯片：4nm AI PC 芯片 Gaia 明年量产**（[IT之家](https://www.ithome.com/0/974/762.htm)）；**美光向美国半导体供应链投资 $3B**（[IT之家](https://www.ithome.com/0/974/743.htm)）；**燧原科技科创板 IPO 获批**（[IT之家](https://www.ithome.com/0/974/719.htm)）；**英伟达 Rubin Ultra 机柜预估 $2100 万/柜**，单柜 HBM4e 成本超 $150 万（[IT之家](https://www.ithome.com/0/974/718.htm)）；**有研硅收购晶隆半导体 60% 股权**（[36氪](https://36kr.com/newsflashes/3888328136047109?f=rss)）
- 国内融资与产业：**Momenta 港股上市首日市值 700 亿港元**，深氪长文剖析（[36氪](https://36kr.com/p/3888180493318921?f=rss)）；**昇视唯盛（焊接具身智能）完成数亿元 B 轮**（[36氪](https://36kr.com/p/3887871679347208?f=rss)）；**深度智控（能源物理 AI）完成数亿元 B 轮**，晶科能源战投（[36氪](https://36kr.com/p/3887726503688968?f=rss)）；**智能体互联网关键系统技术验证工程启动**（信通院，[IT之家](https://www.ithome.com/0/974/706.htm)）；**量化派转型物理 AI**（[量子位](https://www.qbitai.com/2026/07/446435.html)）；**WAIC 2026 定档 7/17–20 上海**，180 家企业参展（[量子位](https://www.qbitai.com/2026/07/436498.html)）；**天立启鸣 AI+教育方案入选联合国 AI for Good**（[量子位](https://www.qbitai.com/2026/07/446562.html)）

## 🔓 开源项目与模型

GitHub Trending（AI 相关 11 项）：
- **MadsLorentzen/ai-job-search** — 基于 Claude Code 的求职框架：评估职位、定制简历、写求职信、模拟面试 | 今日 +3728★ | [GitHub](https://github.com/MadsLorentzen/ai-job-search)
- **addyosmani/agent-skills** — Addy Osmani 出品的生产级 AI 编码 agent 技能库 | +2582★ | [GitHub](https://github.com/addyosmani/agent-skills)
- **iOfficeAI/OfficeCLI** — 首个为 AI agent 打造的 Office 套件：读写 Word/Excel/PPT，单二进制免安装 | +1923★ | [GitHub](https://github.com/iOfficeAI/OfficeCLI)
- **VoltAgent/DESIGN.md 合集** — 知名品牌设计系统的 DESIGN.md 分析集，丢进项目让 agent 生成匹配 UI | +1233★ | [GitHub](https://github.com/sponsors/VoltAgent)
- **asgeirtj/system-prompts** — 提取的各家系统提示词：Claude Fable 5、GPT-5.5、Gemini 3.5 等 | +1135★ | [GitHub](https://github.com/sponsors/asgeirtj)
- **bradautomates/claude-video** — 让 Claude "看视频"：下载、抽帧、转写一条龙 | +727★ | [GitHub](https://github.com/bradautomates/claude-video)
- **vxcontrol/pentagi** — 全自主渗透测试 AI Agent 系统 | +543★ | [GitHub](https://github.com/vxcontrol/pentagi)
- **kyutai-labs/pocket-tts** — CPU 上能跑的口袋级 TTS | +273★ | [GitHub](https://github.com/kyutai-labs/pocket-tts)
- 另有：unclecode/crawl4ai（+195★）、anthropics/claude-cookbooks（+194★）、wonderwhy-er/DesktopCommanderMCP（+185★）

HuggingFace 趋势榜（模型/Space 23 项，前 10）：
- **tencent/Hy3**（趋势分 579）· **empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF**（576，1920 赞）· **zai-org/GLM-5.2**（364，见焦点）· **InternScience/Agents-A1**（242）· **baidu/Unlimited-OCR**（232，模型+Space 双上榜）· **google/tabfm-1.0.0**（表格基础模型，208）· **mistralai/Leanstral-1.5-119B-A6B**（170）· **meituan-longcat/LongCat-2.0**（161）· **deepseek-ai/DeepSeek-V4-Pro-DSpark**（130，投机解码版）· **Space: smolagents/hf-realtime-voice**（实时语音，237）

## 📄 研究论文（HF Daily Papers，26 篇 ≥5 赞）

- **Accurate, Interdisciplinary and Transparent Structure-property Understanding with Deep Native Structural Reasoning** — 结构-性质关系的原生结构推理 | 71赞 | [HF](https://huggingface.co/papers/2607.07708)
- **Hierarchical Sparse Attention Done Right: Toward Infinite Context Modeling** — 分块稀疏注意力做无限上下文 | 53赞 | [HF](https://huggingface.co/papers/2607.02980)
- **Dual Latent Memory in Vision-Language-Action Models** — VLA 模型的双潜在记忆，解长时程操作 | 44赞 | [HF](https://huggingface.co/papers/2607.07608)
- **Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence** — 具身智能的 MoE 视频预训练 | 39赞 | [HF](https://huggingface.co/papers/2607.07675)
- **Gemma 4 Technical Report** — Google 开源多模态新一代，主打计算效率与推理 | 37赞 | [HF](https://huggingface.co/papers/2607.02770)
- **Vision as Unified Multimodal Generation** — 把计算机视觉统一为多模态生成 | 37赞 | [HF](https://huggingface.co/papers/2607.06560)
- **DSpark: Confidence-Scheduled Speculative Decoding** — DeepSeek 投机解码加速（对应上面 V4-Pro-DSpark） | 23赞 | [HF](https://huggingface.co/papers/2607.05147)
- **Infinite Worlds with Versatile Interactions（LingBot-World 2.0）** — 见「模型发布」板块 | 21赞 | [HF](https://huggingface.co/papers/2607.07534)
- **LLM-as-a-Tutor: Policy-Aware Prompt Adaptation for Non-Verifiable RL** | 20赞 | [HF](https://huggingface.co/papers/2607.04412)
- **Parallelized Autoregressive Decoding for Omni-Modal Dense Video Captioning** | 18赞 | [HF](https://huggingface.co/papers/2607.02963)
- 另 16 篇（13–5 赞）：JD Oxygen AIIC V1 · TurnOPD · From Foundation to Application (VLA) · MentalThink · Flex-Forcing · CanvasAgent · PointDiT · CGGS · TREK · RoboDojo · Attending to Multimodal Generation · Rank-Then-Act · Late-Interaction Retrieval Capacity · SWE-Review · PluraMath · 3D HAMSTER —— 全部链接见 items.json

## 💬 KOL 与社区热议

来自 smol.ai 综述（覆盖 12 个 subreddit + 544 个 X 账号）：
- 前一天 X 圈唯一大事就是 **Grok 4.5 发布**（见焦点），其余"a quiet day"；马斯克密集造势："Opus 级但快得多"、对 Tesla/SpaceX 工程师实用性优先于跑分
- **@sama 发布日连环推**：「5.6 直播中：模型之外还有 3 件产品大事——ChatGPT Work（真的很重要）、新桌面 App、托管站点」；「显然是我们做过最好的模型」；「企业最关心 AI 成本，5.6 Sol 在每任务成本上是巨大进步」；「Codex 是 Work 产品的核心，Codex 哪儿也不去」 | [推文串](https://zpravobot.news/@sama)
- **@OpenAI 官方案例营销**：用 GPT-5.6 经营麦片生意的一家人、解开未解数学题的数学家、种西兰花的农民
- HN 高分讨论：
  - **AI 正在改变软件重写的经济学** — 83分/94评论，重写 vs 维护的成本天平被 AI 掀翻 | [HN](https://thetruthasiseeitnow.com/ai-slop-starts-with-the-codebase-itself/)
  - **OpenAI 博客：在编码评测中分离信号与噪声** — 236分/88评论 | [链接](https://openai.com/index/separating-signal-from-noise-coding-evaluations/)
  - **Anthropic 新功能：Reflect with Claude**（回顾你的 Claude 使用方式）— 40分/53评论 | [链接](https://www.anthropic.com/news/reflect-with-claude)
  - **Launch HN: Context.dev (YC S26)** — 任意网站转结构化数据 API，53分 | [链接](https://www.context.dev)
  - Show HN：Devthropology（GitHub 仓库洞察，26分）· Abralo（单窗口跑多个 Claude Code agent，15分）· Mozilla AI「下一个时代是基础设施而非模型」（12分）

## 🇨🇳 中文圈热点

- **英伟达市值不到两个月蒸发 $1 万亿，估值回落到 AI 热潮前水平** — 知乎热榜 #19（70 万热度），投资者转投存储等其他半导体 | [知乎](https://www.zhihu.com/question/2058280043265143682)
- **「当我试图驯服 AI 做短剧（4）」** — B站排行榜，220 万播放，AI 内容创作系列 | [B站](https://www.bilibili.com/video/BV1UaM46yESn)
- **微博热搜**：今日无 AI 条目（台风巴威、晋江火灾等社会新闻刷屏）
- 掘金 AI 热榜（开发者在聊什么，前 10/20 条）：
  - **别被模型宣传骗了，真实 Agent 任务一跑就知道**（15827 阅读）| [掘金](https://juejin.cn/post/7658119907389554738)
  - **凌晨睡不着，我给台风巴威写了个追踪网站**（5507，vibe coding 实录）| [掘金](https://juejin.cn/post/7659393583027896330)
  - **我筛了 1400 个 Claude Code Skills，留下 5 个天天在用的**（4311）| [掘金](https://juejin.cn/post/7657936630132883492)
  - **豆包和千问同时关了智能体，我搭的 3 个自动化全废了——迁移方案**（2116）| [掘金](https://juejin.cn/post/7658599462051086371)
  - **GPT5.6 今晚全量开发？Codex 上线史上最强 Coding 模型**（2079）| [掘金](https://juejin.cn/post/7659585088225624079)
  - **人均配了 AI，为什么公司还是没变快？本质是分布式系统问题**（1808）| [掘金](https://juejin.cn/post/7657956930892136475)
  - **IDEA 爽用 Claude Code 的终极方案**（1432）· **100+ 简历优化经验整理成 Skill**（1162）· **Claude Code 封禁中国用户在代码里下毒？**（874）· **AI 编程时代的 Git worktree**（773）
  - 另 10 条（阅读量 696–205）：三年了 AI 应用为何还没爆发 · 给 AI"写循环" · agent harness 设计 ×3 · Tool Search 按需加载原理 · 无状态 LLM 架构 等，见 items.json

## ⚠️ 本次异常源

全部正常（14/14）。备注：微博 0 条为热搜内容所致非接口故障；smol.ai 首跑时 RSS 含非法控制字符已在脚本层修复。
