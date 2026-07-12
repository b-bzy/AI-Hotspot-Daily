<!--
标题候选：
1. 今日 GitHub AI 热点：编程 agent 生态持续整合
2. OpenAI Codex 插件登陆 Claude Code，今日 GitHub AI 热点一览
3. 今日 GitHub AI 热点：3 个项目 24 小时新增超 1200 star
当前使用：候选 1
-->

# 今日 GitHub AI 热点：编程 agent 生态持续整合

> 今天的 GitHub Trending 日榜上，OpenAI 和 Anthropic 的产品线出现同框：一个官方插件把 Codex 接入了 Claude Code，Claude Code 本身持续增长，Agent Skills 则在给这套生态定义统一的技能格式。

---

## 1. openai/codex-plugin-cc — 让 Claude Code 直接调用 Codex 做代码审查的官方插件

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 23.3k | 634 | JavaScript | Apache-2.0 |

这个插件解决的问题很具体：让已经习惯用 Claude Code 的开发者，不用跳出当前工作流，就能在同一个终端里调用 OpenAI 的 Codex 做代码审查，或者把某个任务转交给 Codex 后台处理。

插件提供 `/codex:review` 做只读代码审查，以及支持自定义关注点的 `/codex:adversarial-review`，专门用来挑战已经做出的技术决策；还有 `/codex:rescue`、`/codex:transfer` 等命令用于会话转移和后台任务管理。使用时需要 ChatGPT 订阅或 OpenAI API key，相当于把 OpenAI 和 Anthropic 两家的编程 agent 接到了同一个工作流里。

适合已经把 Claude Code 当主力工具、又想引入 Codex 做第二方代码审查的开发者。

🔗 项目地址：https://github.com/openai/codex-plugin-cc

---

## 2. anthropics/claude-code — 跑在终端里的 Anthropic 官方编程 agent

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 135.9k | 221 | Python | — |

Claude Code 解决的问题很具体：让开发者不用离开终端就能完成大部分编码相关的杂事——理解整个代码库上下文、执行常规任务、解释复杂逻辑、处理 git 工作流，都通过自然语言指令完成。

作为 Anthropic 官方维护的 CLI 工具，项目从 2025 年 2 月开源至今累计了 13.5 万+ star。除了终端命令行，它也可以装进 IDE，或者在 GitHub 上通过 @claude 直接触发。仓库还内置插件目录，支持扩展自定义命令和 agent——今天登陆的 Codex 插件就是其中之一。

适合已经在使用 Claude 模型、想把代码库理解和常规编码任务交给 agent 处理的开发者。

🔗 项目地址：https://github.com/anthropics/claude-code

---

## 3. agentskills/agentskills — 给 AI agent 添加技能的开放规范

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 22k | 406 | Python | Apache-2.0 |

Agent Skills 是一套开放格式，用一个包含 SKILL.md 的文件夹给 AI agent 打包"专业技能"——具体的操作步骤、参考资料、脚本和模板，让 agent 在遇到匹配任务时才把完整说明加载进上下文。

项目采取"渐进式加载"三段式设计：agent 启动时只读每个技能的名称和一句话描述，匹配到任务才读入完整 SKILL.md，执行时才按需调用脚本或引用文件，这样即使挂载几十个技能也不会占满上下文窗口。该规范由 Anthropic 最初开发并开源，目前已被多个 agent 产品采用。

适合需要把团队内部流程、行业知识沉淀成可复用"agent 技能包"的团队，也适合在做多 agent 产品、需要统一技能格式的开发者。

🔗 项目地址：https://github.com/agentskills/agentskills

---

## 今日观察

今天的三个项目连成了一条线：OpenAI 官方给 Claude Code 做了一个 Codex 插件，Claude Code 自身的插件生态持续增长，而 Agent Skills 正在给"agent 能力如何打包"这件事定标准。编程 agent 之间的边界，正在变得越来越模糊。

---

**Tags**：#GitHub热点 #AI开源 #ClaudeCode #Codex #AgentSkills
