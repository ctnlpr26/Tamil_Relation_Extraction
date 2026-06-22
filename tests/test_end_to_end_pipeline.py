# tests/test_end_to_end_pipeline.py

from pipeline.extraction_pipeline import (
    ExtractionPipeline
)


def test_pipeline_returns_list():

    pipeline = ExtractionPipeline()

    document = """
    சாம்பசிவம் யாழ்ப்பாணத்தில் வாழ்ந்தார்.
    """

    triples = pipeline.run(
        document
    )

    assert isinstance(
        triples,
        list
    )

def test_pipeline_not_none():

    pipeline = ExtractionPipeline()

    document = """
    சாம்பசிவம் யாழ்ப்பாணத்தில் வாழ்ந்தார்.
    """

    triples = pipeline.run(
        document
    )

    assert triples is not None

from domain.triple import Triple


def test_pipeline_triple_type():

    pipeline = ExtractionPipeline()

    document = """
    சாம்பசிவம் யாழ்ப்பாணத்தில் வாழ்ந்தார்.
    """

    triples = pipeline.run(
        document
    )

    for triple in triples:

        assert isinstance(
            triple,
            Triple
        )