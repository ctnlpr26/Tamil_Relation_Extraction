# tests/test_relation_stage.py

from pipeline.relation_stage import RelationStage
from domain.relation_prediction import RelationPrediction



def test_prediction_format():

    relation_stage = RelationStage()

    sentence = """
    [E1] சாம்பசிவம் [/E1]
    [E2] யாழ்ப்பாணம் [/E2]
    வாழ்ந்தார்
    """

    result = relation_stage.predict(
        sentence
    )

    assert isinstance(
        result,
        RelationPrediction
    )

def test_confidence_range():

    relation_stage = RelationStage()

    sentence = """
    [E1] சாம்பசிவம் [/E1]
    [E2] யாழ்ப்பாணம் [/E2]
    வாழ்ந்தார்
    """

    result = relation_stage.predict(
        sentence
    )

    assert 0 <= result.confidence <= 1