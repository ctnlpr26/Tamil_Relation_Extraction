# tests_manual/test_offset_validation.py

from models.ner.ner_model import TamilNERModel

text = "சாம்பசிவம் யாழ்ப்பாணத்தில் வாழ்ந்தார்."

model = TamilNERModel()

preds = model.predict(text)

for p in preds:

    print("MODEL WORD:", p["word"])

    print(
        "OFFSET TEXT:",
        text[p["start"]:p["end"]]
    )

    print()