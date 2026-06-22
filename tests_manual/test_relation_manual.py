# tests/test_relation_manual.py

from pipeline.relation_stage import RelationStage

stage = RelationStage()

sentence = """
[E1] சாம்பசிவம் [/E1]
[E2] யாழ்ப்பாணம் [/E2]
வாழ்ந்தார்
"""

result = stage.predict(sentence)

print(result)