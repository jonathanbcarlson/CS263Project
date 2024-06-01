import json

instruction = "Please choose the most likely answer that fills in the blanks. Only respond with a single number 1, 2, 3, or 4."

def generate_prompts():
    prompts = []
    with open("backgrounds.txt") as backgrounds_f:
        with open("options.txt") as options_f:
            with open("human_annotations.txt") as human_annotations_f:
                backgrounds = backgrounds_f.readlines()
                options = options_f.read().split('|')
                annotations = human_annotations_f.readlines()
                for i in range(len(backgrounds)):
                    background = backgrounds[i].strip()
                    options_block = options[i].strip()
                    annotation = int(annotations[i])
                    prompts.append({
                        "prompt": f"{background}\n{options_block}\n{instruction}",
                        "human_annotation": annotation
                    })
    with open("spatial-temporal.json", "w", encoding="utf-8") as output_file:
        json.dump(prompts, output_file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    generate_prompts()