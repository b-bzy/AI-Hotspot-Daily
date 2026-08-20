<!--
标题候选：
1. 今日 GitHub 热榜：AI 候选撞上去重，三个新项目补位
2. amadeusprotocol/node 登顶今日 Trending，另两个项目同样值得关注
3. 今日 GitHub 热点：3 个项目 24 小时合计新增近 2000 star
当前正在使用：候选 1
-->

# 今日 GitHub 热榜：三个新项目补位登场

> 今天日榜前十里多是已报道过的 AI 项目在持续吸粉，按 90 天去重规则筛下来，符合条件的新 AI 候选一个不剩。于是按当日新增 star 数倒序，补进三个此前没写过的项目：一个区块链节点、一个 LLM 参与链上决策的合约脚手架，以及一款自托管相册工具。

---

## 1. amadeusprotocol/node — 实验性区块链协议的验证者节点客户端

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 4.6k | 1,397 | Erlang | — |

Amadeus Protocol 是一条用 Erlang/Elixir 编写的区块链，node 仓库提供了运行验证者（validator）和计算节点（computor）的完整客户端代码。开发者照着 README 就能起一条本地测试网，通过 RPC 发起转账，并部署用 AssemblyScript 编写、编译成 WebAssembly 的智能合约。

项目构建走 podman/docker 容器化，官方文档给出了针对高并发 UDP 流量的内核参数调优建议，比如调大 `net.core.rmem_max`、`udp_mem`，还配了 systemd 服务定义和自动更新脚本，能看出团队在节点吞吐上做了工程取舍。仓库根目录没有 LICENSE 文件，README 注明这是一份仅供教育研究用途的实验性代码，部分受制裁地区限制使用。

适合关注新公链底层实现、想跑测试网验证 WASM 合约执行逻辑的区块链开发者，对普通应用开发者用处有限。

🔗 项目地址：https://github.com/amadeusprotocol/node

---

## 2. genlayer-project-boilerplate — GenLayer 智能合约平台的官方脚手架，示范 LLM 参与链上决策

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 16.2k | 430 | TypeScript | MIT |

GenLayer 是把大语言模型接入智能合约执行流程的区块链项目，genlayerlabs 官方给出的这份脚手架用一个"足球比赛投注"示例合约做演示：合约在链上发起网络请求、调用 LLM 判断比赛结果，再由多个节点对 LLM 输出做共识校验，避免单次模型推理的不确定性直接写入链上状态。

测试分两层：direct mode 用内存 mock 替换真实网络请求和 LLM 调用，单次只要几毫秒；integration 模式则接上真正的 GenLayer Studio 做端到端验证。配套 GenVM linter 会在部署前检查合约代码是否含不确定性调用、存储类型是否合法，前端用 Next.js 15 加 TypeScript 搭建，附带部署脚本和 CI 流水线。

适合想了解"LLM 参与链上共识"这类智能合约新方向的开发者，作为学习 GenLayer 平台的起点比较合适，README 未提供面向生产环境的部署说明。

🔗 项目地址：https://github.com/genlayerlabs/genlayer-project-boilerplate

---

## 3. immich — 自托管的照片与视频管理方案

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 112k | 128 | TypeScript | AGPL-3.0 |

Immich 要解决的问题很具体：把手机相册和视频的备份、管理功能从 Google Photos 这类云服务搬到用户自己的服务器上。项目同时提供 Flutter 编写的移动端 App 和网页端，手机打开 App 后会自动把新增照片同步到自建服务器，不用依赖第三方云存储。

后端用 NestJS，网页端用 SvelteKit，检索支持按 EXIF 元数据、地理位置、人脸聚类以及 CLIP 向量做语义搜索，体验和商业相册产品比较接近。项目采用 AGPL-3.0 协议，基于它二次开发并对外提供服务时，需要把改动部分一并开源。

适合对隐私敏感、想把家庭照片视频放在自己的 NAS 或服务器上管理的用户，尤其是已经在用群晖、极空间之类自建存储方案的人群。

🔗 项目地址：https://github.com/immich-app/immich

---

## 今日观察

今天的 AI 候选几乎全撞上了去重规则——本地推理、多智能体、Agent Skills 这几类大多是已写过的老面孔在持续吸粉。补位的三个项目里，genlayer-project-boilerplate 算是唯一沾 AI 边的方向（LLM 参与链上共识判定），另两个一个是区块链节点、一个是自托管工具，方向并不统一，更像是按当日新增 star 数排序后的自然结果。

---

**Tags**：#GitHub热点 #开源项目 #智能合约 #自托管 #区块链
