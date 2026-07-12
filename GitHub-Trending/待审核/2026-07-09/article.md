<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub Trending：AI Agent 基础设施与边缘感知同时上榜
2. RuView 登顶今日 Trending，用 WiFi 信号做空间感知，另两个 Agent 项目同样值得关注
3. 今日 GitHub AI 热点：三个项目 24 小时合计新增超 1,600 star
当前使用：候选 1
-->

# 今日 GitHub Trending：AI Agent 基础设施与边缘感知同时上榜

> 今天日榜上排除掉近 90 天写过的项目后，AI 方向剩下的热点集中在两条线：一条是给 Agent 用的运行时基础设施（沙箱、记忆），另一条是把机器学习推到边缘硬件上的感知项目。下面三个项目 24 小时合计新增超过 1,600 star，方向各不相同。

---

## 1. RuView — 用 WiFi 信号做空间感知的边缘传感平台

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 79.3k | 799 | Rust | MIT |

RuView 解决的问题是：不用摄像头、不用可穿戴设备，只靠普通 WiFi 信号来感知一个房间里的情况。它从低成本的 ESP32 传感器上采集信道状态信息（CSI），据此判断有没有人、几个人、以及呼吸和心率等生命体征，甚至能识别跌倒、离床、睡眠阶段这类状态。

技术上的差异点在于它把模型放到了边缘。RuView 用脉冲神经网络在本地学习每个环境，官方称适配时间在 30 秒以内；配套的预训练模型发布在 Hugging Face（`ruvnet/wifi-densepose-pretrained`），4-bit 量化后约 8KB，可在树莓派上以微秒级延迟运行。项目文档给出的是一个 label-free 的时序三元组准确率 82.3%（此前的“100% presence”数据已被作者撤回），这种主动标注数据来源的做法在同类项目里不算常见。

它适合做智能家居、独居老人监护、睡眠监测等对隐私敏感、又不方便装摄像头的场景，并已提供 Home Assistant、Apple Home、Google Home、Alexa 的接入方式。

🔗 项目地址：https://github.com/ruvnet/RuView

---

## 2. CubeSandbox — 面向 AI Agent 的轻量安全沙箱

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 9.0k | 564 | Rust | Apache-2.0 |

当 Agent 需要执行模型生成的代码时，直接在主机上跑存在安全风险。CubeSandbox 提供的是一个硬件级隔离的沙箱服务：基于 RustVMM 和 KVM 构建，官方数据是单个沙箱创建耗时低于 60ms、内存开销小于 5MB，面向高并发、高密度的部署场景。

它的一个工程取舍是兼容 E2B SDK，也就是原本接 E2B 的应用可以较低成本迁移过来。近几个版本补上了不少运维能力：v0.3 引入 CubeCoW 写时复制快照，支持事件级快照、即时克隆和回滚；v0.5（2026-07-03）加入了空闲自动挂起/唤醒、Terraform 一键集群部署和 ARM64 原生支持。项目创建于 2026 年 4 月，目前已进入 CNCF Landscape。

适合需要给 Agent 提供代码执行环境、又关注隔离性和启动速度的团队参考。

🔗 项目地址：https://github.com/TencentCloud/CubeSandbox

---

## 3. TencentDB-Agent-Memory — 面向 AI Agent 的本地长期记忆

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 7.8k | 318 | TypeScript | MIT |

这个项目想解决的是 Agent 反复被“重新交代同一件事”的问题：SOP、项目背景、工具约定、输出格式，本不该每次都塞进上下文重讲一遍。它把记忆设计成分层结构，而不是把历史一股脑塞进一个扁平的向量库。

具体分两条：短期记忆用符号化处理，把冗长的工具日志压缩成紧凑的 Mermaid 符号；长期记忆则搭一个语义金字塔，L0 原始对话 → L1 原子事实 → L2 场景 → L3 用户画像，只有需要细节时才向下钻取。项目给出的 benchmark 显示，与 OpenClaw 集成后在 WideSearch 上 token 用量最多降低 61.38%、通过率相对提升 51.52%，PersonaMem 的准确率从 48% 提到 76%。它强调零外部 API 依赖、本地优先。

适合在长周期、多轮任务里需要控制上下文成本、又想让 Agent 复用历史经验的开发者。

🔗 项目地址：https://github.com/TencentCloud/TencentDB-Agent-Memory

---

## 今日观察

今天的三个项目并没有落在同一个细分主题上，但两条线索比较清晰：CubeSandbox 和 TencentDB-Agent-Memory 都在补 Agent 的运行时短板——一个管“在哪执行”，一个管“记住什么”；RuView 则代表另一类思路，把小模型直接压进边缘硬件去做感知。基础设施和边缘化，是这份榜单当下比较值得留意的两个方向。

---

**Tags**：#GitHub热点 #AI开源 #AIAgent #边缘计算 #向量数据库
