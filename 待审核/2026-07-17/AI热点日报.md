# AI 热点日报 · 2026-07-17（前 24h，共 194 条，25/25 源正常）

## 🔥 今日焦点（跨源同报的大事）

- **月之暗面 Kimi K3 发布：2.8 万亿参数、史上最大开源模型，多榜逼近甚至反超头部闭源模型**（9 源同报，全网刷屏：HN 首页 1257分/792评论、VentureBeat、The Decoder、TechCrunch、量子位/IT之家、微博热搜×2、知乎热榜#7、头条热榜#13、smol.ai）。官方定位"Open Frontier Intelligence"——2.8T 总参数、1M token 上下文、原生多模态、Kimi Delta Attention (KDA) 与 Attention Residuals 新架构，已上线 Kimi.com/Work/Code/API，开源权重承诺 7月27日放出。第三方评测印证其含金量：**LMArena 前端代码榜冲上 #1（1679分，反超 Claude Fable 5，从 K2.6 时的 #18 跃升）**，胜率 76% vs Fable 5 的 63%；Artificial Analysis 智能指数 57 分，与 Opus 4.8、GPT-5.5 相当，但官方与多位 KOL 都承认"相比 Fable 5 / GPT-5.6 Sol 在用户体验上仍有明显差距"。IT之家另注意到 K3 技术博客特别展示了"AI 为 AI 设计芯片"能力——2 天完成构建、优化、验证。 | [HN](https://www.kimi.com/blog/kimi-k3) [VentureBeat](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems) [The Decoder](https://the-decoder.com/kimis-open-model-k3-nears-gpt-5-6-sol-and-fable-5-while-signaling-the-end-of-super-cheap-chinese-ai/) [知乎](https://www.zhihu.com/question/2061204677446964906) [IT之家](https://www.ithome.com/0/977/961.htm)

- **2026 世界人工智能大会（WAIC）在上海开幕，习近平出席开幕式，全网头条级刷屏**（多源同报：36氪、微博热搜#3·97万、抖音热榜×3、百度热榜、量子位、雷锋网、IT之家）。7月17日上午习近平在上海出席 2026 世界人工智能大会暨人工智能全球治理高级别会议开幕式；大会主题"智能伙伴 共创未来"，聚焦 AI 创新发展与安全治理双向协同；"镇馆之宝"名单揭晓（蚂蚁灵波机器人智慧药房、中科曙光全国产十万卡AI超算、百度搭子等）。 | [36氪·习近平出席](https://36kr.com/newsflashes/3899087542699648?f=rss) [微博](https://s.weibo.com/weibo?q=%23%E4%B8%96%E7%95%8C%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E5%A4%A7%E4%BC%9A%E4%BB%8A%E5%A4%A9%E5%BC%80%E5%B9%95%23) [雷锋网](https://www.leiphone.com/category/industrynews/lxXkqwf4vc9J3opM.html)

