<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub 日榜：AI 编码 agent 的"工程化"成为主线
2. YC 总裁的 Claude Code 配置 gstack 登顶今日 Trending，另两个项目同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时合计新增超 2,700 star
当前使用：候选 1
-->

# 今日 GitHub 日榜：AI 编码 agent 的"工程化"成为主线

> 今天 Trending 日榜排在前面的项目方向相当集中，都在解决同一件事：怎么把 AI 编码 agent 从"对话式打草稿"变成一套可复用的固定流程。下面这三个分别覆盖了研发流水线、常驻智能体和逆向建站三个场景，数据和形态都对得上，值得看。

---

## 1. gstack — 把 Claude Code 配置成一支"虚拟工程团队"的工作流

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 114k | 1,011 | TypeScript | MIT |

gstack 是 Y Combinator 总裁 Garry Tan 公开出来的个人 Claude Code 配置。它解决的问题很具体：把原本零散的 AI 编码过程，固定成一条从想法到上线的研发流水线。仓库创建于 2026 年 3 月，目前总 star 已过 11 万，属于近期关注度较高的 Claude Code 项目之一。

和直接裸用 Claude Code 相比，gstack 把研发流程拆成了 23 个带角色的斜杠命令，每个命令对应一个环节：`/design-shotgun` 生成多套设计稿、`/design-html` 把稿子转成可上线的 HTML、`/qa` 自动跑回归并修 bug、`/ship` 开 PR、`/canary` 在部署后监控控制台报错。命令之间用统一的浏览器会话和评分机制串起来。README 里作者自述近 60 天兼职产出了 3 个生产服务、40 多个功能，但他同时注明 AI 会让代码行数虚高，相关产出口径存在争议。

适合想把 AI 编码从"逐条对话"改成"固定流程"的独立开发者和小团队参考。

🔗 项目地址：https://github.com/garrytan/gstack

---

## 2. Hermes Agent — Nous Research 开源的可自我改进命令行智能体

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 201k | 936 | Python | MIT |

Hermes Agent 是 AI 实验室 Nous Research 开源的命令行智能体，主打一个内置的学习循环：它会从每次任务里沉淀出可复用的 skill，在使用过程中改写这些 skill，检索自己过去的对话，并在多次会话之间逐步建立对使用者的画像。仓库创建于 2025 年 7 月，总 star 已超过 20 万。

和把状态绑在本机的助手不同，Hermes 可以跑在 5 美元的 VPS、GPU 集群，或闲置时近乎零成本的 serverless 上，使用者能通过 Telegram 远程指挥它在云端虚拟机上干活。模型层不做锁定：支持 Nous Portal、OpenRouter（README 称接入 200+ 模型）、NVIDIA NIM、z.ai/GLM、Kimi、OpenAI 等，用 `hermes model` 一行命令切换，不需要改代码。

适合想要一个常驻云端、跨会话保留记忆的个人智能体，或想研究 agent 自我改进机制的开发者。

🔗 项目地址：https://github.com/NousResearch/hermes-agent

---

## 3. AI Website Cloner Template — 用 AI 编码 agent 把网站逆向成 Next.js 代码

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 18.6k | 826 | TypeScript | MIT |

这是一套可复用模板，目标是把任意网站逆向成一份干净的 Next.js 代码。用法是把它指向一个 URL，运行 `/clone-website` 命令，AI agent 会检查页面、提取设计 token 和素材、写出组件规格，再派发多个并行 builder 把每个区块重建出来。仓库创建于 2026 年 3 月，目前 1.8 万 star，已有一定关注度。

和手动扒站或纯截图还原相比，它把"逆向"拆成了 agent 可执行的固定步骤，并预置了 Next.js、React、Tailwind、shadcn/ui 这套技术栈。官方推荐配合 Claude Code（README 提到搭配 Opus 4.7 效果较好）使用，但也兼容其他编码 agent——非 Claude 的 agent 会读取仓库里的 `AGENTS.md` 获取项目说明。

适合需要快速复刻某个页面布局做原型、或想把现有静态站迁移到 Next.js 的前端开发者。需要注意它是模板仓库，官方建议用 "Use this template" 建自己的副本，而不是直接克隆主仓库。

🔗 项目地址：https://github.com/JCodesMore/ai-website-cloner-template

---

## 今日观察

今天榜单前列的方向高度一致，三个项目都在围绕"把 AI 编码 agent 固化成可复用流程"做文章：gstack 固化研发流水线，Hermes 固化 agent 的记忆与技能，Cloner 固化逆向建站。相比早期"让模型写两行代码"，社区的关注点正在往"如何用工程化的方式把 agent 用稳"上转。

---

**Tags**：#GitHub热点 #AI开源 #ClaudeCode #AIAgent #NextJS
