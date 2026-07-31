<!--
标题候选：
1. 今日 GitHub 热点：跨代理协作工具与开发者资源集体上榜
2. OpenWork 登顶今日 AI 相关 Trending，另两个项目同样值得关注
3. 今日 GitHub 热点：3 个项目 24 小时合计新增超 2100 star
当前使用：候选 1
-->

# 今日 GitHub 热点：跨代理协作工具与开发者资源集体上榜

> 今天的 Trending 日榜里，真正意义上的新 AI 项目并不多——多数高分选手在过去一个月内已经上过榜。筛掉重复后，AI 方向留下了一个跨代理协作工具，另外两个分别来自 3D 建模和量化交易领域，同样在 24 小时内拿到了数百新增 star。

---

## 1. OpenWork — 让技能和 MCP 连接在多个 AI 代理间共用

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 18.8k | 915 | TypeScript | MIT |

OpenWork 想解决的问题很具体：开发者往往在 Claude Code、Cursor、Codex 等多个 AI 代理里各自配置一遍技能、MCP 连接和第三方服务，团队协作时更是要每人重复一遍。OpenWork 提供一个桌面应用和一个可安装到任意代理的 MCP 服务，把这些能力集中管理、跨工具和跨成员复用。

它的做法是只暴露两个工具：`search_capabilities` 用来发现可用能力，`execute_capability` 用来执行。安装后代理会打开浏览器完成登录，选择所属组织，随后就能直接调用被授权的技能、插件和连接的 Google Workspace、Microsoft 365 服务。面向团队的 OpenWork Den 控制台，则负责管理模型供应商配额、成员与团队权限、发布技能市场等。

适合已经在多个 AI 代理间切换、希望统一管理技能与连接的开发团队，也适合需要给团队成员分配不同工具权限的管理者。

🔗 项目地址：https://github.com/different-ai/openwork

---

## 2. Pascal Editor — 用 React Three Fiber 和 WebGPU 搭建的 3D 建筑编辑器

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 20.2k | 625 | TypeScript | MIT |

Pascal Editor 解决的是"在浏览器里创建和分享 3D 建筑项目"这件事，不依赖桌面端 CAD 软件。项目基于 React Three Fiber 做渲染，用 WebGPU 而非 WebGL 处理图形管线，官方演示站点在 editor.pascal.app 上可以直接体验。

工程结构上，仓库拆成了 core（场景状态与数据结构，用 Zustand 管理并结合 Zundo 支持撤销重做）、viewer（纯渲染运行时）、editor（交互式编辑工具）、nodes（内置节点定义）四个独立发布的 npm 包。这种拆分意味着开发者可以只装 viewer 包做一个只读的 3D 展示页面，不需要引入完整的编辑器功能，场景数据本地持久化在 IndexedDB 中。

适合做 Web 端建筑可视化、空间设计工具的前端开发者，也适合需要在自己的 Next.js 应用里嵌入 3D 建筑查看器的团队。

🔗 项目地址：https://github.com/pascalorg/editor

---

## 3. Awesome Systematic Trading — 系统化交易资源合集

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 11.2k | 621 | Python | — |

这是一份面向量化交易的资源清单，收录了 97 个回测与实盘交易相关的库和包、40 多个来自机构和学术界的策略描述、55 本书籍、23 个视频，外加一批博客和课程链接。分类相当细，光是"回测与实盘交易框架"就区分了事件驱动型（如 backtrader、nautilus_trader）和向量化型（如 vectorbt）两类，另外还单独列出了加密货币交易、经纪商 API、数据源、风险与定价指标计算等子分类。

它本身不是可运行的工具，而是一份索引，价值在于把分散在各处的开源项目和资料按用途归好类，省去搜索和辨别的成本。仓库同时提供了一批策略示例的 Python 脚本，作者维护的商业站点 paperswithbacktest.com 提供更完整的策略实现和回测数据。

适合正在评估回测框架、想系统学习量化交易但不知从何入手的开发者，作为书签收藏或按需查阅都合适。

🔗 项目地址：https://github.com/paperswithbacktest/awesome-systematic-trading

---

## 今日观察

今天榜单上被关键词命中的"AI 项目"大多是老面孔——过去 30 天内已经报道过，剩下能用的新选题只有 OpenWork 一个。今天补位的两个项目分别来自 3D 建模和量化交易，说明当天的开发者关注度并未集中在模型或 Agent 本身，而是分散在协作基础设施和垂直领域工具上。

---

**Tags**：#GitHub热点 #AI开源 #MCP #WebGPU #量化交易
