from pipeline.triple_builder import TripleBuilder
from domain.entity import Entity
from domain.entity_pair import EntityPair
from domain.relation_prediction import RelationPrediction
from domain.triple import Triple


def test_build_triple():

    builder = TripleBuilder()

    pair = EntityPair(
        entity1=Entity(
            "சாம்பசிவம்",
            "PERSON",
            0,
            10
        ),
        entity2=Entity(
            "யாழ்ப்பாணம்",
            "LOCATION",
            15,
            25
        )
    )

    relation = RelationPrediction(
        relation="LIVED_IN",
        confidence=0.95
    )

    triple = builder.build(
        pair,
        relation
    )

    assert isinstance(
        triple,
        Triple
    )


def test_subject():

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

    assert triple.subject == "சாம்பசிவம்"


def test_predicate():

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

    assert triple.predicate == "LIVED_IN"


def test_object():

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

    assert triple.object == "யாழ்ப்பாணம்"