<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub AI 项目：围绕大模型的"外围工具"成为关注焦点
2. system_prompts_leaks 登上今日 Trending，另两个 AI 工具同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时合计新增超 2,200 star
当前使用：候选 1
-->

# 今日 GitHub AI 项目：三个大模型"外围工具"登上日榜

> 今天日榜上 AI 相关项目的共同点，是都不做模型本身，而是围着现有大模型转：一个记录各家模型的系统提示词，一个把大模型接进 Unity，一个改进大模型生成的前端界面。它们分别对应了透明度、集成和产出质量三个方向，都值得关注。

---

## 1. system_prompts_leaks — 收集各家 AI 聊天机器人的系统提示词

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 50.1k | 981 | JavaScript | CC0-1.0 |

这个仓库做的事很具体：把 Claude、ChatGPT、Gemini 等主流 AI 聊天机器人的系统提示词（system prompt）整理归档，按厂商和模型分门别类地放在一起，方便查阅和对比。README 里列出了 Anthropic、OpenAI、Google、xAI、Microsoft 等多家的条目，并给出了不同模型版本之间提示词的 diff 链接。

对使用者来说，系统提示词平时是看不到的那部分指令，决定了模型的语气、边界和默认行为。把这些内容集中记录下来，可以用于研究提示词工程、对比不同厂商的设计取舍，也可以作为教学材料。仓库采用 CC0-1.0 协议，内容可自由取用。README 顶部标注该项目曾被《华盛顿邮报》报道。

这个项目适合做提示词研究、想了解主流模型默认行为的开发者，以及做 AI 教学的人参考。需要注意的是，提示词会随模型迭代变化，仓库里的版本是某个时间点的快照。

🔗 项目地址：https://github.com/asgeirtj/system_prompts_leaks

---

## 2. unity-mcp — 用自然语言操作 Unity 编辑器的 MCP 桥接层

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 12k | 414 | C# | MIT |

unity-mcp 解决的问题是把大模型接到 Unity 游戏引擎里。它基于 Model Context Protocol（MCP），在 AI 助手和 Unity 编辑器之间搭了一座桥，让模型可以创建场景和 GameObject、编辑 C# 脚本、管理资源、运行测试和构建工程。README 说明当前提供 47 个 MCP 工具入口。

和直接在编辑器里手动操作相比，它的差异在于接入方式：项目兼容任意 MCP 客户端，包括 Claude Desktop、Codex、Cursor、VS Code 等，配置后可以用一句"在原点创建一个立方体并加上刚体"这样的自然语言指令来驱动编辑器。项目要求 Unity 2021.3 LTS 到 6.x、Python 3.10+，v10.0.0 于 2026-06-30 发布。

这个项目已有规模，适合想在游戏开发流程里试验 AI 辅助的 Unity 开发者，以及研究 MCP 如何接入具体桌面软件的人。协议为 MIT。

🔗 项目地址：https://github.com/CoplayDev/unity-mcp

---

## 3. taste-skill — 改进 AI 生成前端界面的 Agent Skill 集合

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 57.7k | 863 | JavaScript | MIT |

taste-skill 针对的是一个具体痛点：AI 生成的前端界面常常看起来千篇一律、缺乏设计感。它以 Agent Skills 的形式，给模型补充关于布局、排版、动效和间距的规则，目标是让 AI 产出的 UI 不那么"模板化"。README 里把这个方向称作 "anti-slop"（对抗平庸产出）。

在用法上，它兼容 Vercel 的 agent-skills 体系，通过 `npx skills add` 安装，也可以把单个 SKILL.md 直接复制进项目或粘贴给 ChatGPT、Codex、Claude Code 使用。仓库还附带用于生成参考图板的 image-generation skills，可配合图像生成工具产出设计参考，再交给编码工具实现。项目创建于 2026 年 2 月，目前默认 skill 已迭代到 v2（标注为实验版）。

这个项目适合用 AI 写前端、但对成品观感不满意的开发者，以及想了解 Agent Skill 如何约束模型输出风格的人。需要说明的是，README 中提醒该项目没有任何官方代币或加密项目，谨防冒名。

🔗 项目地址：https://github.com/Leonxlnx/taste-skill

---

## 今日观察

今天日榜上的三个 AI 项目，没有一个是在训练新模型，都是围绕现有大模型做外围工作：一个提高模型行为的透明度，一个把模型接进具体软件，一个改进模型的产出质量。这也反映出当下开源社区的一部分注意力，正从"造模型"转向"怎么把已有模型用好"。三者方向各异，放在一起看更像是同一生态里的不同切面。

---

**Tags**：#GitHub热点 #AI开源 #提示词工程 #MCP #AgentSkill
