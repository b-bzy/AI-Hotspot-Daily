<div align="center" style="margin-bottom: 1em;">

<img src="./docs/assets/images/logo-light-mode.svg#gh-light-mode-only" alt="Outlines Logo" width=300></img>
<img src="./docs/assets/images/logo-dark-mode.svg#gh-dark-mode-only" alt="Outlines Logo" width=300></img>


 🗒️ *Structured outputs for LLMs* 🗒️

Made with ❤👷️ by the team at [.txt](https://dottxt.co)
<br>Trusted by NVIDIA, Cohere, HuggingFace, vLLM, etc.

<!-- Project Badges -->
[![PyPI Version][pypi-version-badge]][pypi]
[![Downloads][downloads-badge]][pypistats]
[![Stars][stars-badge]][stars]

<!-- Community Badges -->
[![Discord][discord-badge]][discord]
[![Blog][dottxt-blog-badge]][dottxt-blog]
[![Twitter][twitter-badge]][twitter]

<br>The .txt API is currently in early access. **[Request access here →](https://h1xbpbfsf0w.typeform.com/to/fwQNWmS8?utm_source=github&utm_medium=organic&utm_campaign=outlines)**


</div>

## 🚀 Building the future of structured generation

We're working with select partners to develop new interfaces to structured generation.

Need XML, FHIR, custom schemas or grammars? Let's talk.

Audit your schema: share one schema, we show you what breaks under generation, the constraints that fix it, and compliance rates before and after. Sign up [here](https://h1xbpbfsf0w.typeform.com/to/rtFUraA2?typeform).

## Table of Contents

- [Why Outlines?](#why-outlines)
- [Quickstart](#quickstart)
- [Real-World Examples](#real-world-examples)
  - [🙋‍♂️ Customer Support Triage](#customer-support-triage)
  - [📦 E-commerce Product Categorization](#e-commerce-product-categorization)
  - [📊 Parse Event Details with Incomplete Data](#parse-event-details-with-incomplete-data)
  - [🗂️ Categorize Documents into Predefined Types](#categorize-documents-into-predefined-types)
  - [📅 Schedule a Meeting with Function Calling](#schedule-a-meeting-with-function-calling)
  - [📝 Dynamically Generate Prompts with Re-usable Templates](#dynamically-generate-prompts-with-re-usable-templates)
- [They Use Outlines](#they-use-outlines)
- [Model Integrations](#model-integrations)
- [Core Features](#core-features)
- [Other Features](#other-features)
- [About .txt](#about-txt)
- [Community](#community)

<div align="center"><img src="./docs/assets/images/install.png" width=300></img></div>

## Why Outlines?

LLMs are powerful but their outputs are unpredictable. Most solutions attempt to fix bad outputs after generation using parsing, regex, or fragile code that breaks easily.

Outlines guarantees structured outputs during generation — directly from any LLM.

- **Works with any model** - Same code runs across OpenAI, Ollama, vLLM, and more
- **Simple integration** - Just pass your desired output type: `model(prompt, output_type)`
- **Guaranteed valid structure** - No more parsing headaches or broken JSON
- **Provider independence** - Switch models without changing code


### The Outlines Philosophy

<div align="center"><img src="./docs/assets/images/use_philosophy.png" width=300></img></div>

Outlines follows a simple pattern that mirrors Python's own type system. Simply specify the desired output type, and Outlines will ensure your data matches that structure exactly:

- For a yes/no response, use `Literal["Yes", "No"]`
- For numerical values, use `int`
- For complex objects, define a structure with a [Pydantic model](https://docs.pydantic.dev/latest/)

## Quickstart

Getting started with outlines is simple:

### 1. Install outlines

``` shell
pip install outlines
```

### 2. Connect to your preferred model

``` python
import outlines
from transformers import AutoTokenizer, AutoModelForCausalLM


MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
model = outlines.from_transformers(
    AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto"),
    AutoTokenizer.from_pretrained(MODEL_NAME)
)
```

### 3. Start with simple structured outputs

``` python
from typing import Literal
from pydantic import BaseModel


# Simple classificat