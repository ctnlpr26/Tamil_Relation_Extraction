# tests/test_entity_marker.py

from pipeline.entity_marker import EntityMarker
from domain.entity import Entity


def test_entity_marking():

    marker = EntityMarker()

    sentence = (
        "சாம்பசிவம் நாவலத்திற்கு பங்களித்தார்."
    )

    entity1 = Entity(
        text="சாம்பசிவம்",
        label="PERSON",
        start=0,
        end=10
    )

    entity2 = Entity(
        text="நாவலம்",
        label="ORG",
        start=11,
        end=18
    )

    result = marker.mark(
        sentence,
        entity1,
        entity2
    )

    assert "[E1]" in result
    assert "[E2]" in result

def test_entity_text_preserved():

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

    result = marker.mark(
        sentence,
        entity1,
        entity2
    )

    assert "சாம்பசிவம்" in result
    assert "யாழ்ப்பாணம்" in result

def test_e1_before_e2():

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

    result = marker.mark(
        sentence,
        entity1,
        entity2
    )

    assert result.count("[E1]") == 1
    assert result.count("[E2]") == 1