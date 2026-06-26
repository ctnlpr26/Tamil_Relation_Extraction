# tests_manual/test_old_ner_style.py

from transformers import AutoTokenizer
from transformers import AutoModelForTokenClassification
from transformers import pipeline

MODEL_NAME = "exentai/SriLankan_Tamil_NER"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)

model = AutoModelForTokenClassification.from_pretrained(
    MODEL_NAME
)

ner_pipeline = pipeline(
    "token-classification",
    model=model,
    tokenizer=tokenizer,
    aggregation_strategy="simple"
)

text = """
சாம்பசிவம் யாழ்ப்பாணத்தில் வாழ்ந்தார்.
யாழ்ப்பாண போதனா வைத்தியசாலையில் டாக்டர் கந்தசாமி அவர்கள் சுகாதார அமைச்சு அதிகாரிகளுடன் ஆலோசனை நடத்தினார்.
"""

results = ner_pipeline(text)

print("\n========== OLD STYLE OUTPUT ==========\n")

for item in results:

    entity_text = text[
        item["start"]:item["end"]
    ]

    print({
        "text": entity_text,
        "label": item["entity_group"],
        "score": float(item["score"])
    })