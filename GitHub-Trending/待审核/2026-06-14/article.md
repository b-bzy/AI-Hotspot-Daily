<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub AI 热点：多模型框架与金融基础模型同时上榜
2. aisuite 因桌面智能体 OpenCoworker 登上今日 Trending，另两个项目同样值得关注
3. 今日 GitHub 日榜：3 个项目 24 小时合计新增超 2k star
当前使用：候选 1
-->

# 今日 GitHub AI 热点：多模型框架与金融基础模型同时上榜

> 今天日榜上 AI 相关项目数量不多，方向也较分散：一个是统一调用多家大模型的开发框架，一个是金融领域的基础模型。榜单头名则是与 AI 无关的 IPTV 频道仓库，这里作为补位一并介绍。

---

## 1. aisuite — 多家大模型供应商的统一调用接口

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 14.3k | 290 | Python | MIT |

aisuite 解决的问题是：用一套 OpenAI 风格的接口去调用 OpenAI、Anthropic、Google、Mistral、Hugging Face、AWS、Cohere、Ollama、OpenRouter 等多家供应商的模型，切换供应商只需要改动一个字符串，不必为每家 SDK 重写业务代码。

项目分两层：底层是统一的 Chat Completions API，上层是带工具和工具包的 Agents API，可以把 Python 函数当作工具交给模型、运行多轮循环，并接入 MCP server。这次登上 Trending 的直接原因，是仓库新增了基于 aisuite 构建的桌面应用 OpenCoworker——一个能读取本地文件、收发消息、生成 PDF/文档/表格的桌面智能体，支持自带 OpenAI/Anthropic/Google 的 API key，也可以用 Ollama 完全本地运行。该项目自 2024 年年中开源。

适合需要在多家模型之间切换，或想在自己应用里加一层供应商抽象的开发者参考。

🔗 项目地址：https://github.com/andrewyng/aisuite

---

## 2. Kronos — 面向金融 K 线的开源基础模型

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 29.7k | 238 | Python | MIT |

Kronos 是一组专门针对金融市场 K 线（OHLCV 序列）预训练的 decoder-only 基础模型，作者称其为"首个面向金融蜡烛图的开源基础模型"，训练数据来自全球 45 个以上交易所。

它采用两阶段框架：先用一个专门的 tokenizer 把连续的多维 K 线数据量化成分层离散 token，再用一个自回归 Transformer 在这些 token 上预训练，使其可以服务于多种量化任务。项目在 Hugging Face 上发布了不同容量的预训练模型，并提供了一个对 BTC/USDT 未来 24 小时走势预测的在线 demo。相关论文已于 2025 年 8 月上传 arXiv，并被 AAAI 2026 接收。

适合做量化研究、或想把时间序列基础模型用在金融数据上的团队参考。

🔗 项目地址：https://github.com/shiyu-coder/Kronos

---

## 3. iptv-org/iptv — 全球公开 IPTV 频道的汇总仓库

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 120k | 1.5k | TypeScript | Unlicense |

这是今日 Trending 日榜的头名项目，方向与 AI 无关，作为补位收录。它汇集了全球公开可用的 IPTV（基于 IP 的电视）频道链接，把主播放列表的 m3u 文件链接粘贴到任意支持直播流的播放器里即可观看。

仓库本身不存储任何视频文件，只收录用户提交的、指向公开视频流的链接；频道数据来自配套的 iptv-org/database 仓库，并通过 GitHub Actions 自动更新。项目还维护了 EPG（电子节目单）、API 等配套仓库。该仓库创建于 2018 年，是同类资源里规模较大的头部项目。

适合需要免费直播源、或想研究 IPTV 播放列表组织方式的用户。

🔗 项目地址：https://github.com/iptv-org/iptv

---

## 今日观察

今天 AI 相关项目在日榜上偏少，且方向各异：一个是面向多模型的开发框架，一个是金融垂直领域的基础模型，两者之间没有直接联系。榜单头名反而是与 AI 无关的 IPTV 频道仓库。可以看到，AI 已不是 Trending 的唯一主线，工具型框架与垂直领域模型各占一席。

---

**Tags**：#GitHub热点 #AI开源 #大模型接口 #智能体 #金融基础模型
