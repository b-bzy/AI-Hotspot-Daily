<!--
标题候选：
1. 今日 GitHub 热点：AI 工具的安全与审美两条线
2. dcg、Hallmark、AI 教材同日上榜，今日 GitHub 热点解读
3. 今日 GitHub AI 热点：3 个项目 24 小时合计新增超 1,600 star
当前使用：候选 1
-->

# 今日 GitHub 热点：AI 工具的安全与审美两条线

> 今天的 GitHub Trending 日榜里，AI 原生开发工具占了不小比例。下面这三个项目分别对应"防止 AI 编程助手误删代码""让 AI 生成的界面不再一眼看出套路""用 AI 助手可查询的开源数理教材"三个具体问题。

---

## 1. destructive_command_guard (dcg) — 拦住 AI 编程助手误删代码的安全钩子

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 4.5k | 473 | Rust | custom |

dcg 解决的问题很具体：AI 编程助手（Claude Code、Codex CLI、Cursor 等）偶尔会执行 `git reset --hard`、`rm -rf`、`DROP TABLE` 这类破坏性命令，几秒内清空掉几个小时的未提交工作。dcg 以钩子（hook）形式介入，在命令真正执行前拦截，给出拦截原因和更安全的替代方案。

技术上它用 Rust 重写（原型由 Jeffrey Emanuel 用 Python 写成，后由 Darin Gordon 移植并扩展），通过 SIMD 加速的过滤把大多数安全命令快速放行，再用三层 heredoc 扫描识别藏在内联脚本里的破坏性调用。50 多个"安全包"按数据库、Kubernetes、云厂商等场景分类，可按需开启；设计上采用"失败即放行"（fail-open）原则，超时或解析出错时不会挡住正常工作流。

适合日常用多个 AI 编程助手协同工作、担心 agent 误删代码或数据的开发者，尤其是多个 agent 并行跑任务的团队。

🔗 项目地址：https://github.com/Dicklesworthstone/destructive_command_guard

---

## 2. Hallmark — 让 AI 生成的页面不再一眼看出是 AI 做的设计技能

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 6.3k | 1,015 | CSS | MIT |

Hallmark 要解决的是一个很多人吐槽过的问题——AI 生成的网页设计长得都差不多，同一套配色、同一套布局，换个品牌名字几乎认不出区别。Hallmark 是一个装进 Claude Code、Cursor、Codex 里的设计技能，通过 57 项"AI 感"检测规则加一轮自我审查，拒绝模型训练时学到的默认审美。

它内置 20 套主题和 4 个命令：默认动作生成新界面，`audit` 给现有代码打分列出问题清单，`redesign` 保留内容和信息架构、换一套设计指纹，`study` 从截图或网址里提取"设计 DNA"供其他项目参考。当需求本身带有创意、套不进任何预设主题时，会切换到 Custom 模式，从零定制配色、字体和布局。项目由 Together AI 出品。

适合用 AI 工具做落地页、产品官网的团队，尤其是已经受够"一眼 AI 感"设计、希望不同项目风格明显区分开的场景。

🔗 项目地址：https://github.com/Nutlope/hallmark

---

## 3. Maths, CS & AI Compendium — 一本由 AI 从业者写给自己看的开源数理教材

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 5.3k | 112 | TypeScript | Apache-2.0 |

这是一本开源在线教材，作者 Henry Ndubuaku 把自己多年在 AI/ML 行业工作积累的笔记整理成 20 章内容，从向量、矩阵、微积分、概率统计这些基础数学讲起，一路铺到机器学习、计算语言学、计算机视觉、多模态学习、图神经网络，再到 GPU 编程、AI 推理优化和 ML 系统设计。

和传统教材不同，它刻意强调"直觉优先、真实场景、不含糊"，尽量少堆数学符号。仓库里还带了一个 MCP 服务器，克隆到本地后，Claude Code、Cursor 等 AI 助手可以直接把这本教材当知识库来查询和引用。作者提到，几位朋友用这份笔记准备 DeepMind、OpenAI、Nvidia 的面试并成功入职，作者本人也在去年被 Y Combinator 录取。

适合已经掌握基础数学和 Python、想系统补齐 AI 工程知识但不想啃传统教材的从业者或学生。

🔗 项目地址：https://github.com/HenryNdubuaku/maths-cs-ai-compendium

---

## 今日观察

今天上榜的三个 AI 相关项目形态各异——一个是安全钩子，一个是设计技能，一个是教材——但共同点很明确：都是围绕"如何更好地和 AI 编程助手协作"展开，而不是训练模型本身。AI coding agent 的安全边界、审美水平和知识背景，正在变成三个各自独立的产品方向。

---

**Tags**：#GitHub热点 #AI开源 #AI编程助手 #MCP #设计技能