- **谷歌旗舰模型 Gemini 3.5 Pro 被曝已延期数月，技术表现（尤其编程）未达内部目标**（3 源同报：HN、Bloomberg、IT之家）。10 名现任及前员工透露，谷歌希望进一步提升模型能力尤其编程表现，因而迟迟未按计划推出。 | [HN/Bloomberg](https://www.bloomberg.com/news/articles/2026-07-16/google-gemini-launch-delayed-as-tech-falls-short-of-internal-goals) [IT之家](https://www.ithome.com/0/977/847.htm)

- **谷歌把 NotebookLM 改名 Gemini Notebook，并开放 AI Mode 接入第三方应用**（4 源同报：HN 首页 262分、The Verge、The Decoder、TechCrunch）。NotebookLM 更名为 Gemini Notebook，仍保留独立 App 但更深度整合进 Gemini 生态，每个 notebook 获得可写代码/运行代码的专属云电脑；AI Mode 新增连接并操作选定应用的能力，从"回答问题"迈向"完成任务"。 | [The Verge](https://www.theverge.com/tech/966112/google-gemini-notebook-notebooklm) [The Decoder](https://the-decoder.com/google-rebrands-notebooklm-as-gemini-notebook-and-opens-its-search-app-to-third-party-integration/) [TechCrunch](https://techcrunch.com/2026/07/16/googles-ai-mode-now-lets-you-link-and-interact-with-select-apps/)

- **1Password 推出"1Password for Claude"，Claude 可调用你存储的账号密码凭证**（3 源同报：HN、The Verge、venturebeat 语境）。1Password 为 Claude 推出浏览器集成，让 Anthropic 的 Claude 在不暴露明文凭证的前提下代用户登录，直击当下"AI Agent 凭证共享安全"的痛点。 | [The Verge](https://www.theverge.com/tech/966442/1password-anthropic-claude-browser-integration) [HN](https://1password.com/blog/1password-for-claude)

- **Suno 源码泄露事件持续发酵，中英同报坐实其全网爬歌训练**（2 源同报，续昨日：IT之家、Techmeme语境）。基于黑客披露的 Suno 内部源码，404Media 报道其从 YouTube Music、Deezer、Genius 抓取数百万首歌构建核心模型；同期 Spotify 宣布去年已下架超 7500 万首 AI 生成歌曲。 | [IT之家·Suno](https://www.ithome.com/0/977/878.htm) [IT之家·Spotify](https://www.ithome.com/0/977/955.htm)

---

## 🚀 模型与产品发布

- **[官方/Google DeepMind]** 与 Isomorphic Labs 联合发布"生物韧性（bioresilience）"方法论，用 AI 模型应对未来疫情/生物安全 | [DeepMind](https://deepmind.google/blog/our-approach-to-bioresilience/)
- **[官方/Google AI]** Google Vids 两项更新：Gemini Omni + 个人虚拟形象，用户可"出演"自己的 AI 视频（2 源同报）| [Google](https://blog.google/products-and-platforms/products/workspace/gemini-omni-personal-avatars/) [TechCrunch](https://techcrunch.com/2026/07/16/google-vids-now-lets-you-star-in-your-own-ai-videos/)
- **[官方/Google AI]** 搜索 AI Mode 新增"连接更多应用"，可在 AI Mode 内安全联动常用服务 | [Google](https://blog.google/products-and-platforms/products/search/connected-apps/)
- **[官方/OpenAI]** 发文《为什么青少年应该用上安全的 AI》，公布面向青少年的年龄适配保护、学习工具、家长控制 | [OpenAI](https://openai.com/index/why-teens-deserve-access-safe-ai)
- **[官方/HuggingFace]** NVIDIA Nemotron 3 Embed 登顶 RTEB 检索基准 #1，推进 Agentic 检索 | [HuggingFace](https://huggingface.co/blog/nvidia/nemotron-3-embed-wins-rteb)
- **Thinking Machines（Mira Murati 创立）Inkling 持续高热**：975B 开源多模态模型，登顶 HF Trending（趋势分815），领先美国开源阵营但落后中国头部（2 源同报）| [The Decoder](https://the-decoder.com/ex-openai-cto-muratis-thinking-machines-drops-inkling-a-975b-parameter-model-that-leads-us-labs-but-trails-china/)
- **LM Studio Bionic** 上线：面向开源模型的 AI 智能体工具，可调用 GLM 5.2、Kimi K3 等做编程/研究/文档（2 源同报）| [HN](https://lmstudio.ai/blog/introducing-lm-studio-bionic) [IT之家](https://www.ithome.com/0/977/860.htm)
- Sakana AI 的 Fugu 编排器接入 NVIDIA Nemotron，力证"集体智能"可媲美单一前沿模型 | [The Decoder](https://the-decoder.com/sakana-ais-fugu-adds-nvidia-nemotron-to-prove-collective-intelligence-can-rival-single-frontier-models/)
- Gemma 4 悄悄更新（同名 stealth update）：修复工具调用 bug、截断响应问题，Hopper GPU 上提速 | [The Decoder](https://the-decoder.com/gemma-4-gets-a-stealth-update-that-fixes-tool-calling-bugs-and-truncated-responses-under-the-same-name/)
- Roblox 移动端推出"Build"功能：一句话提示词即可生成基础游戏（2 源同报）| [TechCrunch](https://techcrunch.com/2026/07/16/roblox-launches-an-ai-powered-game-creation-feature-in-its-mobile-app/) [IT之家](https://www.ithome.com/0/977/876.htm)
- DoorDash 开放 dd-cli 命令行工具限量测试，开发者与 AI Agent 可在终端搜索店铺/建购物车/下单 | [TechCrunch](https://techcrunch.com/2026/07/16/yes-you-can-now-order-doordash-from-the-command-line/)
- 银河通用发布全球首个"仅需人类视频即可部署"的机器人新框架，可边干边学 | [量子位](https://www.qbitai.com/2026/07/451403.html)
- 无问芯穹与清华联合发布 RLinf v0.3：从模型生态到真机部署五大能力跃升，具身智能"进化底座" | [量子位](https://www.qbitai.com/2026/07/451379.html)
- 金山办公发布两款 AI 办公智能体：个人版"灵犀专业版"、企业版"WPS Comate"；CEO 章庆元称订阅与 Token 计费将长期并存 | [IT之家](https://www.ithome.com/0/977/946.htm)
- 阿里 ATH 事业群将推 AI 音乐创作平台"HappyShrimp/快乐虾米"，主打一句话生成专属音乐 | [IT之家](https://www.ithome.com/0/977/869.htm)
- 努比亚/中兴 AI 宠物机器人 iMoochi 发售，1699 元 | [IT之家](https://www.ithome.com/0/977/959.htm)
- 理想 L6 换代 24.98 万开卖，L9 同款自研芯片中控屏下放 | [量子位](https://www.qbitai.com/2026/07/451576.html)
- ProductHunt 新品：**ClipMatch**（AI 把相册变社媒内容）| [PH](https://www.producthunt.com/products/clipmatch)

## 🏢 公司与行业动态

- 微软本月将推出 AI 安全工具，混用 Anthropic、OpenAI 及自研模型，定位 Mythos 的高性价比替代（Techmeme 头条）| [Techmeme](https://www.techmeme.com/260716/p68#a260716p68)
- 智谱 ARR（年度经常性收入）已达 10 亿美元，半年增长 15 倍（2 源同报）| [36氪](https://36kr.com/p/3898662052693894?f=rss) [IT之家](https://www.ithome.com/0/977/873.htm)
- DeepSeek 最新估值曝光：3250 亿–3500 亿元区间（开润股份公告间接投资穿透测算）| [IT之家](https://www.ithome.com/0/977/882.htm)
- OpenAI 160 亿美元"星际之门"（Stargate）数据中心项目遇阻，当地居民担忧水污染/拉高电费 | [IT之家](https://www.ithome.com/0/977/885.htm)
- 欧盟责令谷歌向竞品开放 Android 与搜索的关键部分（DMA 反垄断），第三方 AI 助手/搜索引擎将获更多访问权 | [The Verge](https://www.theverge.com/policy/966438/eu-google-android-ai-interoperability-search-data-dma)
- 德国监管首例裁定：Google AI Overviews 与 Perplexity 被纳入媒体法监管，认定 AI Overviews 是谷歌自有内容而非中立搜索结果 | [The Decoder](https://the-decoder.com/germany-puts-googles-ai-overviews-and-perplexity-under-media-law-in-first-of-its-kind-ruling/)
- 苹果与 OpenAI"窃密大战"新细节：一句"哈哈"引发，苹果怒斥"烂到骨子里"（续前日诉讼）| [量子位](https://www.qbitai.com/2026/07/450921.html)
- Apple Intelligence 获批在华上线，接入阿里 Qwen 与百度（2 源同报，续前日）| [TechCrunch](https://techcrunch.com/2026/07/16/apple-intelligence-approved-for-launch-in-china-with-alibabas-qwen-ai/) [知乎](https://www.zhihu.com/question/2058326197759743941)
- 英国机器人初创 Humanoid 完成 A 轮首笔 1.5 亿美元（投前估值 12 亿美元），9 月前再募 8000万–1亿 | [Techmeme](https://www.techmeme.com/260716/p60#a260716p60)
- Netflix 称今年约 300 部作品用到生成式 AI（多在后期），以更快更低成本产出更高质量 | [Techmeme](https://www.techmeme.com/260716/p56#a260716p56)
- MLB 禁止球队用联盟配发的 iPad 在场边调用生成式 AI 做战术决策，据称至少 1/3 球队此前如此使用 | [Techmeme](https://www.techmeme.com/260716/p64#a260716p64)
- NYT 记者发现 Amazon 上充斥 AI 生成的、未授权的记者传记，"作者"身份成谜的 AI 书籍泛滥 | [Techmeme](https://www.techmeme.com/260716/p55#a260716p55)
- 前 DeepMind 研究员 Andrew Dai 以 3 亿美元 pre-seed 估值融资（产品尚未发布）| [TechCrunch](https://techcrunch.com/2026/07/16/how-a-former-deepmind-researcher-raised-at-a-300m-pre-seed-valuation-before-launching-a-product/)
- Yann LeCun 的世界模型创业 AMI Labs CEO Alexandre LeBrun：拒绝把自家 AI 叫"AGI"或"超级智能" | [TechCrunch](https://techcrunch.com/2026/07/16/why-ami-labs-alexandre-lebrun-wont-call-his-ai-agi-or-superintelligence/)
- Applied Computing 融资 2000 万美元 A 轮，为油气行业造覆盖全厂的基础 AI 模型 | [TechCrunch](https://techcrunch.com/2026/07/15/applied-computing-wants-to-give-oil-and-gas-operators-an-ai-model-for-the-entire-plant/)
- 能源公司 IPO 本世纪最快节奏涌现，投资者借道押注 AI 数据中心用电潮 | [Ars Technica](https://arstechnica.com/information-technology/2026/07/energy-ipos-surge-as-investors-hunt-for-ways-to-play-ai-boom/)
- xAI 因大规模数据泄露后开源 Grok Build（续前日）：CLI 曾静默上传含 SSH 密钥/密码库的整个目录，马斯克承诺删除已上传数据 | [The Decoder](https://the-decoder.com/xai-open-sources-grok-build-on-github-after-massive-data-breach/)
- 纽约州长 Hochul：正用 AI 分析该州"每一条法规"（尽管刚签署新数据中心暂停令）| [The Verge](https://www.theverge.com/ai-artificial-intelligence/966647/new-york-governor-kathy-hochul-ai-policies)
- 具身智能"第一个基建商"出现：Robotaxi 第一股文远知行孵化 | [量子位](https://www.qbitai.com/2026/07/451327.html)
- 中国移动投资友机技术，押注"工业母机计算化"下一代基础设施 | [量子位](https://www.qbitai.com/2026/07/451371.html)
- 多起具身智能/机器人融资：模感科技（全身触觉，红杉/高瓴/智元）、日冕开物（具身世界模型，数亿元，百度风投等）、半醒具身（人形机器人ODM）、酷奇奇科技（AI角色硬件，商汤跟投）| [36氪·模感](https://36kr.com/p/3899128277452681?f=rss) [36氪·日冕](https://36kr.com/p/3899081603483525?f=rss)
- 中国一汽基于千问自研的行业大模型入驻阿里云百炼，业内首个商业化服务的行业大模型面向全行业开放 | [雷锋网](https://www.leiphone.com/category/industrynews/REYfC0ECzRMeS8hD.html)
- 国产 DPU 厂商云豹智能递交创业板 IPO，被视作"国产 DPU 第一股"，但连亏三年+营收依赖单一大客户引争议 | [雷锋网](https://www.leiphone.com/category/chips/lxIbicm9WU6RU1Qe.html)
- 深氪：中专生刘梓瑜用 AI 拍出全网播放破亿短片《丧尸清道夫》，收到好莱坞制作人 Offer | [36氪](https://36kr.com/p/3898151587890824?f=rss)

## 🔓 开源项目与模型

**GitHub Trending**
- [Nutlope/hallmark](https://github.com/Nutlope/hallmark)（今日+3372星，登顶）— 反 AI 糊味设计 skill（Claude Code/Cursor/Codex）
- [sponsors/mattpocock](https://github.com/sponsors/mattpocock)（+2060星）— "Skills for Real Engineers"
- [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)（+1107星）— 把任意代码/文档/论文文件夹变可查询知识图谱的 AI coding skill
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)（+923星）— 100+ 可跑的 AI Agent & RAG 应用合集
- [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter)（+661星）— 面向开源模型（如 Kimi K3）的编程 Agent
- [PostHog/posthog](https://github.com/PostHog/posthog)（+77星）— AI 可观测性/分析/会话回放平台
- [sponsors/lobehub](https://github.com/sponsors/lobehub)（+71星）— 把 Agent 编入 7×24 运营的"首席 Agent 运营官"
- [apache/ossie](https://github.com/apache/ossie)（+60星）— Apache Ossie，跨分析/AI/BI 平台交换语义元数据的标准化规范
- [github/copilot-sdk](https://github.com/github/copilot-sdk)（+13星）— 把 GitHub Copilot Agent 集成进应用的多平台 SDK

**HuggingFace Trending**（节选）
- [thinkingmachines/Inkling](https://huggingface.co/thinkingmachines/Inkling)（趋势分815·827赞，登顶）
- [prism-ml/Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)（趋势分589）+ [Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)（趋势分339）— 可塞进 iPhone 的 27B 推理模型持续走热
- [zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)（趋势分234·4030赞）— 智谱模型持续高热
- [tencent/Hy3](https://huggingface.co/tencent/Hy3)（趋势分169·813赞）
- [ATH-MaaS/OvisOCR2](https://huggingface.co/ATH-MaaS/OvisOCR2)（趋势分135）— 0.8B 文档解析模型，同日有技术报告论文
- [InternScience/Agents-A1](https://huggingface.co/InternScience/Agents-A1)（趋势分129·568赞）
- [smolagents/hf-realtime-voice](https://huggingface.co/spaces/smolagents/hf-realtime-voice)（Space·趋势分59）
- 其余同质化 GGUF 微调/角色扮演类模型（Qwythos 系列、Qwen3.6-Uncensored、MiniCPM5-Claude-Opus 等）热度较高但多为社区二创，未单独展开

## 📄 研究论文（HF Daily Papers）

- **[46赞]** [KnowAct-GUIClaw](https://huggingface.co/papers/2607.12625) — 具备自进化记忆与技能的个人 GUI 助手，补强跨平台 GUI 交互
- **[43赞]** [OvisOCR2 Technical Report](https://huggingface.co/papers/2607.13639) — 0.8B 端到端文档解析模型，图像→Markdown
- **[23赞]** [GigaWorld-Policy-0.5](https://huggingface.co/papers/2607.13960) — AutoResearch 加持的更快更强世界动作模型（WAM）
- **[18赞]** [SEED: Self-Evolving On-Policy Distillation for Agentic RL](https://huggingface.co/papers/2607.14777) — 面向 Agent 强化学习的自进化在策略蒸馏
- **[11赞]** [BadWAM: When World-Action Models Dream Right but Act Wrong](https://huggingface.co/papers/2607.15207) — 世界动作模型"想对了却做错了"的失效分析
- **[11赞]** [Hallo4D](https://huggingface.co/papers/2607.12752) — 多模态幻觉缓解，一致的时空生成
- **[9赞]** [AgentCompass](https://huggingface.co/papers/2607.13705) — 统一的 Agent 能力评测基础设施
- **[8赞]** [SearchOS-V1](https://huggingface.co/papers/2607.15257) — 鲁棒的开放域信息检索 Agent 协作
- **[7赞]** [Video = World + Event Stream](https://huggingface.co/papers/2607.15038) — Wan-Streamer v0.3，原生流式交互模型
- **[7赞]** [Discrete Diffusion Models: A Unified Framework](https://huggingface.co/papers/2607.13431) — 离散扩散模型从 tokenization 到生成的统一框架

## 💬 KOL 与社区热议

**smol.ai 每日综述要点**（本期主题即 Kimi K3，标题"平静的一天"名不副实）：
- Moonshot 正式发布 Kimi K3"Open Frontier Intelligence"：2.8T 参数、1M 上下文、原生多模态、KDA 注意力，权重承诺 7/27 开源，若兑现即史上最大开源权重模型
- 主打长程 Agentic 编程与自进化工作流，以及"vision in the loop"（代码↔截图迭代）的编程/游戏构建
- LMArena 前端代码榜 K3 冲 #1（1679分，胜率76%），从 K2.6 的 #18 跃升；文本榜 #9（1486分，从 #38 跃升）
- Artificial Analysis 独立评测：AA 智能指数 57，与 Opus 4.8/GPT-5.5 相当，但整体仍落后 Fable 5 / GPT-5.6 Sol；官方自认"用户体验仍有明显差距"

**官方号/KOL 推文**（zpravobot 转发）：
- @sama：新语音模型"真的跨过了一道门槛，现在我跟 ChatGPT 说话比打字多"；反思"过去12个月不是我们最好的12个月，主要是我的责任，但接下来将是史上最好的12个月"
- @thsottiaux（OpenAI，Sam 转）：**回应 GPT-5.6 删文件**——已调查数起报告，最常见于（特定用户操作条件下）触发；并对新版 ChatGPT 桌面 App 收集反馈后做了调整
- @GoogleDeepMind：与 Isomorphic Labs 合作应对生物安全，部署 AI 应对未来疫情

**Bluesky KOL**（本日多聚焦 Kimi K3 实测，观点分化）：
- Ethan Mollick：K3 让开源权重再次逼近前沿，但复杂统计审计中"K3 Max 出了不少错，包括误用统计方法"；并把 K3 加入其"程序化生成港口小镇"一次成型基准（与 GPT-5.6 Pro/Fable/Inkling 同台）；调侃 K3（和所有模型一样）写不好谋杀悬疑
- Simon Willison：发布 Kimi K3 笔记 + 对"鹈鹕基准"局限的反思
- John Carmack：吐槽 Claude 在被质疑一处 clamp 必要性时"低调地阴阳怪气"了他一把

**Hacker News 高分讨论**：
- [1257分/792评论] [Kimi K3: Open Frontier Intelligence](https://www.kimi.com/blog/kimi-k3)
- [295分/212评论] [至少 105 位前 YC 创始人曾在 OpenAI 和 Anthropic 工作过](https://joinedanthropic.com)
- [262分/131评论] [NotebookLM 改名 Gemini Notebook](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/)
- [200分/205评论] [LLM 批评者是对的，但我照用不误](https://www.theocharis.dev/blog/llm-critics-are-right-i-use-llms-anyway/)
- [178分/67评论] [LM Studio Bionic：面向开源模型的 AI Agent](https://lmstudio.ai/blog/introducing-lm-studio-bionic)
- [163分/112评论] [用"经典"机器学习检测 LLM 生成文本](https://blog.lyc8503.net/en/post/llm-classifier/)
- [160分/171评论] [100 美元 AI 音乐视频：Claude Fable 5 vs GPT-5.6 Sol](https://www.tryai.dev/blog/ai-music-video-arena-claude-vs-gpt-5.6)
- [104分/55评论] [用 6GB 显存的旧 Linux 桌面训练生成式 AI 底鼓模型](https://www.zhinit.dev/blog/training-a-kick-drum-diffusion-model)

## 🇨🇳 中文圈热点

**微博**
- [热搜#3·97万·新] 世界人工智能大会今天开幕（详见"今日焦点"）
- [热搜#18·48万] [Kimi K3参数达2.8万亿](https://s.weibo.com/weibo?q=%23Kimi%20K3%E5%8F%82%E6%95%B0%E8%BE%BE2.8%E4%B8%87%E4%BA%BF%23) · [热搜#50·新] KimiK3发布

**知乎**
- [热榜#7·192万] Kimi K3 开源模型评价（详见"今日焦点"）
- [热榜#10·184万] [美国团队用宇树 G1 人形机器人完成活猪胆囊切除，Nature 论文，含金量几何](https://www.zhihu.com/question/2060754085637271982)
- [热榜#22·147万] 努比亚全球首款 AI 智能体手机 NaviX Ultra（详见"公司与行业动态"）

**抖音/头条/百度热榜**
- [抖音#3] AI站稳产业圈顶流C位 · [抖音#6] 人形机器人格斗赛诞生躺赢名场面 · [头条#13] 全球最大规模开源模型Kimi K3发布 · [百度#10] 国内芯片龙头办公室遭韩国检方搜查

**B站**
- [1002万播放] [孩子总把网络烂梗挂嘴边怎么办？【AI全民制作人】](https://www.bilibili.com/video/BV1oxNA6SE8k)
- [267万播放] [假如你在一个十万人宿舍查寝【AI全民制作人】](https://www.bilibili.com/video/BV1UFN264ETi)
- [130万播放] [原创AIGC剧集《有异人》【AI全民制作人】](https://www.bilibili.com/video/BV1psN86KEt5)

**量子位/雷锋网**（未归入其他板块）
- [逐际动力放出Demo，Figure：睡不着啊——不要赌某个模型能通吃一切](https://www.qbitai.com/2026/07/451084.html)
- [一位失忆患者，揭开了AI记忆的误区——记忆能够独立成层](https://www.qbitai.com/2026/07/451049.html)
- [挚达科技发布"AI能源+机器人"家庭及公共场景自动充电机器人方案](https://www.leiphone.com/category/transportation/lV4IbRbkPa4Urphm.html)

**掘金 AI 热榜**（开发者社区，节选高阅读量）
- [3138阅读] [不自己造轮子：在小艺开放平台搭一个真实的健康小助手](https://juejin.cn/post/7662376768221364233)
- [3037阅读] [一键还原任意网站，这套Playwright+多Agent工程流太猛了](https://juejin.cn/post/7661439504077176847)
- [2111阅读] [七月，一个德国开发者在评论区甩了个链接](https://juejin.cn/post/7661915632607625225)
- [1806阅读] [图解120个大语言模型（LLM）核心概念（1-30）](https://juejin.cn/post/7660708287620808739)
- [1491阅读] [AI编程普及，初学者还要不要学习基础语法？](https://juejin.cn/post/7661117411174350890)
- [1342阅读] [从5万次到日均2000万次调用：大模型推理服务的性能工程实践](https://juejin.cn/post/7660697495832035362)
- [1078阅读] [Grok4.5发布，马斯克终于上桌了！Cursor功不可没～](https://juejin.cn/post/7660359043139731496)
- [1021阅读] [耗时7天，我们开源了腾讯WorkBuddy实战蓝皮书](https://juejin.cn/post/7661324464743858219)
- [880阅读] [Hy3 + WorkBuddy = 国产顶级Agent（附完整提示词）](https://juejin.cn/post/7660755249066344490)
- [816阅读] [ChatGPT取消5小时限额，Codex终于可以疯狂造起来了！](https://juejin.cn/post/7661754132201586723)
- [681阅读] [看了微软几万人用AI编程的数据——效率涨24%的代价没人提](https://juejin.cn/post/7662245660751396891)
- [550阅读] [Claude Fable 5提示词泄漏，抓紧学习下](https://juejin.cn/post/7661117411174105130)
- [477阅读] [女朋友想要专属桌宠？我用AI提示词，1小时把照片变成57帧动画精灵](https://juejin.cn/post/7661821409980760099)
- [469阅读] [曾经人手一个的Superpowers，为什么现在都在卸](https://juejin.cn/post/7662691781214437412)

---

## ⚠️ 本次异常源

- 全部 25 个源本次窗口内均正常，无异常（mit_tr 本窗口 0 条匹配，非抓取失败）
