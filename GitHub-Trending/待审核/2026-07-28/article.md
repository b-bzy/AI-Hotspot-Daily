<!--
标题候选：
1. 今日 GitHub 热点：AI Agent 工程化工具与去中心化通信同时上榜
2. BitChat 登顶今日 GitHub Trending，AI Agent 工具包同样入围
3. 今日 GitHub 热点：三个项目 24 小时合计新增近 3000 star
当前正在使用：候选 1
-->

# 今日 GitHub 热点：AI Agent 工程化工具与去中心化通信同时上榜

> 今天的 GitHub Trending 日榜上 AI 相关项目数量不多，真正符合"AI"标签的只有面向 Google Antigravity 生态的 ag-kit。另外两个项目分别来自去中心化通信和终端工具方向，24 小时新增星标合计接近 3000。

---

## 1. BitChat — 蓝牙网状网络 + Nostr 双通道的去中心化聊天应用

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 32.4k | 2,346 | Swift | Unlicense |

BitChat 解决的是"网络不可用时如何通信"的问题：不需要账号、手机号或服务器，设备之间靠蓝牙网状网络直接建立连接，最多支持 7 跳中继；一旦能联网，又可以切换到 Nostr 协议接入 290 多个公共中继节点，实现跨地域的消息送达。

技术上它做了双层传输设计：离线层用 Noise 协议加密并具备前向保密，专门为蓝牙 LE 的带宽限制做了二进制协议优化；在线层则用 XChaCha20-Poly1305 加密私信，并引入基于 geohash 的位置频道，可以按街区、社区或城市粒度划分聊天范围。消息会按当前可用的传输方式自动路由，优先蓝牙、其次 Nostr。

适合灾害、集会等网络设施不可靠的场景，也适合对隐私和匿名性有要求的社区协作。

🔗 项目地址：https://github.com/permissionlesstech/bitchat

---

## 2. ag-kit — 面向 Google Antigravity 的 Agent 工程化工具包

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 8k | 14 | TypeScript | MIT |

ag-kit 要解决的是在 Google Antigravity 环境里搭建 AI Agent 时缺乏标准工程结构的问题。它在项目里放入一个 `.agents/` 工作区契约，内置 20 个专项 agent、47 个技能（skills）和 13 个可复用工作流，把原本需要手写的 agent 编排、持久化上下文管理、MCP 配置这些工作固定成了可复用的模板。

和普通的 agent 脚手架相比，ag-kit 多了一层安全约束：它内置一个原生 hook，会在文件系统操作层面拦截高风险动作（比如误删、越权写入），同时放行正常的清理任务，并提供更新回滚机制和一份生产环境就绪检查清单。运行需要 Node.js 22+ 与 Python 3.10+，通过 npm 安装。

适合已经在用 Antigravity 搭建多 agent 系统、需要一套统一工程规范而不是从零手写的团队。

🔗 项目地址：https://github.com/vudovn/ag-kit

---

## 3. superfile — 终端里的可视化文件管理器

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 21k | 600 | Go | MIT |

superfile 用 Go 写了一个终端文件管理器，目标很具体：给习惯命令行操作的用户提供一个界面更友好的替代品，而不是继续记 `cp`、`mv`、`find` 这类命令的参数组合。它基于 TUI（终端用户界面）构建，支持鼠标操作和键盘快捷键并行。

和同类的终端文件管理器相比，superfile 把主题定制、插件系统和 vim 风格快捷键都做成了可配置项，并提供跨平台安装脚本（Linux、macOS、Windows），支持 Homebrew、Winget、Scoop 等主流包管理器一键安装，还带自动检查更新功能。

适合每天大量在终端里操作文件、又不想放弃图形化文件浏览体验的开发者。

🔗 项目地址：https://github.com/yorukot/superfile

---

## 今日观察

今天的 AI 相关项目数量偏少，唯一入选的 ag-kit 面向的是 Google Antigravity 这个相对小众的 Agent 开发生态，24 小时新增星标只有 14，远低于榜单前列的项目。另外两个入选项目一个是去中心化通信工具，一个是终端效率工具，方向各异，没有共同的技术趋势可总结——今天更像是一个"AI 之外的日常工具"占主导的榜单。

---

**Tags**：#GitHub热点 #AIAgent工程化 #去中心化通信 #BluetoothMesh #终端文件管理
