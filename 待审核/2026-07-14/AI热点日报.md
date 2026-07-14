# AI 热点日报 · 2026-07-14（前 24h，共 157 条，25/25 源正常）

> 说明：本期抓取脚本 08:15 完成（25/25 源，157 条），但云端整理 routine 03:30 首次检查时 fetch 尚未落盘——起因是 GitHub Actions 的 `schedule` 触发被延迟约 3.5 小时（三班次 02:35/02:55/03:15 UTC 全部延迟到 ~06:57 UTC 才提交），routine 按规范等待 1 小时无果后判定「今日跳过」。现已人工补发，并同步修复了触发机制（见文末异常源说明）。

## 🔥 今日焦点

- **【4源同报】GPT-5.6 + Codex 全量上线，国内开发者三种声音开撕** — 掘金三篇独立视角扎堆热榜：兴奋党「Codex上线史上最强Coding模型」、吐槽党「Codex被夺舍了」、冷静党「我可能得泼点冷水」；同日 The Decoder 报道 Anthropic 顺势宣布 Claude Fable 5 免费额度延长至 7/19（原定今日切换按量计费）——巨头「宽限战」剧本继续，这次多了国内开发者一线实测的分裂反应 | [掘金×3](https://juejin.cn/post/7659585088225624079) · [The Decoder](https://the-decoder.com/anthropic-extends-free-fable-5-access-for-subscribers-as-openais-gpt-5-6-sol-heats-up-the-pricing-war/)
- **【3源同报·含跨语言】逐际动力再融 2 亿美元 Pre-IPO，中国人形机器人 IPO 潮提速** — CNBC（经 Techmeme）报道中国 100+ 人形机器人创业公司正扎堆冲 IPO；36氪独家确认逐际动力 LimX Dynamics 完成近 2 亿美元 Pre-IPO 轮（投后估值 150 亿元）；量子位补充「营收对赌不符合具身商业逻辑」的创始人表态 | [Techmeme](https://www.techmeme.com/260713/p36#a260713p36) · [36氪](https://36kr.com/p/3893976502287618) · [量子位](https://www.qbitai.com/2026/07/449474.html)
- **【3源同报】Anthropic 发布 31 万对话规模的 Claude「价值观」研究** — 基于约 31 万条匿名对话，Anthropic 官方（AnthropicAI 推文串）披露 Claude 的价值观表达会因模型和语言显著变化：俄语最强硬、印地语/阿拉伯语最温暖；MIT Technology Review 撰文解读这项研究「说明了什么、又没说明什么」；Techmeme 头条同步 | [Techmeme](https://www.techmeme.com/260713/p34#a260713p34) · [MIT科技评论](https://www.technologyreview.com/2026/07/13/1140343/) · [@AnthropicAI](https://zpravobot.news/@AnthropicAI/116913854711394114)
- **【2源同报】苹果诉 OpenAI 商业机密案，最疯狂指控曝光** — TechCrunch 与 The Verge 同日盘点起诉书里的猎奇细节：从员工爆料 OpenAI 硬件负责人面试时要求候选人带上"未发布的苹果产品部件"，到双方各执一词的技术窃取指控 | [TechCrunch](https://techcrunch.com/2026/07/13/the-wildest-allegations-in-apples-trade-secrets-lawsuit-against-openai/) · [The Verge](https://www.theverge.com/tech/964843/apple-openai-lawsuit-wildest-claims)
- **【2源同报】荣耀阿里将官宣 Agentic OS 终端合作** — IT之家、36氪同步消息源：荣耀将于 7/18 在 WAIC 2026 举办「从数字屏幕到具身智能」分论坛，双方合作方向指向下一代终端操作系统 Agentic OS 落地 | [IT之家](https://www.ithome.com/0/976/367.htm) · [36氪](https://36kr.com/newsflashes/3894943679167744)
- **【2源同报·罗生门】字节跳动被曝入局自动驾驶，官方随即否认** — 36氪独家：字节正探索自动驾驶，项目由 Seed 旗下周畅的世界模型团队负责；同日雷锋网早报援引字节官方回应「没有做智能驾驶业务的计划」——独家爆料与官方否认打起了架 | [36氪](https://36kr.com/p/3893815451417347) · [雷锋网](https://www.leiphone.com/category/zaobao/mXH74oCuoPfxSBho.html)

## 🚀 模型与产品发布

- **阶跃星辰发布全球首个智能体原生操作系统 Step AOS + AI 终端品牌 STEPX**：同场亮相全球首款大模型原生智能体手机 STEPX Neo，打通模型-系统-硬件"模软硬"三位一体闭环 | [雷锋网](https://www.leiphone.com/category/ai/DCPWHecweBJl5y9S.html)
- **【官方】微软研究院**：用 Rust + Lean + Aeneas + AI agent 组合，为生产级密码学库 SymCrypt 做形式化验证扩展 | [微软研究院](https://www.microsoft.com/en-us/research/blog/verifying-rust-cryptography-in-symcrypt-from-standards-to-code/)
- **高德发布通用世界模型工坊 ABot-World Studio**：单张 5090 显卡可生成小时级实时交互式视频与 3D 场景 | [量子位](https://www.qbitai.com/2026/07/449568.html)
- **视频 Agent 新品**：100+ 导演级 Skill 随叫随到，"当大导演"级可用产品首次出现 | [量子位](https://www.qbitai.com/2026/07/449566.html)
- **OpenAI 发布面向普通用户的新版 Prompting 指南**：不再讲复杂公式，改用目标/上下文/格式/约束四个可选模块，核心建议是"别过度设计，先给结果" | [The Decoder](https://the-decoder.com/openais-new-prompting-guide-tells-users-to-stop-overthinking-and-start-with-the-result/)
- **ACRouter**：智能路由挑选每个任务最合适的模型，比纯用 Opus 省 2.6 倍成本 | [VentureBeat](https://venturebeat.com/orchestration/acrouter-picks-the-smartest-ai-model-per-task-beating-opus-only-setups-by-2-6x-on-cost)
- **德国 AI 联盟开源 Soofi S（30B-A3B）**：完全基于德国电信慕尼黑云基础设施训练，英德双语基准双双登顶 | [The Decoder](https://the-decoder.com/german-ai-consortium-releases-soofi-s-an-open-30b-model-that-tops-benchmarks-in-both-english-and-german/)
- 图灵奖得主 Rich Sutton 创立 Oak Lab，做能自主学习的 AI agent，称现有深度学习"弱且低效" | [The Decoder](https://the-decoder.com/turing-award-winner-rich-sutton-founds-oak-lab-to-build-ai-agents-that-learn-on-their-own/)
- Google SensorFM：基于 500 万 Fitbit/Pixel Watch 用户超万亿分钟穿戴数据训练的健康基础模型，35 项基准中 34 项超越现有方案 | [The Decoder](https://the-decoder.com/sensorfm/)
- 两百余位经济学家与 AI 研究者（含 16 位诺奖得主）联合声明：应对 AI 经济冲击的准备窗口正快速关闭 | [The Decoder](https://the-decoder.com/nobel-laureates-and-ai-leaders-warn-the-window-to-prepare-for-ais-economic-impact-is-closing-fast/)
- Nadella 批评 OpenAI/Anthropic 等大厂"反向信息悖论"：一边用公开数据训练自己模型，一边禁止别人蒸馏自家模型 | [The Decoder](https://the-decoder.com/nadella-calls-out-ai-labs-like-openai-and-anthropic-for-banning-distillation-while-training-on-everyone-elses-data/)

## 🏢 公司与行业动态

- **英伟达收紧芯片出口审查**：据 FT，新加坡/马来西亚/日本获授权的 AI 芯片客户被削减 50%+，意在防止芯片"绕道"流入中国 | [Techmeme](https://www.techmeme.com/260714/p1#a260714p1)
- **【2源同报】Nous Research（Hermes 开源 agent，OpenClaw 对手）融资 7500 万美元+**，估值 15 亿美元，Robot Ventures 领投 | [Techmeme](https://www.techmeme.com/260713/p33#a260713p33) · [TechCrunch](https://techcrunch.com/2026/07/13/hermes-agent-maker-nous-research-in-talks-for-new-funding-at-1-5b-valuation/)
- **【2源同报】iOS 27 公测上线，Siri AI 首次公开亮相**，The Verge 实测称"已经在改变我用 iPhone 的方式" | [Techmeme](https://www.techmeme.com/260713/p31#a260713p31) · [The Verge](https://www.theverge.com/tech/964714/siri-ai-public-beta-preview-ios-27-hands-on)
- **【2源同报】Waze 接入 Gemini，新增语音指令与个性化路线功能**（The Verge 称"没那么话痨"）| [TechCrunch](https://techcrunch.com/2026/07/13/waze-adds-new-ai-powered-features-and-customization-updates/) · [The Verge](https://www.theverge.com/transportation/964132/waze-gemini-ai-voice-commands-less-chatty)
- OpenAI 商业化版图"一拆为三"，负责 AGI 部署与应用的掌舵人 Fidji Simo 因慢性病恶化意外卸任全职高管 | [雷锋网](https://www.leiphone.com/category/industrynews/AsJkNmGbxJ5mPq93.html)
- OpenAI 反击马斯克 xAI 窃密官司：要求法官驳回诉讼，令 xAI 承担超百万美元法律费 | [IT之家](https://www.ithome.com/0/976/380.htm)
- Anthropic 开始为印度（美国外最大市场）本地化 Claude 定价，改为印度卢比计价 | [TechCrunch](https://techcrunch.com/2026/07/13/anthropic-starts-localizing-claude-pricing-for-india-its-biggest-market-after-the-us/)
- 视频生成创业公司 PixVerse 融资 4.39 亿美元，估值突破 20 亿美元 | [TechCrunch](https://techcrunch.com/2026/07/13/video-generation-startup-pixverse-raises-439m-valuation-soars-past-2b/)
- 伦敦 Valarian（让企业用美国云但自己掌控数据）获 NEA 领投 5000 万美元 A 轮 | [Techmeme](https://www.techmeme.com/260713/p26#a260713p26)
- 西雅图 Augmodo（AI 智能徽章追踪货架库存）获 2100 万美元融资，估值 3.5 亿美元 | [Techmeme](https://www.techmeme.com/260713/p25#a260713p25)
- 微软警告：AI 正把漏洞从"公开披露"到"被利用"的窗口从数周压缩到数小时，建议 Windows 安全更新延迟别超 3 天 | [IT之家](https://www.ithome.com/0/976/290.htm)
- 三星健康新增条款：拒绝 AI 训练数据授权可能导致无法备份数据 | [IT之家](https://www.ithome.com/0/976/309.htm)
- 汤森路透因加大 AI 应用，对工程部门裁员至多 500 人（约占该部门 5%）| [IT之家](https://www.ithome.com/0/976/364.htm)
- Uber 产品负责人访谈：谈酒店、robotaxi 业务，以及为何不想做"万能超级 App" | [TechCrunch](https://techcrunch.com/2026/07/13/ubers-product-chief-on-hotels-robotaxis-and-why-the-company-doesnt-want-to-be-everything-for-everyone/)
- 已经财务自由的一批科技赢家们又开始"卷"了——不想错过 AI 定义时代的机遇 | [TechCrunch](https://techcrunch.com/2026/07/13/already-rich-already-successful-why-the-last-wave-of-tech-winners-is-grinding-again/)
- Sam Altman 回怼马斯克"骗子"指控，反讽对方在向公开市场投资者兜售"短期太空数据中心" | [TechCrunch](https://techcrunch.com/2026/07/13/sam-altmans-space-data-center-trash-talk-is-what-most-experts-already-believe/)
- 伦理讨论：一个完全"用户对齐"的 AI 世界，是否意味着 AI 该帮你摆脱杀害配偶的指控？| [TechCrunch](https://techcrunch.com/2026/07/13/should-ai-help-you-get-away-with-killing-your-spouse/)
- 英伟达汽车业务负责人 Xinzhou Wu 访谈：自动驾驶芯片、激光雷达在 L4 上的价值等 | [The Verge](https://www.theverge.com/tech/964843/apple-openai-lawsuit-wildest-claims)

## 🔓 开源项目与模型

**GitHub Trending**：HKUDS/Vibe-Trading（今日+1153★，个人交易 agent）· Graphify-Labs/graphify（+1095★，任意文件/代码/文档转可查询知识图谱的 Claude Code/Codex 技能）· Shubhamsaboo/awesome-llm-apps（+996★，100+ AI Agent/RAG 应用合集）· Nutlope/hallmark（+794★，反 AI 土味设计 skill）· coreyhaines31 营销技能赞助集（+299★）· moeru-ai/airi（+78★，虚拟伴侣/AI Waifu）

**HF 趋势榜**：zai-org/GLM-5.2（趋势分 286·3908 赞，持续霸榜）· tencent/Hy3（趋势分 361·757 赞）· empero-ai/Qwythos-9B-Claude-Mythos（趋势分 362·2094 赞，社区微调）· bottlecapai/ThinkingCap-Qwen3.6-27B · baidu/Unlimited-OCR（1964 赞）· nvidia/Nemotron-Labs-Audex-30B-A3B（语音向）· unsloth/DeepSeek-V4-Flash-GGUF 量化版 · open-gigaai/Giga-World-1（开源世界模型）· Space 榜：smolagents/hf-realtime-voice（实时语音，381 赞）· mrfakename/Z-Image-Turbo（3548 赞，图像编辑霸榜）

## 📄 研究论文

- **ABot-AgentOS**：面向长时程具身智能体的通用机器人 Agent OS，含终身多模态记忆（51 赞）
- **ABot-N1**：面向通用视觉语言导航的基础模型（48 赞）
- **LightMem-Ego**：面向手机/穿戴设备的轻量级 AI 长期记忆系统（23 赞）
- **AdvancedMathBench**：高等数学证明生成与验证基准，揭示 LLM 在高等数学上能力被高估（11 赞）

## 💬 KOL 与社区热议

- **smol.ai 综述**（标题"not much happened today"，检索 12 个 subreddit + 544 条推文，无新增 Discord）：今天罕见地"平静"，本身就是一个信号——上一轮 GPT-5.6/Codex 大发布的余震正在消化中
- **@sama**（今日高频发言，火药味与自信并存）：「只有我们觉得你够资格才回答硬核问题，不会偷偷把你降级」· 调侃网友把他的账号当反串测试（"一直找有没有拼成 c1audeai"）· 「模型终于开始擅长设计了，还是有点颠覆认知」· 「来是因为最强模型，留下是因为我们不轻视你」
- **@OpenAI**：ChatGPT 在 WhatsApp 重新恢复欧洲经济区（EEA）可用
- **@AnthropicAI**：31 万对话价值观研究详情串（见焦点）
- **@GoogleDeepMind**：用 Antigravity 的"Predicting the Past" Skill 溯源一起罗马戒指盗窃案、绘制古代教派跨欧洲传播地图——AI 考古新玩法
- **Ethan Mollick**（Bluesky）：让 Fable（Claude）做了个《伊利亚特》"船只名录"交互地图网站，效果惊艳
- **Simon Willison**（Bluesky）：GitHub Actions 里跑 `uvx` 的缓存友好写法 TIL
- **John Carmack**（Bluesky）：对喷泉码（fountain codes）技术表示惊叹
- **HN 高分**：Claude Code 插件让 Claude 等待时播放瑞克和莫蒂梗音效（128 分/54 评论，轻松向）· Show HN：用 SQL 实现神经网络（70 分/16 评论）· Show HN：Jacquard，一门"AI 写、人审核"的编程语言（66 分/39 评论）· 微软早期部署 Claude Code 与 GitHub Copilot CLI 的实证研究（46 分/28 评论）· Agents.md 吐槽向短文（34 分/9 评论）· Show HN：Sx 2.0，用 Dropbox 文件夹当团队技能服务器（26 分/26 评论）· DoorDash 用 LLM 陪审团构建食品元数据（22 分/5 评论）

## 🇨🇳 中文圈热点

- **微博热搜**：#AI脸 恐怖谷效应#（热搜 #30，26.3 万）· #AI时代最危险的岗位是什么#（热搜 #48，21.1 万）
- **知乎热榜**：苹果测试中国企业长鑫存储内存芯片背后的战略考量（热榜 #10，197 万热度）· AI 生成劣质信息是否已开始占领互联网（热榜 #26，58 万热度）
- **掘金 AI 热榜**（除已入焦点/其它板块外）：凌晨睡不着给台风巴威写追踪网站（10962 阅读，持续霸榜 3 天）· 三年了为什么 AI 应用还没爆发（2032 阅读）· 100+ 简历优化经验整理成 Skill（1903 阅读）· 图解 120 个 LLM 核心概念上/下篇（1379+942 阅读）· 大模型推理服务从 5 万到日均 2000 万次调用的性能工程实践（1252 阅读）· 一个看不见的撇号追踪中国开发者三个月（1116 阅读，持续发酵第 5 天）· Claude Code/Cursor/Codex 三工具真实差距横评（1108 阅读）· Playwright + 多 Agent 一键还原任意网站（912 阅读）· Grok4.5 发布马斯克上桌（751 阅读）· browser use 实现原理拆解（729 阅读）· Agent Tool Search 按需加载原理（713 阅读）· Hy3+WorkBuddy 国产顶级 Agent 组合（549 阅读）· AI 写代码快 3 倍但 Code Review 全变成自己的（445 阅读）· 22 道 AI Agent 工程师面试题（439 阅读）· AI 编程普及初学者还要不要学基础语法（437 阅读）· 不会前端一天给公司 BI 系统装 AI 智能体（400 阅读）
- **量子位**：爱诗科技完成 29.8 亿元 C 轮融资 · 菲尔兹奖疑似提前泄露传闻（存疑，非 AI 相关暂不展开）· Agent 专用搜索登顶 Product Hunt（中国团队出品）· 浪潮信息单柜养 4 万 Agent + 多模融合超节点 · WAIC 思想者论坛聚焦"谁在拆解 AI 底层的底层" · 问界母公司突发亏损预警
- **IT之家**：9 年 iOS 开发者 100% AI 编写代码打造外卖游戏，斩获 2.5 万美元奖金 · 孙正义称核聚变将是 AI 未来供电关键 · QuestMobile 6 月 AI 原生 App 月活榜，豆包 3.8 亿"断层第一" · AI 大模型周榜代码榜首易主，claude-opus-4-7-thinking 登顶 · 上半年算力硬件进出口 5.13 万亿元，增 56.6% · 三星 Dremo & Minimo 儿童机器人斩获红点最佳概念奖（子母 AI 套件）· 特斯拉开发轮椅无障碍自动驾驶汽车
- **36氪**：浙大系桌面 CNC 团队获近亿元天使轮 · 前博世自动驾驶算法工程师创业做触觉大模型（大衍科技，数千万天使轮）· Meta 追加 400 亿美元投资路易斯安那数据中心 · B 站"AI 创造公开赛"投币榜上线，近 5000 创作者参赛 ·"新奇机器人"完成 A+ 轮融资
- **雷锋网**：激光雷达割草机器人商业化故事（耐士劳）· 长鑫近 2 万员工分红超百万，IPO 造富 ·《智能体个人信息保护自律公约》31 家企业首批签署 · 文远知行 L2++ 智驾方案出海德法日

## ⚠️ 本次异常源

抓取全部正常（25/25，157 条）。**流程异常**：本次 fetch-daily.yml 的三班次 `schedule` 触发（02:35/02:55/03:15 UTC）全部被 GitHub 延迟约 3.5 小时，实际产物 06:57 UTC 才提交（脚本自身运行仅约 30 秒，延迟完全来自 GitHub Actions 调度排队），导致云端整理 routine 按规范等待 1 小时无果后判定"今日跳过"。本期由人工触发补发。已同步修复触发机制：`fetch-daily.yml` 新增基于 push 的即时触发通道，日报 routine 检测不到 items.json 时会主动 push 一个标记文件唤起抓取，不再单纯依赖不可靠的 GitHub `schedule` 事件（该事件本身在 GitHub 官方文档中即注明"best effort，高峰期可能延迟"）。详见本仓库 `.github/workflows/fetch-daily.yml` 与 routine 配置变更。
