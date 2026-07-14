<!--
标题候选：
1. 今日 GitHub AI 热点：虚拟陪伴、开发方法论与技能包同时登场
2. AIRI 登上今日 GitHub Trending，另两个项目同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时合计新增超 900 star
当前正在使用：候选 1
-->

# 今日 GitHub AI 热点：虚拟陪伴、开发方法论与技能包同时登场

> 今天的 GitHub AI 类 Trending 呈现出三条不同路径：虚拟陪伴角色、规格驱动开发、营销技能包。三者的共同点是都在给大模型接上更具体的应用场景。

---

## 1. airi — 自部署的开源虚拟陪伴角色

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 42k | 78 | TypeScript | MIT |

AIRI 想做的是一个用户自己托管的长期陪伴虚拟角色：把语音识别、语音合成、大语言模型对话和 Live2D/VRM 形象绑定在一起，让角色能实时对话、做出表情动作，甚至进 Minecraft、Factorio 陪玩家一起玩。项目 README 直接写明，目标是复刻 Neuro-sama 这类虚拟主播的路径，但完全开源、可自行部署。

和常见的单一聊天机器人不同，AIRI 把大模型接入做成可插拔层，支持 OpenAI、Anthropic Claude、DeepSeek、Ollama、vLLM 等十余种模型来源；语音合成接了 ElevenLabs、Azure Speech、阿里云和本地 Kokoro TTS 多个后端，用户可按需替换任意一环。形象层同时支持 Live2D 和 VRM 两种格式，并做了浏览器端和 PWA 适配。

适合想搭建个人虚拟角色、对隐私和自部署有要求的开发者。VRM 舞台、游戏联动等功能目前仍标注为进行中。

🔗 项目地址：https://github.com/moeru-ai/airi

---

## 2. Spec Kit — 用规格说明驱动 AI 编程的工具包

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 120.7k | 543 | Python | MIT |

Spec Kit 由 GitHub 官方维护，解决的问题很具体：用 AI 编码助手写代码时，需求常停留在口头描述里，规格写完就被丢在一边。Spec Kit 让规格说明本身变成可执行文档——先用 `/speckit.constitution` 定项目原则，再用 `/speckit.specify` 说清楚做什么、为什么做，由此生成实现计划和任务列表，交给 AI 编码助手落地。

相比直接把需求扔给模型生成代码，Spec Kit 把流程拆成 constitution、specify、plan、tasks、implement 五个阶段，每步产出的文档都可被人审阅、修改后再进入下一步。它不绑定单一模型或 IDE，官方列出的集成对象超过 30 个，包括 GitHub Copilot、Claude Code 等主流 AI 编码代理，统一通过 Specify CLI 初始化项目。

作为头部开源项目，Spec Kit 适合需要给 AI 生成代码留痕、留审阅记录的团队，也适合个人开发者在动手写代码前先理清思路。

🔗 项目地址：https://github.com/github/spec-kit

---

## 3. marketingskills — 面向 AI 编码助手的营销技能包

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 38.7k | 299 | JavaScript | MIT |

marketingskills 要解决的不是写代码，而是把营销从业者的专业知识喂给 AI 编码助手。作者 Corey Haines 把 SEO、转化率优化、文案、广告投放、增长复盘等近 50 个营销子领域写成 Markdown 技能文件，装进 Claude Code、Cursor 这类支持 Agent Skills 规范的工具，让代理处理营销任务时能调用对应框架，而不是泛泛而谈。

这类技能包和传统营销工具的差异在于：不提供界面或自动化流程，只提供结构化知识和判断逻辑，技能之间还互相引用——比如 product-marketing 技能会被其他所有技能优先读取，用来先弄清楚产品、受众和定位。安装方式做了适配，可用 `npx skills` 按需选取部分技能，也可作为 Claude Code 插件市场里的插件整体安装。

适合独立开发者、没有专职营销人员的初创团队，需要 AI 编码助手协助处理增长相关工作的场景。

🔗 项目地址：https://github.com/coreyhaines31/marketingskills

---

## 今日观察

今天入选的三个项目分别落在虚拟陪伴、开发方法论和垂直技能包三个方向，共同点是都在给"AI 编码助手"做延伸——接入角色形象、给流程立规矩、给代理喂专业知识，思路都是让通用大模型在具体场景里更好用。

---

**Tags**：#GitHub热点 #AI开源 #AI陪伴 #SpecDrivenDevelopment #AgentSkills
