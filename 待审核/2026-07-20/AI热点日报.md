# AI 热点日报 · 2026-07-20（前 24h，共 143 条，25/25 源正常）

> 周日，海外源（HF Papers / 官方博客 / X 转发 / MIT TR 等）多为空档，条目偏少；开源模型军备竞赛 + WAIC 收官占据主导。

## 🔥 今日焦点（跨源同报的大事）

- **阿里发布 Qwen 3.8 Max 预览版：2.4 万亿参数，自称"仅次于 Fable 5"、承诺"即将开源权重"，正面接招 Kimi K3**（多源同报：HN 首页 808分/564评论、Techmeme头条、The Decoder）。Bloomberg 报道阿里推出 Qwen3.8 Max 预览版，称其比肩前沿模型、仅次于 Claude Fable 5，多模态、计划"即将开源权重"。这被视作对 Kimi K3 的直接回应，中国开源大模型军备竞赛白热化。 | [HN/Qwen](https://twitter.com/Alibaba_Qwen/status/2078759124914098291) [Techmeme](https://www.techmeme.com/260719/p7#a260719p7) [The Decoder](https://the-decoder.com/alibabas-qwen-takes-on-kimi-k3-with-open-weight-qwen-3-8-says-model-is-second-only-to-fable-5/)

- **Kimi K3 需求暴涨压垮算力，月之暗面宣布暂停 C 端新用户订阅；同时被曝筹备赴港 IPO（6 月 ARR 已达 3 亿美元）**（多源同报：Techmeme头条×2、HN 237分、IT之家、知乎热榜#6·389万、微博热搜#12、掘金实测）。官方公告称过去 48 小时用户请求量逼近集群承载极限，暂停新订阅以保障已有用户；Bloomberg 补充其 ARR 从 4 月 2 亿美元涨到 6 月 3 亿美元，最快 6 个月内赴港上市。The Decoder 实测指出 K3 前端代码大幅领先 Fable 5，但复杂数学仍差距明显。 | [Techmeme·暂停订阅](https://www.techmeme.com/260719/p11#a260719p11) [知乎](https://www.zhihu.com/question/2062310754481656074) [IT之家](https://www.ithome.com/0/978/808.htm) [The Decoder·数学差距](https://the-decoder.com/moonshots-kimi-k3-outperforms-fable-5-in-frontend-code-but-lags-far-behind-in-complex-math/)

- **Hugging Face 遭 Agentic AI 入侵数据管线，多个内部集群与凭证被访问；讽刺的是取证时因美国前沿模型安全护栏被拒，改用开源 GLM-5.2 完成溯源**（2 源同报：Techmeme头条×2）。HF 称一套 agentic AI 系统攻破其数据管线，靠自家 AI 分诊系统发现入侵；事后做泄露取证时，美国前沿模型的安全护栏拦截了相关请求，HF 转而用自托管的开源 GLM-5.2 完成 forensics——成为"开源模型补位闭源安全过度拦截"的标志性案例。 | [Techmeme·被入侵](https://www.techmeme.com/260719/p12#a260719p12) [Techmeme·GLM取证](https://www.techmeme.com/260719/p13#a260719p13)

- **WAIC 2026 收官，工信部披露上半年 AI 硬数据：智能算力规模达 2185 EFLOPS、规上制造业 AI 应用普及率超 30%、人形机器人整机超全球半数**（多源同报：36氪多条、微博热搜#3·243万、头条热榜#3、量子位/雷锋网全景）。国新办发布会公布：四足机器人占全球销量近 70%、人形机器人整机 400 余款超全球半数；将加快出台"人工智能+软件"行动方案、印发算力标准体系建设指南。 | [36氪·2185EFLOPS](https://36kr.com/newsflashes/3903375424522113?f=rss) [36氪·人形机器人超半数](https://36kr.com/newsflashes/3903383107110785?f=rss) [微博](https://s.weibo.com/weibo?q=%23%E4%B8%AD%E5%9B%BD%E6%88%90%E4%B8%BA%E5%85%A8%E7%90%83AI%E5%8F%91%E5%B1%95%E4%B8%8E%E6%B2%BB%E7%90%86%E5%85%B3%E9%94%AE%E5%8A%9B%E9%87%8F%23)

- **世界人工智能合作组织正式签署：29 国成为创始成员国，总部设上海、鼓励共建开源生态**（续前日，多源同报：IT之家、微博、36氪）。《关于成立世界人工智能合作组织的协定》签署仪式 16 日在上海举行，来自亚非拉欧的 29 国现场签署。 | [IT之家](https://www.ithome.com/0/978/797.htm)

- **Claude Code 已改用"用 Rust 重写的 Bun"，OpenAI Codex 上下文从 372k 砍到 272k**（HN 双热点：413分/576评论、328分/156评论）。Simon Willison 发现已安装 Claude Code 的用户实际在运行"用 Rust 重写的未发布版 Bun"；同时 OpenAI Codex 一个 PR 把模型上下文从 372k 缩到 272k 引发讨论。 | [HN/Bun](https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/) [HN/Codex](https://github.com/openai/codex/pull/33972/files)

---

## 🚀 模型与产品发布

- 面壁智能联合 OpenBMB 发布端侧模型 **MiniCPM5-2B**，AA-Index 榜单 4B 以下性能第一，已完成多款芯片适配 | [IT之家](https://www.ithome.com/0/978/796.htm)
- 黎曼动力发布 **Riemann-1.0**：看 20 万小时"人类干活实录"训练机器人 | [量子位](https://www.qbitai.com/2026/07/454592.html)
- 上海 AI Lab 让 Harness 自进化：不换模型、效果提升 104%（Harness 本身可被搜索、验证、迭代）| [量子位](https://www.qbitai.com/2026/07/454441.html)
- 腾讯混元 Hy3 限免活动延长至 8 月 5 日（应用户"再来两周"呼声，面向 WorkBuddy/CodeBuddy 用户）| [IT之家](https://www.ithome.com/0/978/865.htm)
- 腾讯云智能体开发平台 **ADP 4.0 海外版**发布，升级智能工作台/Claw 模式/Skill 广场，正式出海 | [36氪](https://36kr.com/p/3901396207584902?f=rss)
- Google DeepMind **GenCeption**：论证"视频生成器已内含计算机视觉缺失的世界模型"，用更少数据做深度估计/分割达 SOTA | [The Decoder](https://the-decoder.com/google-deepmind-argues-video-generators-already-contain-the-world-models-computer-vision-has-been-missing/)
- 千里科技公布 ASD 4.1 技术预览（零断点全场景 D2D 通行），阶跃 Step AOS 将上车、年底推 ASD 5.0 | [IT之家](https://www.ithome.com/0/978/803.htm)
- 润科具能发布全球首款"半人马"轮足复合机器人（自主巡检/消防应急）| [IT之家](https://www.ithome.com/0/978/833.htm)
- HF Trending 新上榜：[baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)（趋势分232）、[Wan-AI/Wan-Dancer-14B](https://huggingface.co/Wan-AI/Wan-Dancer-14B)

## 🏢 公司与行业动态

- 鸿海首度夺下 SpaceX AI 服务器代工订单，总价高达 520 亿美元（马斯克拟新建超 1.3 万个 GB300 机柜）| [IT之家](https://www.ithome.com/0/978/843.htm)
- 百度昆仑芯 M100 实物首次公开亮相（面向大模型推理优化，延续自研 XPU）| [IT之家](https://www.ithome.com/0/978/920.htm)
- 摩尔线程 MTT C256 超节点亮相，把 256 张 GPU 变成一台计算机；爱芯元智元曦系列 A 系列推理卡算力超 1000 TOPS（2 条）| [IT之家·摩尔线程](https://www.ithome.com/0/978/856.htm) [IT之家·爱芯](https://www.ithome.com/0/978/841.htm)
- 奇异摩尔国产 GPU 直通方案实测：不靠英伟达网卡，吞吐飙升、延迟砍半 | [量子位](https://www.qbitai.com/2026/07/454932.html)
- 工信部：将加快出台"人工智能+软件"行动方案、印发算力标准体系建设指南（推动算力市场化定价）| [36氪·软件](https://36kr.com/newsflashes/3903399623542657?f=rss) [36氪·算力标准](https://36kr.com/newsflashes/3903384861771649?f=rss)
- 中央网信办启动为期 4 个月"清朗·未成年人网络保护"专项行动，整治利用 AI 恶搞经典动画形象的"毒动画" | [IT之家](https://www.ithome.com/0/978/922.htm)
- 欧洲议会拟最快 9 月上线 EPGenAI Hub，向议员及工作人员提供 Meta/OpenAI/Anthropic/Mistral 模型 | [Techmeme](https://www.techmeme.com/260719/p18#a260719p18)
- 非营利组织 Current AI（4 亿美元承诺，含法国 1 亿）冲刺建"人人免费的 AI 万维网"（2 源同报）| [Techmeme](https://www.techmeme.com/260719/p14#a260719p14) [TechCrunch](https://techcrunch.com/2026/07/19/nonprofit-current-ai-is-racing-to-build-the-world-wide-web-of-ai-free-for-all/)
- WSJ：多数公司用便宜模型省 AI 成本，Shopify 却反其道全押前沿模型、禁止工程师用其他 | [Techmeme](https://www.techmeme.com/260719/p10#a260719p10)
- FT：AI 正重塑专业服务业初级岗位——公司在重新设计招聘/培训/文化，而非简单砍初级岗 | [Techmeme](https://www.techmeme.com/260719/p6#a260719p6)
- 分析：OpenAI 与 Anthropic 员工的政治献金比 Google/Meta/Airbnb 上市后员工更集中、更活跃 | [Techmeme](https://www.techmeme.com/260719/p4#a260719p4)
- 红熊 AI 完成数亿元 A+ 轮（投后近 30 亿元），15 个月内第 6 轮，基于 AI"记忆科学"从 To B 延伸 To C | [36氪](https://36kr.com/p/3899612612494976?f=rss)
- 黄仁勋日本行影响持续（横跨日本整个科技生态的合作）；其皮夹克拍出 96 万美元天价 | [TechCrunch](https://techcrunch.com/2026/07/19/what-to-watch-for-after-jensen-huangs-japan-visit/)
- 全美出现数据中心出售潮，"反数据中心运动"向红蓝州同时蔓延（知乎热榜#13·138万）| [知乎](https://www.zhihu.com/question/2062127994513183627)
- 海尔承建全国首个家居家电方向国家人工智能应用中试基地 | [IT之家](https://www.ithome.com/0/978/839.htm)
- GPT-5.6 删文件续报：某 AI 初创老板"痛失整台 Mac"（量子位）| [量子位](https://www.qbitai.com/2026/07/454689.html)
- 苹果砍 Mac Pro 前曾秘密开发英特尔新机型与 M2/M3 Extreme 芯片（古尔曼）| [IT之家](https://www.ithome.com/0/978/829.htm)
- 商汤大装置与国信数算共建全国一体化算力网试验场 | [量子位](https://www.qbitai.com/2026/07/454771.html)

## 🔓 开源项目与模型

**GitHub Trending**
- [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)（今日+1734星）— 李博杰《深入理解 AI Agent：设计原理与工程实践》全书正文+PDF+配套代码开源
- [sponsors/tirth8205](https://github.com/sponsors/tirth8205)（+663星）— 面向 MCP/CLI 的本地优先代码智能图谱
- [jamiepine/voicebox](https://github.com/jamiepine/voicebox)（+610星）— 开源 AI 语音工作室（克隆/听写/创作）
- [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo)（+595星）— 面向 AI 编程 Agent 的本地优先 web 搜索/抓取（MCP，$0/query）
- [PostHog/posthog](https://github.com/PostHog/posthog)（+411星）— AI 可观测性/分析平台
- [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli)（+410星）— Kimi Code CLI 官方 Agent（随 K3 热度上涨）
- [kvcache-ai/ktransformers](https://github.com/kvcache-ai/ktransformers)（+360星）— 异构 LLM 推理/微调优化框架
- [sponsors/lyogavin](https://github.com/sponsors/lyogavin)（+358星）— AirLLM：单张 4GB GPU 跑 70B 推理
- [Canner/WrenAI](https://github.com/Canner/WrenAI)（+121星）— 面向 AI Agent 的 GenBI（自然语言→可信 SQL/仪表盘）
- [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot)（+83星）— 多 IM 平台 AI Agent 助手/开发框架

**HuggingFace Trending**（节选）
- [thinkingmachines/Inkling](https://huggingface.co/thinkingmachines/Inkling)（趋势分1113·1158赞，连续登顶）
- [prism-ml/Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)（趋势分760）+ [Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)（趋势分487）— 可塞进 iPhone 的 27B 推理模型持续霸榜
- [zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)（趋势分253·4172赞，本日因 HF 取证事件更受关注）
- [baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)（趋势分232·2199赞，新上榜）
- [ATH-MaaS/OvisOCR2](https://huggingface.co/ATH-MaaS/OvisOCR2)（趋势分193）
- 注：Kimi K3、Qwen 3.8 权重均未在本日 HF 上榜（K3 承诺 7/27 开源、Qwen3.8"即将开源"）；其余为社区二创微调，未单独展开

## 📄 研究论文（HF Daily Papers）

- 本次抓取窗口内 HF Daily Papers 源返回 0 条（周末更新空档，非抓取失败），明日恢复跟进。相关研究可见"模型与产品发布"板块的 Google DeepMind GenCeption。

## 💬 KOL 与社区热议

**smol.ai**：本期站点仍为 7/16-17 期"平静的一天"综述（未更新至最新一期），暂不展开。

**Bluesky KOL**（本日聚焦 Kimi K3、中国实验室与能力曲线）：
- Ethan Mollick：① "大家太纠结于当下格局（谁领先、怎么控成本），却没足够关注能力曲线仍在持续陡增"；② 让 Kimi K3"认真想两首适用于当前生成式AI的非流行诗"，思维链长达 32 页
- Simon Willison：证实"装了 Claude Code 就在跑用 Rust 重写的未发布 Bun"，给出两条自查命令
- Nathan Lambert：若 Kimi K3 让你终于想理解中国实验室怎么做 AI、与旧金山权力中心有何不同，推荐读其新文

**Hacker News 高分讨论**：
- [808分/564评论] [Qwen 3.8](https://twitter.com/Alibaba_Qwen/status/2078759124914098291)
- [413分/576评论] [Claude Code 现在用 Rust 写的 Bun](https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/)
- [328分/156评论] [OpenAI 把 Codex 模型上下文从 372k 砍到 272k](https://github.com/openai/codex/pull/33972/files)
- [294分/163评论] [研究：AI 建议让人更不准确却更自信](https://thenextweb.com/news/ai-advice-suppresses-critical-thinking-wrong-answers-study)
- [237分/97评论] [月之暗面因 Kimi K3 需求暂停新订阅](https://twitter.com/kimi_moonshot/status/2078855608565207130)
- [29分] [Anthropic 用 Claude Code 跑大规模代码迁移](https://claude.com/blog/ai-code-migration)
- 相关警示研究（The Decoder）：① AI 文本检测器在"模仿作者风格"时最多 18% 漏检；② 放射科 AI 读 X 光"错得很自信"（RadLE 2.0 基准）| [The Decoder·检测器](https://the-decoder.com/ai-text-detectors-struggle-when-language-models-mimic-an-authors-style/) [The Decoder·X光](https://the-decoder.com/ai-chatbots-reading-x-rays-can-be-dangerously-confident-even-when-theyre-wrong/)

## 🇨🇳 中文圈热点

**微博 / 知乎 / 抖音头条**
- [微博热搜#3·243万·新] [中国成为全球AI发展与治理关键力量](https://s.weibo.com/weibo?q=%23%E4%B8%AD%E5%9B%BD%E6%88%90%E4%B8%BA%E5%85%A8%E7%90%83AI%E5%8F%91%E5%B1%95%E4%B8%8E%E6%B2%BB%E7%90%86%E5%85%B3%E9%94%AE%E5%8A%9B%E9%87%8F%23)
- [微博热搜#12·52万·新] Kimi K3引发算力逻辑讨论 · [微博热搜#49·新] 第一次见AI把自己卸载了（AI删文件梗延续）
- [知乎热榜#6·389万] [如何看待月之暗面Kimi宣布算力紧张暂停会员开放](https://www.zhihu.com/question/2062310754481656074)
- [知乎热榜#13·138万] [全美数据中心出售潮，"反数据中心运动"向红蓝州蔓延](https://www.zhihu.com/question/2062127994513183627)
- [头条热榜#3] [2026世界人工智能大会硬核瞬间](https://www.toutiao.com/trending/7664429615074725403/)

**量子位 / 雷锋网 / 36氪**（WAIC 收官现场）
- [逛了趟WAIC，AI在物理世界都快卷疯了——AI圈春晚](https://www.qbitai.com/2026/07/454802.html)
- [冷门的哲学，成了"治"AI的热门](https://www.qbitai.com/2026/07/455041.html)
- [谁还在卷参数？WAIC2026全是能干活的实体AI](https://36kr.com/p/3903383663478403?f=rss)
- [从烤披萨到拿快递，满场跑的机器人终于要进你家了｜WAIC全面探展](https://36kr.com/p/3902007640459145?f=rss)
- [在WAIC地下一层找机会的年轻人：光鲜是过去，眼下是生存](https://36kr.com/p/3903396279125888?f=rss)
- [对话商汤林达华：多模态是Coding之后的下一个战场](https://www.leiphone.com/category/yanxishe/uHHqpDWEcbFxyyvD.html)

**B站**
- [308万播放] [原创AIGC剧集《有异人》【AI全民制作人】](https://www.bilibili.com/video/BV1psN86KEt5)
- [110万播放] [和AI玩猜历史人物，惨遭戏耍的一集](https://www.bilibili.com/video/BV1dnNY6vEeN)

**掘金 AI 热榜**（开发者社区，节选高阅读量）
- [6337阅读] [不自己造轮子：在小艺开放平台搭一个真实的健康小助手](https://juejin.cn/post/7662376768221364233)
- [3893阅读] [曾经人手一个的Superpowers，为什么现在都在卸](https://juejin.cn/post/7662691781214437412)
- [2386阅读] [七月，一个德国开发者在评论区甩了个链接](https://juejin.cn/post/7661915632607625225)
- [1343阅读] [用Kimi K3交付一个真实项目后：很强，但还有不足](https://juejin.cn/post/7663313773420462118)
- [1295阅读] [Harness企业级落地(二)-让AI读懂项目](https://juejin.cn/post/7662586328122982415)
- [885阅读] [看了微软几万人用AI编程的数据——效率涨24%的代价没人提](https://juejin.cn/post/7662245660751396891)
- [550阅读] [曾经狂推的Superpowers，今天我终于把它卸载了！臃肿，Token吞金兽](https://juejin.cn/post/7662933531113324586)
- [532阅读] [Memory系统全面横评：谁让Agent具备更强长期智能](https://juejin.cn/post/7662194686455349258)
- [432阅读] [全网都在吹的Kimi K3，到底怎么样](https://juejin.cn/post/7663685196478611506)
- [481阅读] [DeepSeek实习生日薪5500：真正恐怖的不是工资](https://juejin.cn/post/7662694676458307622)

---

## ⚠️ 本次异常源

- 全部 25 个源均正常抓取，无失败。
- 其中 **hf_papers、vendor_blogs、zpravobot(官方号推文)、mit_tr、arstechnica、producthunt** 本窗口返回 0 条——为周末 RSS/更新空档（源健康、非抓取错误），明日恢复。
