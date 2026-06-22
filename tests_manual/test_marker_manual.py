# test_marker_manual.py

from pipeline.entity_marker import EntityMarker
from domain.entity import Entity

marker = EntityMarker()

sentence = (
    "சாம்பசிவம் யாழ்ப்பாணத்தில் வாழ்ந்தார்."
)

entity1 = Entity(
    "சாம்பசிவம்",
    "PERSON",
    0,
    10
)

entity2 = Entity(
    "யாழ்ப்பாணம்",
    "LOCATION",
    11,
    22
)

print(
    marker.mark(
        sentence,
        entity1,
        entity2
    )
)