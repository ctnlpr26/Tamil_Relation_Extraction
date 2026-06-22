from models.ner.ner_model import TamilNERModel

model = TamilNERModel()

result = model.predict(
    "சாம்பசிவம் யாழ்ப்பாணத்தில் வாழ்ந்தார்."
)

for r in result:
    print(r)