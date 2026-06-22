# tests/test_pair_generator_edge_cases.py

from pipeline.pair_generator import PairGenerator
from domain.entity import Entity
from domain.entity_pair import EntityPair


def test_empty_entity_list():

    generator = PairGenerator()

    pairs = generator.generate([])

    assert pairs == []


def test_single_entity():

    generator = PairGenerator()

    entities = [
        Entity(
            text="சாம்பசிவம்",
            label="PERSON",
            start=0,
            end=10
        )
    ]

    pairs = generator.generate(entities)

    assert pairs == []


def test_disallowed_pair():

    generator = PairGenerator()

    entities = [
        Entity(
            text="சாம்பசிவம்",
            label="PERSON",
            start=0,
            end=10
        ),
        Entity(
            text="ராஜா",
            label="PERSON",
            start=20,
            end=25
        )
    ]

    pairs = generator.generate(entities)

    assert len(pairs) == 0

def test_multiple_entities():

    generator = PairGenerator()

    entities = [
        Entity("சாம்பசிவம்", "PERSON", 0, 10),
        Entity("நாவலம்", "ORG", 20, 30),
        Entity("யாழ்ப்பாணம்", "LOCATION", 40, 50)
    ]

    pairs = generator.generate(entities)

    assert len(pairs) == 3

    assert isinstance(pairs[0], EntityPair)

    assert pairs[0].entity1.text == "சாம்பசிவம்"
    assert pairs[0].entity2.text == "நாவலம்"

    assert pairs[1].entity1.text == "சாம்பசிவம்"
    assert pairs[1].entity2.text == "யாழ்ப்பாணம்"

    assert pairs[2].entity1.text == "நாவலம்"
    assert pairs[2].entity2.text == "யாழ்ப்பாணம்"

def test_return_type():

    generator = PairGenerator()

    entities = [
        Entity("சாம்பசிவம்", "PERSON", 0, 10),
        Entity("நாவலம்", "ORG", 20, 30)
    ]

    pairs = generator.generate(entities)

    assert isinstance(pairs[0], EntityPair)