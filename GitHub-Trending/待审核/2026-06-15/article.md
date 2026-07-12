<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub Trending：AI 热点暂歇，工具与教材类项目回到前排
2. Chatwoot 登上今日 Trending 前排，另两个项目同样值得关注
3. 今日 GitHub 日榜：3 个项目 24 小时新增超 950 star
当前使用：候选 1
-->

# 今日 GitHub Trending：AI 热点暂歇，工具与教材类项目回到前排

> 今天日榜上几个排名靠前的 AI 项目（NVIDIA/SkillSpector、Kronos、aisuite）过去几天已经写过，不重复。剩下新进前排的项目方向各异：一个自托管客服平台、一本机器人教材、一份网站克隆合集。下面按 24 小时新增 star 排序介绍。

---

## 1. Chatwoot — 自托管的多渠道客户支持平台

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 31.4k | 400 | Ruby | 自定义（GitHub 标记 NOASSERTION） |

Chatwoot 解决的问题是把分散在不同入口的客户对话收拢到一个收件箱里。它把网站在线聊天、邮件、WhatsApp、Instagram、Telegram、SMS 等渠道接到同一个面板，定位是 Intercom、Zendesk 这类 SaaS 客服系统的开源自托管替代品，数据留在自己手里。

和这些 SaaS 产品的差异主要在部署形态：Chatwoot 基于 Rails 加 Vue，可以用 Docker、Heroku、DigitalOcean 自行部署。README 里还提到一个名为 Captain 的 AI 客服功能，用于自动回复常见问题、分担人工坐席的重复工作量，把人力留给更复杂的对话。此外它带有帮助中心、内部备注与 @ 提及、标签、快捷回复、自动分配等协作功能。

适合希望自己掌握客户数据、或想替换商业客服订阅的中小团队参考。

🔗 项目地址：https://github.com/chatwoot/chatwoot

---

## 2. Introduction to Autonomous Robots — 自主机器人的开源教材

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 2.9k | 293 | TeX | CC-BY-NC-ND 4.0 |

这是一本关于自主机器人计算原理的开源教材，作者为 Nikolaus Correll 等四人，对应 MIT Press 2022 年出版的同名书籍。内容覆盖机构、传感器、执行器与算法等机器人学基础主题，仓库创建于 2013 年，长期维护至今。

它的形态和一般开源项目不同：仓库里放的是 LaTeX 源码，而不是现成 PDF。由于纸质版版权归 MIT Press，作者按 CC-BY-NC-ND 4.0 释出源码，读者可以自行用本地 LaTeX 或 Overleaf 编译出 PDF，但不允许把编译好的成品再传到网上。教学用途下可在署名前提下使用书中图文。

适合机器人方向的学生与教师作为系统性的入门材料。

🔗 项目地址：https://github.com/Introduction-to-Autonomous-Robots/Introduction-to-Autonomous-Robots

---

## 3. Clone-Wars — 100 多个流行网站的开源克隆合集

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 35.7k | 269 | — | AGPL-3.0 |

Clone-Wars 本身不是一个应用，而是一份清单：收录了 100 多个流行网站的开源克隆与替代实现，覆盖 Airbnb、Netflix、Instagram、Spotify、WhatsApp、YouTube 等，并附上源码、演示链接、教程和技术栈。

清单分成两张表：一张是带配套教程的全栈克隆，适合照着从零搭一遍；另一张区分"克隆"和"替代品"——前者多为 UI 相似、功能不完整的学习项目，后者是功能完整的开源替代软件，可以用 GitHub star 数大致判断两者区别。仓库创建于 2020 年，靠社区 PR 持续补充。

适合想通过复刻已知产品来练习全栈开发的开发者。

🔗 项目地址：https://github.com/GorvGoyl/Clone-Wars

---

## 今日观察

今天日榜的 AI 项目集中在前几天已经覆盖过的几个，新进前排的项目方向比较分散：客服工具、学术教材、学习资源各占一类，彼此之间没有明显共同主线。这类日子更适合把它们当作不同方向的独立信息点来看，而不是硬找趋势。

---

**Tags**：#GitHub热点 #开源项目 #客户支持 #机器人学 #全栈开发
