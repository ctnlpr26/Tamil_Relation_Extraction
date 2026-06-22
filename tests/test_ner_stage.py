# tests/test_ner_stage.py

from pipeline.ner_stage import NERStage


def test_extract_returns_list():

    ner = NERStage()

    result = ner.extract(
        "சாம்பசிவம் யாழ்ப்பாணத்தில் வாழ்ந்தார்."
    )

    assert isinstance(result, list)


def test_empty_sentence():

    ner = NERStage()

    result = ner.extract("")

    assert isinstance(result, list)


def test_entity_has_required_fields():

    ner = NERStage()

    result = ner.extract(
        "சாம்பசிவம் யாழ்ப்பாணத்தில் வாழ்ந்தார்."
    )

    for entity in result:

        assert hasattr(entity, "text")
        assert hasattr(entity, "label")
        assert hasattr(entity, "start")
        assert hasattr(entity, "end")


def test_no_crash_with_random_text():

    ner = NERStage()

    result = ner.extract(
        "asdfghjkl"
    )

    assert isinstance(result, list)


def test_no_crash_with_numbers():

    ner = NERStage()

    result = ner.extract(
        "12345"
    )

    assert isinstance(result, list)