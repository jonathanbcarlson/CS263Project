# CS 263 Project

- Project for Spring 2024 by Nanyung (Violet) Peng
- Examining LLM's performance on interdomain commonsense reasoning across
  spatial, temporal, and physical domains

## Project structure

- The prompts for each combination of commonsense reasoning are in
  `<domain-combination>/<domain-combination>.json`.
- The `chatgpt-api, gemini, llama3_8b` are for calling the LLMs APIs.
- `result_calculations` creates the plots showing how the different LLMs perform
  on the different commonsense reasoning prompts using the human evaluation as
  the ground truth.

```
.
├── chatgpt-api # used to call OpenAI API for GPT-3.5/4o
│   └── chatgpt-api-prompt.ipynb
├── gemini # used to call Gemini API for Gemini 1.5 Flash/Pro
│   └── gemini_api.ipynb
├── llama3_8b # used to call Ollama for llama3:8b model
│   └── eval_llama3_8b.py
├── physical-temporal # physical-temporal prompts
│   ├── backgrounds.txt # the background for each prompt provided to the model
│   ├── generate_prompts.py # script to create the prompt from backgrounds and options
│   ├── human_annotations.txt # human created ground truth for prompts
│   ├── options.txt # what options the LLM can choose for each prompt
│   └── physical-temporal.json # physical-temporal prompts with LLM responses
├── result_calculations # create plots for LLMs results
│   ├── calculateLLMStats.ipynb # use human evaluation as ground truth
│   └── figures # result figures
├── spatial-physical # spatial-physical prompts: same format as physical-temporal
│   ├── backgrounds.txt
│   ├── generate_prompts.py
│   ├── human_annotations.txt
│   ├── options.txt
│   └── spatial-physical.json # spatial-physical prompts with LLM responses
├── spatial-temporal # spatial-temporal prompts: same format as physical-temporal
│   ├── backgrounds.txt
│   ├── generate_prompts.py
│   ├── human_annotations.txt
│   ├── options.txt
│   └── spatial-temporal.json # spatial-temporal prompts with LLM responses
└── spatial-temporal-physical # used to generate spatial-temporal-physical prompts
    ├── README.md
    ├── create_prompt.py # create random STP prompt combinations
    └── spatial-temporal-physical.json # STP prompts with LLM responses
```

## Dependencies

- [OpenAI API key](https://platform.openai.com/docs/quickstart)
- [Gemini API key](https://ai.google.dev/gemini-api/docs/api-key)
- [Ollama](https://ollama.ai/)
