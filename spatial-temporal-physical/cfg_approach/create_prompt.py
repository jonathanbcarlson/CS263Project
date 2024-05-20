from textwrap import dedent
import random
import json
import copy


def create_prompt(
    transport_method_1: str,
    transport_method_2: str,
    transport_method_3: str,
    days_layer: int,
    destination: str,
    distance: int,
    duration_1: str,
    duration_2: str,
):
    prompt = f"""If I {transport_method_1} into the street and {days_layer} days later
    I find myself by the {destination} which is {distance} miles away.
    How could I have gotten to the {destination}?
    1. I {transport_method_2} for {duration_1}.
    2. I {transport_method_3} for {duration_2}.
    Please choose the most likely answer and only respond with the number 1 or 2.
    """
    prompt = dedent(prompt)
    return prompt


transport_methods = ["bike", "run", "sprint", "jog", "swim", "walk", "ride a horse"]
durations = ["a quarter of a day", "10 hours", "3 hours", "half a day", "1 hour"]
destinations = ["ocean", "mountains", "plains", "desert"]
days_later = list(range(100))
distances = list(range(100))
PROMPTS_JSON_FILENAME = "transport_spatial_temporal_physical_prompts.json"


def human_annotate_prompts(num_prompts_to_create):
    annotated_results = []
    while len(annotated_results) < num_prompts_to_create:
        transport_choices = random.sample(transport_methods, 3)
        duration_choices = random.sample(durations, 2)
        created_prompt = create_prompt(
            transport_method_1=transport_choices[0],
            transport_method_2=transport_choices[1],
            transport_method_3=transport_choices[2],
            days_layer=random.sample(days_later, 1)[0],
            destination=random.sample(destinations, 1)[0],
            distance=random.sample(distances, 1)[0],
            duration_1=duration_choices[0],
            duration_2=duration_choices[1],
        )
        print(created_prompt)
        human_annotation = int(
            input("enter human annotation (1 or 2) or 3 if ambiguous then hit enter\n")
        )
        if human_annotation == 3:
            continue
        annotated_results.append(
            {"prompt": created_prompt, "human_annotation": human_annotation}
        )
        print(f"So far have annotated {len(annotated_results)} prompts")
    with open(PROMPTS_JSON_FILENAME, "w") as output_json:
        json.dump(annotated_results, output_json, indent=2)


def llm_prompt_response(model_name: str):
    with open(PROMPTS_JSON_FILENAME, "r") as prompts_json_file:
        prompts = json.load(prompts_json_file)
    new_prompts = copy.deepcopy(prompts)
    for i, prompt in enumerate(prompts):
        print(prompt["prompt"])
        llm_response = int(input("enter chat response (1 or 2) then hit enter\n"))
        new_prompts[i]["responses"] = {model_name: llm_response}
    with open(PROMPTS_JSON_FILENAME, "w") as prompts_json_file:
        json.dump(new_prompts, prompts_json_file, indent=2)


if __name__ == "__main__":
    # human_annotate_prompts(10)
    llm_prompt_response("gpt4o_llm_response")
