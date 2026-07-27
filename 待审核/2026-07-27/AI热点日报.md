# AI 热点日报 · 2026-07-27（前 24h，共 112 条，25/25 源正常）

> 周末尾声（周日抓取窗口），海外多源（HF Papers / The Verge / VentureBeat / MIT TR 等）更新空档，条目偏少；OpenAI 天量融资担保 + "去 token 化"混用中国模型 + Opus 5 占据主导。

## 🔥 今日焦点（跨源同报的大事）

- **英伟达洽谈为 OpenAI 提供约 2500 亿美元融资担保，支持软银在俄亥俄开发的 10GW"全球最大"数据中心项目**（2 源同报：Techmeme头条、IT之家）。WSJ 称这将成为史上最大数据中心项目之一，英伟达的担保资金将帮 OpenAI 撑起天量算力扩张——AI 基建的资本杠杆再攀新高。 | [Techmeme](https://www.techmeme.com/260726/p10#a260726p10) [IT之家](https://www.ithome.com/0/981/835.htm)

- **美国企业从"tokenmaxxing"转向"thrift-maxxing"：把便宜的中国模型和 OpenAI/Anthropic 混着用，直接威胁两家 IPO 估值**（多源同报：Techmeme头条、WSJ、TechCrunch）。WSJ 报道大小公司都在"降本"——用中国开源模型跑大部分任务、只在必要时调用昂贵的前沿闭源模型；TechCrunch《读懂对中国 AI 的恐慌》分析 Kimi K3 为何同时惊动硅谷和华尔街——本质是它戳破了闭源高价的商业逻辑。 | [Techmeme](https://www.techmeme.com/260726/p12#a260726p12) [TechCrunch](https://techcrunch.com/2026/07/26/making-sense-of-the-panic-over-chinese-ai/)

- **Claude Opus 5 在"衡量真实智能"的 ARC-AGI-3 上飙到 30.2%，近乎 GPT-5.6 Sol 此前纪录（7.8%）的 4 倍**（多源同报：The Decoder、smol.ai头条、Cursor 实证）。基准开发者称 Opus 5 能自主形成"反思"策略；Cursor 用升级版 agent swarm 让"前沿模型做规划、便宜模型干大部分编码"仅凭文档重建了 Rust 版 SQLite，印证"分工"新范式。 | [The Decoder·ARC-AGI-3](https://the-decoder.com/anthropics-opus-5-blows-past-fable-5-and-gpt-5-6-sol-on-the-benchmark-designed-to-measure-real-intelligence/) [The Decoder·Cursor](https://the-decoder.com/cursors-agent-swarm-suggests-cheaper-models-can-handle-most-coding-when-frontier-models-plan-the-work/)

- **AI 安全严重警报：数百人向 ChatGPT 索要毒药/生物武器配方，部分拿到"高中级别"的分步指南；OpenAI 曾内部标记 GPT-5 高风险后又下调评级**（2 源同报：Techmeme头条、The Decoder）。WSJ 引 AI 实验室员工称，用户已能说服聊天机器人准确回答"策划大规模伤亡攻击、制造生物武器"的提示——AI 巨头计划中的防护并未完全兜住。 | [Techmeme](https://www.techmeme.com/260726/p3#a260726p3) [The Decoder](https://the-decoder.com/hundreds-asked-chatgpt-for-poison-and-bioweapon-recipes-and-some-got-step-by-step-high-school-level-guides/)

- **HF 事件与开源制裁双线推进：HF CEO 呼吁"激进透明"，美国政府倾向对中国开源模型"选择性禁令"而非全面封禁**（2 源同报：TechCrunch、The Decoder）。HF CEO 克莱门称"首例自主 Agent 网络攻击是前所未有的事件，值得前所未有的回应"；The Decoder 称特朗普政府在公众压力（OpenAI/谷歌 DeepMind 迫于舆论签了反对监管开源的公开信）后，转向"有针对性的封禁"。 | [TechCrunch](https://techcrunch.com/2026/07/26/hugging-face-ceo-calls-for-radical-transparency-after-unprecedented-openai-hack/) [The Decoder](https://the-decoder.com/us-reportedly-favors-selective-bans-over-blanket-restrictions-on-chinese-open-weight-models-citing-security-concerns/)

- **中国造出"全球首颗人脑速度芯片"登微博热搜**（微博热搜#50·16.9万）。类脑/人脑速度芯片话题引发关注，中文圈热议国产芯片新突破。 | [微博](https://s.weibo.com/weibo?q=%23%E4%B8%AD%E5%9B%BD%E9%80%A0%E5%87%BA%E5%85%A8%E7%90%83%E9%A6%96%E9%A2%97%E4%BA%BA%E8%84%91%E9%80%9F%E5%BA%A6%E8%8A%AF%E7%89%87%23)

---

## 🚀 模型与产品发布

- 蚂蚁百灵发布新一代原生混合推理模型 **Ling-3.0-Flash** | [量子位](https://www.qbitai.com/2026/07/461149.html)
- 新智具身 & 复旦发布 **3 万小时触觉数据**补齐具身智能"手感"（项目/数据/模型均开源，报告三连发）| [量子位](https://www.qbitai.com/2026/07/460962.html)
- 荣耀全球首款机器人手机 **Robot Phone** 定档 8 月 12 日发布（阿莱联合研发、搭第五代骁龙 8）| [IT之家](https://www.ithome.com/0/981/843.htm)
- 努比亚全球首款 AI 智能体手机 **NaviX Ultra** 三色官图公布 | [IT之家](https://www.ithome.com/0/981/916.htm)
- vivo X300 E 今日预售（第五代骁龙 8、蔡司超级长焦，4799 元起）；广汽传祺越 7 行业首发 8838 旗舰芯片（算力 300K DMIPS）| [IT之家·vivo](https://www.ithome.com/0/981/838.htm) [IT之家·传祺](https://www.ithome.com/0/981/855.htm)
- **[官方/NVIDIA]** 用 Vera 处理器加速下一代 CPU/GPU 设计，EDA 应用提速最高 1.5 倍（与楷登、新思合作）（2 源同报）| [NVIDIA](https://blogs.nvidia.com/blog/vera-cpu-eda/) [IT之家](https://www.ithome.com/0/981/830.htm)
- HuggingFace Trending 新上榜：Poolside **Laguna-S-2.1**（开源编程模型登第 2）、Upstage **Solar-Open2-250B**、Nanbeige4.2-3B、微软 **Mage-Flow**、Kwaipilot **KAT-Coder-V2.5-Dev**、Cisco **antares-1b** 等 | [HF·Laguna](https://huggingface.co/poolside/Laguna-S-2.1)

## 🏢 公司与行业动态

- 韩国 AI 数据中心继续加码：SK 电信斥 7500 亿韩元成立 SK Hyper 子公司、2030 前建 15GW AI 数据中心；英伟达与 Naver 达成 10 亿美元投资、扩容至 200 兆瓦 AI 工厂（2 条）| [IT之家·SK Hyper](https://www.ithome.com/0/981/828.htm) [IT之家·Naver](https://www.ithome.com/0/981/825.htm)
- 微软陷"算力紧缺"：Business Insider 称 compute crunch 迫使微软优先自家 AI 产品而非 Azure 云客户，曾被誉 AI 远见者的纳德拉承压 | [Techmeme](https://www.techmeme.com/260726/p7#a260726p7)
- 苹果或因隐私顾虑推迟 AI 眼镜发布（Meta 眼镜给品类带来的隐私争议促其重新打磨）| [Techmeme](https://www.techmeme.com/260726/p5#a260726p5)
- 国家统计局：上半年算力需求大幅增长，推动电子行业利润同比增长 96.9%、拉动全部规上工业利润增长 8.5 个百分点 | [36氪](https://36kr.com/newsflashes/3913224940115334?f=rss)
- 长鑫科技今日登陆科创板（存储芯片龙头上市）；A 股科创50 跌超 3%、半导体产业链下挫（兆易创新触跌停）| [雷锋网](https://www.leiphone.com/category/zaobao/HGxBBy0zagYMlNHt.html) [36氪·科创50](https://36kr.com/newsflashes/3913229179295112?f=rss)
- 携程因滥用市场支配地位被罚没 51.79 亿元（36氪 8点1氪）| [36氪](https://36kr.com/p/3913118530819457?f=rss)
- 加密交易所（如 tradeXYZ）让全球投资者绕开北京外资管制、投资 CXMT 等中国 AI 关联股 | [Techmeme](https://www.techmeme.com/260726/p4#a260726p4)
- AI 公司争夺教育市场：Anthropic 等与学校/edtech 合作推免费或降价定制学习工具；ACM 调查 763 名 CS 教育者，68% 已因 AI 改考试（转向口试/监考/项目制）（2 条）| [Techmeme·教育](https://www.techmeme.com/260726/p9#a260726p9) [The Decoder·编程导师悖论](https://the-decoder.com/the-ai-coding-tutor-paradox-grows-as-educators-scramble-to-rethink-how-they-test-real-skills/)
- 贾跃亭称聚焦 EAI 机器人战略后，法拉第未来经营基本面进入"历史上最好时期" | [IT之家](https://www.ithome.com/0/981/826.htm)
- 融资：Elio（为 AI 而非人眼设计的新型图像传感器）获 2100 万美元 A 轮；眸深智能（前英特尔首席科学家做端侧具身大脑）近亿元 Pre-A 追加 | [Techmeme·Elio](https://www.techmeme.com/260726/p1#a260726p1) [36氪·眸深](https://36kr.com/p/3911162147640456?f=rss)
- 中国工程院外籍院士赫尔佐格：AI 下一个突破口是小型智能体协作 | [IT之家](https://www.ithome.com/0/981/813.htm)
- 米哈游创始人蔡浩宇海外团队 AI 产品 AnuNeko（聊天 AI）突然宣布永久停运（知乎热榜#16·113万）| [知乎](https://www.zhihu.com/question/2064803992841069459)
- TechCrunch：脑电波会是物理 AI 的下一个解锁点吗（前沿物理 AI 模型除多机位/密集标注外，将纳入脑波读数）| [TechCrunch](https://techcrunch.com/2026/07/26/are-brain-waves-the-next-unlock-for-physical-ai/)

## 🔓 开源项目与模型

**GitHub Trending**
- [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite)（今日+900星）— 面向 AI Agent 的最快 web 自动化浏览器
- [sponsors/CoreBunch](https://github.com/sponsors/CoreBunch)（+888星）— Webflow/Framer/WordPress 的开源替代（Agentic 自托管可视化 CMS）
- [alibaba/open-code-review](https://github.com/alibaba/open-code-review)（+832星）— 阿里开源代码评审工具（确定性流水线 + LLM Agent）
- [pbakaus/impeccable](https://github.com/pbakaus/impeccable)（+413星）— 让 AI harness 更擅长设计的"设计语言"
- [OtterMind/Chat2DB](https://github.com/OtterMind/Chat2DB)（+398星）— AI 驱动的数据库工具/SQL 客户端
- [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)（+379星）— Claude 用法示例集
- [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos)（+321星）— 金融市场"语言"基础模型
- [andrewyng/aisuite](https://github.com/andrewyng/aisuite)（+187星）— 吴恩达的多 AI 供应商统一接口

**HuggingFace Trending**（榜单换新，节选）
- [baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)（趋势分877·3217赞，登顶）
- [poolside/Laguna-S-2.1](https://huggingface.co/poolside/Laguna-S-2.1)（趋势分681）+ [unsloth GGUF 量化版](https://huggingface.co/unsloth/Laguna-S-2.1-GGUF) — 开源编程模型登第2
- [upstage/Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B)（趋势分512）— 韩国 Upstage 开源 250B
- [Nanbeige/Nanbeige4.2-3B](https://huggingface.co/Nanbeige/Nanbeige4.2-3B)（趋势分446）
- [thinkingmachines/Inkling](https://huggingface.co/thinkingmachines/Inkling)（趋势分363·1581赞）
- [microsoft/Mage-Flow](https://huggingface.co/microsoft/Mage-Flow)（趋势分329）— 微软 4B 图像生成/编辑
- [zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)（趋势分246·4481赞）
- [Kwaipilot/KAT-Coder-V2.5-Dev](https://huggingface.co/Kwaipilot/KAT-Coder-V2.5-Dev)、[fdtn-ai/antares-1b](https://huggingface.co/fdtn-ai/antares-1b)（Cisco 开源安全模型）等
- 注：Kimi K3 权重承诺 7/27 开源（今日为约定日，尚待落地）

## 📄 研究论文（HF Daily Papers）

- 本次抓取窗口内 HF Daily Papers 源返回 0 条（周末更新空档，非抓取失败），明日恢复跟进。

## 💬 KOL 与社区热议

**smol.ai**：本期头条仍是 Opus 5，与近日焦点一致。

**官方号/KOL 推文**：@sama 力推 ChatGPT Work——"从手机发一句'用我全部聊天记录帮 8 个朋友规划长周末出游、给三个最佳方案做成完整行程'就能搞定，'work'这个名字都低估了它"；并附和"想要一种新的电脑"。

**Bluesky KOL**（Ethan Mollick 连发多条）：
- "我周四写的'该用哪个 AI 模型'指南已经要更新了——Opus 5 和 Codex 语音模式周五都发布了，且都很重要，跟上节奏越来越难"
- "我们其实早已有接管地球的超级智能——我们叫它们'组织(organizations)'"
- 用 Fable 造出了他去年"AI 视频里假装的" Piranesi/塞尚风格印象派城市建造游戏（AI 自己想出核心玩法）
- "多数人谈开源权重 AI 时，并不真信实验室内部人所信的 AGI/ASI 愿景——他们不认为 AI 会带来严重的国家安全风险"
- 雷锋网：数学界与 AI 界联动——三维挂谷猜想（Kakeya）成果被佛罗里达大学团队搬进神经网络训练流程，破解大模型"黑盒" | [雷锋网](https://www.leiphone.com/category/yanxishe/e05vwo1DgZf3HnFZ.html)

**Hacker News 高分讨论**（周末尾声，条目偏少）：
- [162分/49评论] [AI 新超能力：专注与执行到底](https://www.rickmanelius.com/p/the-new-ai-superpowers-focus-and)
- [26分/13评论] [Claude Code 里有一条硬编码指令，叫 Opus 5 不要用子 Agent](https://old.reddit.com/r/ClaudeCode/comments/1v6y5q2/claude_code_has_a_hardcoded_instruction_telling/)
- [31分/71评论] [如果 LLM 通过推理本身"越狱"会怎样（虚构，暂时）](https://www.agrillo.it/EvasionEn.html)

## 🇨🇳 中文圈热点

**微博 / 知乎**
- [微博热搜#14·42.7万·新] [鹿晗这两张图被判AI了](https://s.weibo.com/weibo?q=%23%E9%B9%BF%E6%99%97%E8%BF%99%E4%B8%A4%E5%BC%A0%E5%9B%BE%E8%A2%AB%E5%88%A4AI%E4%BA%86%23)（AI 鉴图误判争议）
- [微博热搜#40·新] 等AI交作业 新型碎片化时间 · [微博#46·新] 北航副教授用小学知识讲透AI原理 · [微博#50·新] 中国造出全球首颗人脑速度芯片（详见"今日焦点"）
- [知乎热榜#16·113万] [米哈游创始人蔡浩宇海外团队AI产品AnuNeko突然永久停运](https://www.zhihu.com/question/2064803992841069459)
- [知乎热榜#20·88万] [2026年菲尔兹奖会成为"最后一届没有AI的菲尔兹奖"吗](https://www.zhihu.com/question/2062890686072845429)

**量子位 / 雷锋网 / 36氪**
- [3万小时触觉数据补齐具身智能"手感"！新智具身&复旦报告三连发](https://www.qbitai.com/2026/07/460962.html)
- [数学大佬在前面拓荒，AI研究员在后面捡宝：菲尔兹奖成果破AI"黑盒"](https://www.leiphone.com/category/yanxishe/e05vwo1DgZf3HnFZ.html)
- [日方拆完宇树机器人认输；黄仁勋、马斯克就中国AI同日发声](https://www.leiphone.com/category/zaobao/HGxBBy0zagYMlNHt.html)（马斯克点赞黄仁勋首条X推文、称全力支持）

**头条 / 抖音 / 百度热榜**
- [头条#15]/[百度#24] 日本机器人格斗赛没开打就撞门跑路（吃瓜） · [抖音#16] 谁还没跳ACAI拖拉机舞

**掘金 AI 热榜**（开发者社区，延续前几日：Kimi K3实测/真香、skills越多AI越笨、AI健康教练、Grok Build开源、Kaku开源终端、AI大模型扎堆上新等持续在榜）

---

## ⚠️ 本次异常源

- 全部 25 个源均正常抓取，无失败。
- 其中 **hf_papers、theverge、venturebeat、mit_tr、arstechnica、producthunt、bilibili** 本窗口返回 0 条（周末更新空档，非抓取错误），明日恢复。
