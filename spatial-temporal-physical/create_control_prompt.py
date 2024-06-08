import json

def generate_control():
    control_prompts = []
    with open("spatial-temporal-physical.json", encoding="utf-8") as f:
        prompt_entries = json.load(f)
        for entry in prompt_entries:
            prompt = entry["prompt"]
            control_text = prompt.split("?")[1].strip()
            control_prompts.append({
                "prompt": control_text,
                "human_annotation": entry["human_annotation"]
            })

    with open("spatial-temporal-physical-control.json", "w", encoding="utf-8") as output_file:
        json.dump(control_prompts, output_file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    generate_control()
