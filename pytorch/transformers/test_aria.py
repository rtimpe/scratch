from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    AriaForConditionalGeneration,
)
from transformers.generation.configuration_utils import CompileConfig
import torch

model_name = "rhymes-ai/Aria"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AriaForConditionalGeneration.from_pretrained(
    model_name, device_map="cpu", torch_dtype=torch.bfloat16
)

messages = [
    {"role": "user", "content": "Write a Python function is_prime(n). Keep it short."},
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
model.compile(fullgraph=False, backend="eager", dynamic=True)

inputs = tokenizer(text, return_tensors="pt").to(model.device)

out = model(**inputs)

print(out[0], out[0].shape)
