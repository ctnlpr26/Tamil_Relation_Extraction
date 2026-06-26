# tests_manual/test_raw_ner_model.py

from models.ner.ner_model import TamilNERModel

model = TamilNERModel()

text = """
யாழ்ப்பாண போதனா வைத்தியசாலையில் டாக்டர் கந்தசாமி அவர்கள் சுகாதார அமைச்சு அதிகாரிகளுடன் ஆலோசனை நடத்தினார்.
"""

predictions = model.predict(text)

print("\n========== RAW MODEL OUTPUT ==========\n")

for pred in predictions:
    print(pred)