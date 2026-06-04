import torch
from transformers import pipeline
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    BitsAndBytesConfig,
)


def main():
    model_name = "ibm-granite/granite-4.0-tiny-preview"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="cpu",
    )
    model.eval()
    input_text = """A list of colors: red, blue"""
    input_ids = tokenizer(input_text, return_tensors="pt").to(model.device)
    model.compile(fullgraph=True)

    output = model.generate(**input_ids, max_new_tokens=10)
    print(tokenizer.decode(output[0], skip_special_tokens=True))


if __name__ == "__main__":
    main()
