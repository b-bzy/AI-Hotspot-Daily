<!--
标题候选：
1. 今日 GitHub AI 热点：Trending 日榜里 AI 新面孔只剩一个
2. AutoGPT 登顶今日 AI 项目，另两个非 AI 项目同样值得关注
3. 今日 GitHub 热点：3 个项目 24 小时新增合计超 300 star
当前正在使用：候选 1
-->

# 今日 GitHub AI 热点：Trending 日榜里 AI 新面孔只剩一个

> 今天的 GitHub Daily Trending 上，多数高星位置被 AI Agent、Skills 框架类项目占据，但按 90 天去重后大多是老面孔，剩下的新 AI 候选只有 Significant-Gravitas/AutoGPT 一个。另两个位置按 24 小时新增 star 倒序，从非 AI 项目里补上了 goauthentik/authentik 和 TapXWorld/ChinaTextbook。

---

## 1. AutoGPT — 从命令行智能体到可视化 Agent 搭建平台

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 186k | 37 | Python | MIT（classic）/ Polyform Shield（platform） |

AutoGPT 最早是 2023 年那波"自主智能体"实验的代表项目，如今已经演化成一套完整的 Agent 构建与运行平台：用户可以用自然语言描述一个任务目标，系统把对话转成能重复执行的智能体，支持按需触发或定时运行。

项目分两部分维护：`classic/` 目录保留最早的单智能体命令行实现，继续沿用 MIT 协议；新的 `autogpt_platform/` 是可视化搭建、市场化分发的完整平台，单独采用 Polyform Shield 协议——允许企业内部使用，但限制第三方拿它做同类托管服务。平台已接入 Gmail、Slack、GitHub、Notion 等 45 个以上外部服务，智能体可以直接调用这些服务完成任务。

适合想把重复性工作流（比如晨会简报、销售调研、客服草稿）交给智能体处理、又不想从零搭 Agent 框架的团队。

🔗 项目地址：https://github.com/Significant-Gravitas/AutoGPT

---

## 2. authentik — 自建身份认证网关，替代第三方 SSO 服务商

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 23.2k | 138 | Python | MIT（核心代码） |

authentik 是一个开源身份提供方（IdP），把 SAML、OAuth2/OIDC、LDAP、RADIUS 几种登录协议统一收进一套系统。企业可以用它自建单点登录，不用把员工账号数据交给 Okta、Auth0 这类第三方服务商。

部署方式覆盖从个人实验环境到生产级 Kubernetes 集群：Docker Compose 用于测试和小规模场景，Helm Chart 面向大规模生产环境，另外提供 AWS CloudFormation 模板和 DigitalOcean 一键安装。项目同时维护开源版和企业版，企业版面向要从 Okta、Auth0、Entra ID 迁移评估的团队，提供额外支持。

适合已经在用第三方 IdP、但想把认证系统迁回自有基础设施、对数据主权有要求的团队。

🔗 项目地址：https://github.com/goauthentik/authentik

---

## 3. ChinaTextbook — 把中小学到大学的 PDF 教材集中开源

| 总 Star | 24h 新增 | 主语言 | 协议 |
|---|---|---|---|
| 77.2k | 134 | Roff | 未附 LICENSE 文件 |

这是一个纯资源型仓库，把小学到大学的数学教材 PDF 按年级、学期、版本分类整理并公开托管。发起者在 README 里给出的初衷是：国内教育网站的资源本该免费，却常被人加水印转卖，仓库希望把这类资源集中开源，也方便海外华人子女保留国内教材资源。

因为单个 PDF 文件经常超过 GitHub 100MB 的上传上限，仓库把大文件切成 35MB 一份的分卷，并提供配套的 Windows 合并工具 `mergePDFs-windows-amd64.exe`，下载后放进分卷目录双击即可拼回完整文件。国内访问慢的用户可以用作者另一个项目 `tchMaterial-parser` 重新下载原始资源。

适合需要免费获取标准版教材、或者在海外想让孩子跟上国内教学进度的家庭。

🔗 项目地址：https://github.com/TapXWorld/ChinaTextbook

---

## 今日观察

今天的日榜里，AI Agent、Skills 框架类项目占了大半个版面，但这个方向在过去一个多月被密集覆盖过，90 天去重后反而只剩 AutoGPT 一个新面孔。剩下两个位置被身份认证、教育资源这类"老需求"项目补上，说明基础设施和资源整理类仓库依然有稳定的日增长曲线，不完全靠 AI 热点驱动。

---

**Tags**：#GitHub热点 #AI开源 #AIAgent #身份认证 #开源教育资源
