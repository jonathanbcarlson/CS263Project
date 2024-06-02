import json
from tqdm import tqdm
import urllib.request

ollama_url = "http://localhost:11434/api/generate"


def get_llm_output(prompt: str):
    params = {"model": "llama3:8b", "prompt": prompt, "stream": False}
    params = json.dumps(params).encode("utf8")
    # from https://stackoverflow.com/a/25491579/14842908
    req = urllib.request.Request(
        ollama_url, data=params, headers={"content-type": "application/json"}
    )
    response = urllib.request.urlopen(req)
    response_dict = json.loads(response.read().decode("utf8"))
    response_txt = response_dict["response"]
    return response_txt


prompt_dirs = [
    "spatial-physical",
    "physical-temporal",
    "spatial-temporal",
    "spatial-temporal-physical",
]

for dir in prompt_dirs:
    prompts_json_filename = f"../{dir}/{dir}.json"
    with open(prompts_json_filename, "r") as prompts_file:
        prompts = json.load(prompts_file)
        for prompt in tqdm(prompts):
            llm_out = get_llm_output(prompt["prompt"])
            prompt["responses"]["llama3:8b"] = llm_out
    with open(prompts_json_filename, "w") as new_prompts_file:
        json.dump(prompts, new_prompts_file, indent=2, ensure_ascii=False)
