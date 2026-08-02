<!--
标题候选：
1. 今日 GitHub AI 项目：3D 生成与语音工具重新成主线
2. TRELLIS.2 登顶今日 AI Trending，另两个项目同样值得关注
3. 今日 GitHub AI 热点：3 个项目 24 小时新增超 200 star
当前正在使用：候选 1
-->

# 今日 GitHub AI 项目：3D 生成与语音工具重新成主线

> 今天的 GitHub Trending 日榜里，AI 相关项目集中在生成与语音两个方向。微软开源的 3D 生成模型、面向韩语用户的 Agent 技能集合、以及一款语音克隆工具，分别代表了模型研究、Agent 生态和实用工具三种不同的落地路径。

---

## 1. TRELLIS.2 — 微软开源的 4B 参数 3D 生成模型

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 9,957 | 107 | Python | MIT |

TRELLIS.2 解决的是图片转 3D 资产的问题：输入一张图，输出带完整拓扑结构和 PBR 材质（basecolor、roughness、metallic、opacity 四个通道）的三维模型。项目由微软开源，参数规模为 40 亿。

技术上，它引入了一种名为 O-Voxel 的稀疏体素架构，不依赖传统等值面提取方法，因此能处理开放曲面（比如衣物）、非流形几何和封闭内部结构等复杂拓扑，这是很多同类 3D 生成方法处理不了的场景。生成速度方面，在 H100 上生成 512³ 分辨率结果约需 3 秒，1536³ 分辨率约需 60 秒；网格转 O-Voxel 格式单 CPU 10 秒内完成，反向转换用 CUDA 可压到 100 毫秒以内。模型基于 Sparse 3D VAE，做了 16 倍空间下采样以压缩潜在空间，训练数据用了 Objaverse-XL 数据集。

项目提供完整训练代码，支持从零训练或在自有数据集上微调，运行需要 24GB 以上显存的 NVIDIA GPU。适合做 3D 资产生成研究、游戏与影视资产预生产的团队参考。

🔗 项目地址：https://github.com/microsoft/TRELLIS.2

---

## 2. k-skill — 面向韩语用户的 AI Agent 技能集合

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 6,758 | 53 | JavaScript | MIT |

k-skill 把韩国本地化的琐碎数字服务打包成一批可供 AI Agent 调用的"技能"（skills），让 Claude Code、Codex、OpenCode、ClawHub 这类 Agent 工具能直接完成买火车票、查股票、查政务信息这些操作。项目目前收录超过 100 个技能，覆盖交通订票（SRT、KTX、长途大巴）、金融证券查询、电商比价（Coupang、番腾、当近）、法律文书和生活服务等类别。

架构上它没有做客户端 API 封装层，而是让技能直接向代理服务器发 HTTP 请求，减少了中间代码。鉴权方式比较灵活：本地凭证、环境变量或托管代理三选一，部分技能（如电商比价）同时支持本地 HMAC 签名和托管代理两种模式。核心代码用 MIT 协议开源，代理服务组件单独用了 AGPL-3.0-only。截至目前项目累计 862 次提交，仍有 116 个开放 issue，处于活跃迭代状态。

适合已经在用 Claude Code 或其他 Agent 工具、且需要处理韩国本地化服务的开发者参考，也可以作为"给 Agent 做技能包"这类工程模式的一个具体案例来看。

🔗 项目地址：https://github.com/NomaDamas/k-skill

---

## 3. Voice-Pro — 集成语音克隆与字幕生成的 Gradio 工具

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 11,803 | 58 | Python | GPL-3.0 |

Voice-Pro 是一个基于 Gradio 的 WebUI 工具，把语音识别、零样本语音克隆、文本转语音和多语言翻译整合到一个界面里。语音识别用 Whisper、Faster-Whisper 系列模型，克隆功能基于 E2-TTS、F5-TTS 和 CosyVoice，文本转语音支持 Edge-TTS 和 kokoro 模型，同时内置 YouTube 下载和 Demucs 人声分离。

最新的 v4.0 版本把包管理从 Miniconda/pip 迁移到了 uv，运行环境升级到 Python 3.12 配合 Torch 2.8.0+cu128，新增对 RTX 50 系列显卡的支持。这一版还加入了 Fun-CosyVoice3-0.5B 模型，为克隆功能补上了韩语以及另外 8 种语言。依赖现在以预编译 wheel 形式分发，不再需要单独装 CUDA Toolkit 和 Visual Studio Build Tools，安装门槛有所降低。运行需要 4GB 以上显存的 NVIDIA GPU、20GB 以上存储空间，首次启动会下载约 10GB 模型文件。

适合做播客、有声书、短视频配音的内容创作者，以及需要批量处理多语言字幕和配音的团队。

🔗 项目地址：https://github.com/abus-aikorea/voice-pro

---

## 今日观察

今天入选的三个项目分别落在模型研究（3D 生成）、Agent 生态基建（技能集合）和终端工具（语音处理）三个不同层次，说明当前 AI 相关的开源产出并不集中在单一方向，而是从底层模型到应用工具都有人在推进。

---

**Tags**：#GitHub热点 #AI开源 #3D生成 #AgentSkills #语音克隆
