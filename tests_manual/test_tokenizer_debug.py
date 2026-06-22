# # tests_manual/test_tokenizer_debug.py

# from transformers import AutoTokenizer

# tokenizer = AutoTokenizer.from_pretrained(
#     "exentai/SriLankan_Tamil_NER"
# )

# text = "சாம்பசிவம்"

# tokens = tokenizer.tokenize(text)

# print(tokens)

# print(
#     tokenizer.convert_tokens_to_string(tokens)
# )

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "exentai/SriLankan_Tamil_NER"
)

text = "சாம்பசிவம்"

encoded = tokenizer(
    text,
    return_offsets_mapping=True
)

tokens = tokenizer.convert_ids_to_tokens(
    encoded["input_ids"]
)

for token, offset in zip(
    tokens,
    encoded["offset_mapping"]
):
    print(token, offset)