# tests_manual/test_ner_pipeline_debug.py

from pipeline.ner_stage import NERStage

ner = NERStage()

text = """
சாம்பசிவம் யாழ்ப்பாணத்தில் வாழ்ந்தார்.
யாழ்ப்பாண போதனா வைத்தியசாலையில் டாக்டர் கந்தசாமி அவர்கள் சுகாதார அமைச்சு அதிகாரிகளுடன் ஆலோசனை நடத்தினார்.
"""

entities = ner.extract(text)

print("\n========== ENTITIES ==========\n")

for entity in entities:

    print(f"TEXT      : {entity.text}")
    print(f"LABEL     : {entity.label}")
    print(f"START-END : {entity.start} - {entity.end}")

    if entity.end < len(text):
        print(
            "NEXT CHAR :",
            repr(text[entity.end])
        )

    print("-" * 50)