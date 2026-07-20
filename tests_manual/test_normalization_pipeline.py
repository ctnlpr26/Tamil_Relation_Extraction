from pipeline.ner_stage import (
    NERStage
)

ner = NERStage()

sentence = (

    "சாம்பசிவம் யாழ்ப்பாணத்தில் வாழ்ந்தார்."

)

entities = ner.extract(sentence)

print()

print("=" * 50)

for entity in entities:

    print()

    print("Original :", entity.original_text)

    print("Lemma    :", entity.lemma)

    print("Label    :", entity.label)