# test_pair_manual.py

from pipeline.pair_generator import PairGenerator
from domain.entity import Entity


entities = [
    Entity("சாம்பசிவம்", "PERSON", 0, 10),
    Entity("நாவலம்", "ORG", 20, 30),
    Entity("யாழ்ப்பாணம்", "LOCATION", 40, 50)
]

generator = PairGenerator()

pairs = generator.generate(entities)

for e1, e2 in pairs:
    print(
        e1.text,
        e1.label,
        " --> ",
        e2.text,
        e2.label
    )