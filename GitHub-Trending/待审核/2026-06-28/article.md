<!--
标题候选（3 个，jacob 挑用）：
1. 今日 GitHub AI 项目：文档转 PPT、终端编码、图像视频生成各占一席
2. ppt-master 领跑今日 AI Trending，opencode 与 Open Generative AI 同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时合计新增逾 1,200 star
当前使用：候选 1
-->

# 今日 GitHub AI 项目：文档转 PPT、终端编码、图像视频生成各占一席

> 今天 Trending 日榜上的 AI 项目集中在"生成"和"编码"两条线上。我们挑了 24 小时新增 star 最高的三个，方向各不相同：一个把文档转成可编辑的 PPT，一个是终端里的开源编码 agent，一个把 200 多个图像视频模型聚合到一个工作台里。

---

## 1. ppt-master — 把任意文档转成可编辑 PPT 的 agent 工具

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 33.2k | 589 | Python | MIT |

PPT Master 解决的问题很具体：把一份现成文档自动转成一份真正可编辑的 PowerPoint。它接收 Word、HTML、Markdown、Jupyter Notebook 等格式，输出的不是"把图片贴在幻灯片上"，而是带原生形状、动画和演讲者备注的 .pptx 文件，备注还能转成配音音频。

和很多"一键生成 PPT"的工具不同，它本身不内置模型，而是作为一个 agent 工具运行在 Cursor、VS Code、Claude Code 这类能读写文件、执行命令的环境里，由这些工具背后的模型来驱动生成。环境依赖只有 Python，.docx/.html/.epub/.ipynb 走原生解析，少数老格式才需要 pandoc。当前版本 v2.11.0，开源于 2025 年 12 月。

适合需要把报告、笔记批量转成演示文稿、又希望成稿能继续编辑而非重排版的用户。

🔗 项目地址：https://github.com/hugohe3/ppt-master

---

## 2. opencode — 运行在终端里的开源编码 agent

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 179.8k | 392 | TypeScript | MIT |

opencode 是一个开源的命令行 AI 编码 agent，定位是在终端里完成读代码、改代码、跑命令这类日常开发任务。它提供终端 UI，也有处于 beta 阶段的桌面端应用，安装方式覆盖 npm、Homebrew、Scoop、pacman、Nix 等多种包管理器。

和绑定在某个 IDE 里的编码助手相比，它走的是终端优先、开源的路线。项目采用客户端／服务端结构，配置项较多，文档集中在 opencode.ai/docs；README 已经被翻译成 20 多种语言。它创建于 2025 年 4 月，目前总 star 约 18 万，属于这一方向里体量靠前的开源项目。

适合习惯在终端而非图形界面里写代码、并希望工具链保持开源可控的开发者。

🔗 项目地址：https://github.com/anomalyco/opencode

---

## 3. Open Generative AI — 聚合 200 多个模型的图像视频生成工作台

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 21.4k | 255 | JavaScript | MIT |

Open Generative AI 是一个开源、可自托管的图像与视频生成工作台，把 200 多个模型放进同一个界面。它划分出图像、视频、对口型（Lip Sync）、电影镜头（Cinema）和工作流（Workflow）几个工作区，把自己定位成闭源生成平台的开源替代。

除了通过 MuAPI 调用云端模型，它也支持本地推理：内置的 sd.cpp 引擎可在 Mac、Windows、Linux 上跑 SD 1.5、SDXL、Z-Image，另可外接 Wan2GP 服务运行 Flux、Qwen-Image 以及 Wan 2.2、Hunyuan、LTX 等视频模型；编辑类模型最多支持上传 14 张参考图。项目开源于 2023 年 5 月。

适合想在一个工具里横向比较多种图像／视频模型、或对数据本地化有要求的创作者。

🔗 项目地址：https://github.com/Anil-matcha/Open-Generative-AI

---

## 今日观察

今天这三个 AI 项目方向并不重叠，却共享同一条主线：把原本分散的生成或编码能力，收进一个开源、可本地运行、底层模型可替换的工具里。从文档转 PPT、终端编码到图像视频生成，"开源替代加上用户自己掌握模型选择权"是它们共同的卖点。

---

**Tags**：#GitHub热点 #AI开源 #AIPPT #编码Agent #AI视频生成
