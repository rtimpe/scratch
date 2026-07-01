from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.configuration_utils import CompileConfig

model_name = "deepreinforce-ai/Ornith-1.0-9B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    dtype="auto",
    device_map="auto",
)

messages = [
    {"role": "user", "content": "Write a Python function is_prime(n). Keep it short."}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
model.compile(fullgraph=False, backend='eager')

inputs = tokenizer(text, return_tensors="pt").to(model.device)

out = model(**inputs)

print(out[0])
# generated = model.generate(
#     **inputs,
#     max_new_tokens=512,
#     do_sample=True,
#     temperature=0.6,
#     top_p=0.95,
#     top_k=20,
#     compile_config=compile_config,
#     cache_implementation='static',
# )
# output_ids = generated[0][inputs.input_ids.shape[1]:]

# # The reply contains a <think> ... </think> reasoning block followed by the answer.
# content = tokenizer.decode(output_ids, skip_special_tokens=True)
