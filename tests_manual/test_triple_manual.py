from pipeline.triple_builder import TripleBuilder

from domain.entity import Entity
from domain.entity_pair import EntityPair
from domain.relation_prediction import RelationPrediction


builder = TripleBuilder()

pair = EntityPair(
    Entity(
        "சாம்பசிவம்",
        "PERSON",
        0,
        10
    ),
    Entity(
        "யாழ்ப்பாணம்",
        "LOCATION",
        15,
        25
    )
)

relation = RelationPrediction(
    "LIVED_IN",
    0.95
)

triple = builder.build(
    pair,
    relation
)

print(triple)