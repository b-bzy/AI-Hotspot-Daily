<!--
标题候选：
1. 今日 GitHub AI 项目：Agent 上下文管理成为关注焦点
2. OpenViking 领跑今日 AI 项目，另两个热门工具同样值得关注
3. 今日 GitHub 热点：3 个项目 24 小时新增超 1800 star
当前正在使用：候选 1
-->

# 今日 GitHub AI 项目：Agent 上下文管理成为关注焦点

> 今天的 GitHub Trending 日榜上，AI 相关项目大多是过去一两个月写过的老面孔，去重后只剩下一个新项目符合筛选标准——面向 Agent 的上下文数据库 OpenViking。另外两个按 24 小时新增 star 数补位的项目分别是免费 API 目录 public-apis 和跨平台下载管理器 Motrix。

---

## 1. OpenViking — 统一 Agent 记忆、RAG 检索与技能的上下文数据库

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 29.5k | 213 | Rust | AGPL-3.0 |

OpenViking 要解决的问题是 Agent 上下文管理的碎片化——记忆、RAG 检索结果、技能往往分散在不同系统里，查询方式也不统一。它把三者统一存进一个虚拟文件系统，通过 `viking://` 协议访问，Agent 可以用 `ls`、`tree`、`find` 这类命令式操作浏览自己的上下文，不必单独接入一套向量检索接口。

和常见的向量数据库检索方式不同，OpenViking 把内容按 L0（一句话摘要）、L1（约 2k token 概览）、L2（完整原文）分三层组织，按需加载对应深度以节省 token；检索时先用向量定位命中率最高的目录，再逐层下钻，同时保留检索轨迹便于调试。已完成的会话还会被异步转成长期记忆。README 给出的 benchmark 显示，用户记忆准确率从 24%-57% 提升到 80%-83%，token 消耗下降 34%-91%，查询延迟降低 58%-66%。

适合搭建需要跨会话记住用户偏好、长期运行的 Agent 系统的团队参考。

🔗 项目地址：https://github.com/volcengine/OpenViking

---

## 2. public-apis — 收录数百个免费 API 的社区维护目录

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 464.8k | 1,005 | Markdown | MIT |

public-apis 解决的问题很直接：开发者想找一个"能免费用的某领域 API"时，不用满世界搜索，直接按分类查这个仓库。内容按 40 多个类目索引，涵盖动物、反恶意软件、区块链、汇率、机器学习、天气等方向，每条 API 标注了描述、认证方式、是否支持 HTTPS、是否支持 CORS。

和一般的 Awesome List 不同，它更像一份持续维护的数据表——由社区成员和 APILayer 的员工共同人工审核收录，保证条目里的链接和认证信息不轻易失效。仓库目前有 51.3k fork 和 1.7k 个已合并 PR，贡献和使用的门槛都比较低。

适合做原型开发时快速找免费数据源，或者做 API 聚合、测试工具的开发者参考。

🔗 项目地址：https://github.com/public-apis/public-apis

---

## 3. Motrix — 支持 BT 与磁力链接的跨平台桌面下载管理器

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 53.8k | 609 | TypeScript | MIT |

Motrix 解决的问题是给 macOS、Windows、Linux 用户提供一个统一的下载管理界面，同时支持 HTTP/FTP 直链、BitTorrent 和磁力链接，不用为不同协议分别装软件。

它的下载引擎基于 aria2 的一个 fork，v2（Turbo）版本用 Electron、React、TypeScript 重写，新增了基于 JSON-RPC 2.0 的开放协议，让 UI、浏览器插件和命令行工具可以互相通信。功能上支持 BT 按文件选择下载、tracker 自动更新、UPnP/NAT-PMP 端口映射、QuickJS 插件沙箱与插件市场，还提供官方 CLI 和可跑在 NAS 上的 Docker 无头服务端。

适合需要统一管理多协议下载任务的个人用户，或想把下载能力接入自己脚本、NAS 系统的开发者。

🔗 项目地址：https://github.com/agalwood/Motrix

---

## 今日观察

今天的 AI 候选池里大多数是过去一两个月写过的老项目——短视频生成、Agent 长期记忆、安全技能库都命中了 90 天去重窗口，去重后只剩 OpenViking 一个新面孔。剩余名额按 24 小时新增 star 数由非 AI 项目补足，今天更像是一次平淡的日榜，而不是 AI 项目集中爆发的一天。

---

**Tags**：#GitHub热点 #AI开源 #AgentMemory #开源工具 #下载管理器
