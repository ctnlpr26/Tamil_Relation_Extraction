# tests/test_pair_generator.py

from pipeline.pair_generator import PairGenerator
from domain.entity import Entity


def test_person_org_pair():

    generator = PairGenerator()

    entities = [
        Entity(
            text="சாம்பசிவம்",
            label="PERSON",
            start=0,
            end=10
        ),
        Entity(
            text="நாவலம்",
            label="ORG",
            start=15,
            end=25
        )
    ]

    pairs = generator.generate(entities)

    assert len(pairs) == 1


def test_person_location_pair():

    generator = PairGenerator()

    entities = [
        Entity(
            text="சாம்பசிவம்",
            label="PERSON",
            start=0,
            end=10
        ),
        Entity(
            text="யாழ்ப்பாணம்",
            label="LOCATION",
            start=15,
            end=25
        )
    ]

    pairs = generator.generate(entities)

    assert len(pairs) == 1
  


def test_org_location_pair():

    generator = PairGenerator()

    entities = [
        Entity(
            text="நாவலம்",
            label="ORG",
            start=0,
            end=10
        ),
        Entity(
            text="யாழ்ப்பாணம்",
            label="LOCATION",
            start=15,
            end=25
        )
    ]

    pairs = generator.generate(entities)

    assert len(pairs) == 1