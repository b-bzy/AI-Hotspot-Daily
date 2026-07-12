<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub Trending：AI Agent 从对话转向安全测试与视频剪辑
2. Strix 进入今日 Trending 前列，另两个 AI 项目同样值得关注
3. 今日 GitHub AI 热点：三个项目 24 小时合计新增近 700 star
当前使用：候选 1
-->

# 今日 GitHub Trending：AI Agent 从对话转向安全测试与视频剪辑

> 今天的日榜里，AI 项目集中在"把大模型嵌进具体工种"这条线上。我们挑了三个方向各异的项目：一个做自动化安全测试，一个是流式三维重建的基础模型，一个用编码 Agent 剪视频。它们的共同点是都强调可落地、可验证，而不是停留在对话演示。

---

## 1. Strix — 用 AI Agent 做自动化安全测试

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 26.8k | 122 | Python | Apache-2.0 |

Strix 解决的问题是应用安全测试的人力成本。它把一组自治 Agent 模拟成渗透测试人员：动态运行目标代码、寻找漏洞，并通过真实的概念验证（PoC）来确认漏洞是否成立。面向的是没时间做手工渗透、又不想被静态扫描工具大量误报淹没的开发者和安全团队。

与传统静态分析相比，Strix 的差异在于"先验证再上报"。它不只是标记可疑代码，而是在沙箱（依赖本地 Docker）里实际复现，给出 PoC 和可执行的修复报告；多个 Agent 之间还能协作分工。运行时需要接一个 LLM API key，README 里列出的支持方包括 OpenAI、Anthropic、Google 等。

适合需要把安全测试接进 CI/CD、在每次 pull request 上自动扫描的团队，以及做 bug bounty 研究、希望自动生成 PoC 的人。项目创建于 2025 年 8 月，目前已有规模。

🔗 项目地址：https://github.com/usestrix/strix

---

## 2. LingBot-Map — 流式三维重建的前馈基础模型

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 8.2k | 372 | Python | Apache-2.0 |

LingBot-Map 面向的是从连续视频流里重建三维场景这一具体任务，对应机器人、SLAM、自动驾驶等需要实时建图的场景。它是一个前馈（feed-forward）的三维基础模型，输入流式数据、输出重建结果，并配有 arXiv 论文以及 HuggingFace、ModelScope 上的模型权重。

技术上的差异点在它命名的 Geometric Context Transformer：通过锚点上下文、位姿参考窗口和轨迹记忆，把坐标对齐、稠密几何线索和长程漂移校正放进同一个流式框架里处理。配合分页 KV 缓存注意力，README 给出的数据是在 518×378 分辨率、超过 10,000 帧的长序列上保持约 20 FPS 的稳定推理；作者称在 KITTI、Oxford Spires、Tanks and Temples 等多个基准上相比现有流式方法和迭代优化方法有更好表现。

适合做实时三维视觉、在线建图研究的开发者参考。项目创建于 2026 年 4 月，已有一定关注度。

🔗 项目地址：https://github.com/Robbyant/lingbot-map

---

## 3. video-use — 用编码 Agent 剪视频

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 11.2k | 196 | Python | MIT |

video-use 来自 browser-use 团队，解决的问题是把视频粗剪交给编码 Agent。使用方式是把原始素材丢进一个文件夹，在 Claude Code 或类似 Agent 里对话，最后拿回 `final.mp4`。它会剪掉口头语和停顿、按统一风格做调色、在每个剪辑点加 30ms 音频淡入淡出、烧录字幕，并能调用外部工具生成动画叠层。

它的工程取舍值得注意：模型本身并不"看"视频，而是"读"视频。每段素材先用 ElevenLabs Scribe 转成带词级时间戳、说话人分离和音频事件的文字，全部素材打包进一个约 12KB 的 `takes_packed.md` 作为 Agent 的主要阅读视图，从而实现按词边界精确剪辑。每个剪辑点渲染后 Agent 会先自评，再把结果给用户；会话状态写进 `project.md` 以便下次接续。

适合愿意用 Agent 工作流处理口播、教程、访谈类素材的创作者。运行需要 ffmpeg 和 ElevenLabs API key。项目创建于 2026 年 4 月，已有规模。

🔗 项目地址：https://github.com/browser-use/video-use

---

## 今日观察

今天上榜的三个项目方向各不相同——安全测试、三维重建、视频剪辑，但都体现了同一种工程思路：把大模型能力嵌进一个特定专业流程，并通过 PoC 验证、基准测试或渲染自评来保证输出可信。相比纯对话演示，这类"嵌进具体工种"的项目更接近实际生产环节。

---

**Tags**：#GitHub热点 #AI开源 #AIAgent #三维重建 #AI安全
