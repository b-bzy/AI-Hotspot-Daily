# AI 相关性关键词打分表

> 用于判断一个 GitHub 仓库是否"AI 相关"。
> 对每个仓库的 `description` + `topics` + `name` + `README 前 50 行` 四个字段做匹配。
> 至少命中两类信号、得分 ≥ 3 才算 AI 相关。

---

## 打分规则

| 信号 | 权重 |
|---|---|
| description 命中下面任一关键词 | +2 |
| topics 命中下面任一标签 | +2 |
| 主语言是 Python 且 description 提到模型 / 数据 / 训练 / 推理 | +1 |
| 仓库名（owner/name）直接含 `gpt` / `llm` / `ai` / `claude` / `agent` 子串 | +1 |
| README 前 50 行出现 OpenAI / Anthropic / HuggingFace / Mistral / Llama 等公司或模型名 | +1 |

阈值：≥ 3 进入候选池。

---

## 关键词词表（命中即 +2）

### 通用 AI / ML
ai, llm, gpt, claude, llama, mistral, gemini, qwen, deepseek, phi, mixtral
agent, agentic, autonomous-agent, multi-agent
ml, machine-learning, deep-learning, neural, neural-network
transformer, attention, embedding, vector
rag, retrieval-augmented, knowledge-graph
prompt, prompt-engineering, prompting
chatbot, copilot, assistant
inference, fine-tuning, fine-tune, lora, qlora, peft
training, pretraining, post-training, rlhf, dpo
mlops, llmops

### 生成式
diffusion, stable-diffusion, sd, sdxl, flux
image-generation, video-generation, text-to-image, text-to-video
tts, asr, speech-synthesis, voice-cloning
multimodal, vision, vlm, vision-language

### 工具 / 框架
openai, anthropic, huggingface, hf
ollama, vllm, llama-cpp, lm-studio, gpt4all
langchain, llamaindex, haystack, dspy
crewai, autogen, smolagents
mcp, model-context-protocol

### 应用层
ai-coding, ai-agent, ai-app, ai-tool
chat-with, doc-qa, text-summariz

---

## Topics 标签（命中即 +2）

artificial-intelligence, machine-learning, deep-learning
llm, large-language-models, language-model
ai, gpt, chatgpt, openai, claude, anthropic
agent, ai-agent, autonomous-agent, multi-agent-systems
rag, retrieval-augmented-generation, vector-database
embedding, embeddings
transformer, transformers, attention
neural-network, neural-networks
mlops, llmops, ai-tools
prompt-engineering, prompts
diffusion-models, stable-diffusion, text-to-image
multimodal, vision-language-model
fine-tuning, peft, lora
nlp, natural-language-processing

---

## 反向词表（命中扣分 -2，避免误判）

- `ai` 出现在"airdrop / air / airline / airbnb"等非 AI 上下文（脚本里要做整词匹配，不是子串匹配）
- `agent` 出现在"user-agent / web-agent（不指 AI）/ http-agent"
- `agent` 出现在网络代理、SaltStack agent、监控 agent 等基础设施场景
- `vision` 出现在 computer-vision 之外的"愿景规划"语境（少见，但 README 可能踩到）

> 这一条主要靠 Claude 二判兜底。脚本只做基础整词匹配。

---

## 维护

- 新关键词随时往上加（每次跑完看看淘汰列表，有漏的词就补）
- 词表越长越严格不一定越好；保持 50–100 个高质量关键词即可
- 不需要做大小写敏感（脚本内统一 lowercase）
