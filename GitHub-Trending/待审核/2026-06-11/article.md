<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub 热榜：从写代码到做视频，AI 工具链占据主线
2. agent-skills 登顶今日 Trending，MoneyPrinterTurbo 单日新增 1.4k star
3. 今日 GitHub AI 热点：3 个项目 24 小时合计新增约 2.9k star
当前使用：候选 1
-->

# 今日 GitHub 热榜：从写代码到做视频，AI 工具链占据主线

> 今天的日榜由 AI 工程化工具领跑：登顶的 agent-skills 给 AI 编程代理装上软件工程流程，MoneyPrinterTurbo 以单日新增 1.4k star 重回视野，supervision 继续巩固计算机视觉工具链的位置。

---

## 1. agent-skills — 给 AI 编程代理的工程化技能包

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 52.1k | 821 | Shell | MIT |

AI 编程代理（Claude Code、Cursor 这类工具）写代码时常缺乏资深工程师的流程意识：不写规格就动手，不做测试就提交。由开发者 Addy Osmani 维护的 agent-skills 把"先写 spec、拆小任务、测试驱动、上线前审查"这些工程实践打包成可安装的技能，让代理在每个开发阶段都按规范执行。

项目提供 7 个斜杠命令对应开发生命周期：/spec、/plan、/build、/test、/review、/code-simplify、/ship。技能还能按场景自动激活——设计 API 时触发接口设计技能，写 UI 时触发前端工程技能。客户端覆盖面较宽，支持 Claude Code、Cursor、Gemini CLI、Windsurf 等多个工具。该仓库今年 2 月才创建，4 个月累计 52.1k star，增长速度在同类项目里少见。

适合正在用 AI 编程工具、又苦于产出质量不稳定的开发者。

🔗 项目地址：https://github.com/addyosmani/agent-skills

---

## 2. MoneyPrinterTurbo — 输入一个关键词，自动合成完整短视频

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 85.2k | 1,389 | Python | MIT |

MoneyPrinterTurbo 把短视频制作压缩成一步：给一个主题或关键词，自动生成文案、匹配素材、加字幕和背景音乐，最后合成 1080x1920 竖屏或 1920x1080 横屏的高清成片。

架构上是完整的 MVC 工程，同时提供 Web 界面和 API。模型接入面较宽，支持 OpenAI、通义千问、Gemini、DeepSeek、Ollama 等十余种服务；素材源对接 Pexels、Pixabay、Coverr 等免费素材库。GPU 不是必需项，普通配置也能运行。项目 2024 年 3 月开源，累计 85.2k star，这次 24 小时新增 1.4k 重新回到日榜前列。

适合需要批量产出口播类、文案类短视频的运营团队，以及想搭自动化内容流水线的开发者。

🔗 项目地址：https://github.com/harry0703/MoneyPrinterTurbo

---

## 3. supervision — 模型无关的计算机视觉工具箱

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 43.6k | 695 | Python | MIT |

做计算机视觉应用时，模型推理之外的环节——检测结果的格式统一、画框标注、区域计数、数据加载——往往要重复造轮子。supervision 把这些环节做成可复用组件，`pip install supervision` 即可使用。

它的设计是模型无关：内置 Ultralytics、Transformers、MMDetection 等主流库的连接器，任何分类、检测、分割模型的输出都能转成统一的 Detections 格式，再接标注器和统计工具。项目由视觉平台公司 Roboflow 维护，2022 年 11 月开源，迭代至今保持稳定节奏，已被多个团队用于生产环境。

适合需要把检测/分割模型快速落到实际应用的工程师，尤其是涉及视频流区域统计的场景。

🔗 项目地址：https://github.com/roboflow/supervision

---

## 今日观察

今天三个项目正好覆盖 AI 工具链的三个层面：agent-skills 管"AI 怎么写好代码"，MoneyPrinterTurbo 管"AI 怎么直接产出内容"，supervision 管"视觉模型怎么落地"。共同点是都不做模型本身，而是做模型周边的工程化配套——这一层的需求目前看比模型本身更稳定。

---

**Tags**：#GitHub热点 #AI开源 #AI编程 #短视频生成 #计算机视觉
