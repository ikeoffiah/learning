import replicate
import os

os.environ['REPLICATE_API_TOKEN'] = "r8_XlcwqXy1gORmEIFXXq73D2Rj02UXoQn1WJtbS"

# The meta/llama-2-13b-chat model can stream output as it's running.
for event in replicate.stream(
    "meta/llama-2-13b-chat",
    input={
        "debug": False,
        "top_k": 50,
        "top_p": 1,
        "prompt": "Please what do you sell ?",
        "temperature": 0.75,
        "system_prompt": "Salu is an orange selling entrepreneur, she sells her oranges for 500 naira for 3 bundle. At most she give 10% discounts to her customers but mostly, she doesn't. Please serve as a customer service agent for Salu",
        "max_new_tokens": 500,
        "min_new_tokens": -1
    },
):
    print(str(event), end="")