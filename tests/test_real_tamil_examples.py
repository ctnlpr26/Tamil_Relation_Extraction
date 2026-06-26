from pipeline.extraction_pipeline import (
    ExtractionPipeline
)

pipeline = ExtractionPipeline()


def test_initials_person():

    document = """
    சாம்.ஏ.சபாபதி யாழ்ப்பாணத்தில் வாழ்ந்தார்.
    """

    triples = pipeline.run(document)

    assert isinstance(triples, list)


def test_doctor_person():

    document = """
    டாக்டர் கந்தசாமி யாழ்ப்பாண போதனா வைத்தியசாலையில் பணியாற்றினார்.
    """

    triples = pipeline.run(document)

    assert isinstance(triples, list)


def test_professor_person():

    document = """
    பேராசிரியர் கார்த்திகேசு சிவத்தம்பி இலங்கைப் பல்கலைக்கழகத்தில் கற்பித்தார்.
    """

    triples = pipeline.run(document)

    assert isinstance(triples, list)


def test_author_book_relation():

    document = """
    சாம்.ஏ.சபாபதி தமிழர் வரலாறு என்ற நூலை எழுதியுள்ளார்.
    """

    triples = pipeline.run(document)

    assert isinstance(triples, list)


def test_person_organization():

    document = """
    கந்தையா கணேஷ் நாவலர் கலாச்சார மையத்தில் பணியாற்றினார்.
    """

    triples = pipeline.run(document)

    assert isinstance(triples, list)