import json

instruction = "Please choose the most likely answer that fills in the blanks. Please ONLY respond with a single number 1, 2, 3, or 4. NO punctuation."

def generate_prompts():
    prompts = []
    with open("options.txt") as options_f:
        with open("human_annotations.txt") as human_annotations_f:
            options = options_f.read().split('|')
            annotations = human_annotations_f.readlines()
            for i in range(len(options)):
                options_block = options[i].strip()
                annotation = int(annotations[i])
                prompts.append({
                    "prompt": f"{options_block}\n{instruction}",
                    "human_annotation": annotation
                })
    with open("spatial-temporal-control.json", "w", encoding="utf-8") as output_file:
        json.dump(prompts, output_file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    generate_prompts()