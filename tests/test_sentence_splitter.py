# tests/test_sentence_splitter.py

from pipeline.sentence_splitter import SentenceSplitter

def test_single_sentence():
    splitter = SentenceSplitter()

    text = "சாம்பசிவம் நாவலத்திற்கு பங்களித்தார்."

    result = splitter.split(text)

    assert len(result) == 1
    assert result[0] == text


def test_two_sentences():
    splitter = SentenceSplitter()

    text = (
        "சாம்பசிவம் நாவலத்திற்கு பங்களித்தார். "
        "அவர் யாழ்ப்பாணத்தில் வாழ்ந்தார்."
    )

    result = splitter.split(text)

    assert len(result) == 2


def test_three_sentences():
    splitter = SentenceSplitter()

    text = (
        "சாம்பசிவம் நாவலத்திற்கு பங்களித்தார். "
        "அவர் யாழ்ப்பாணத்தில் வாழ்ந்தார். "
        "அவர் ஆசிரியராக பணியாற்றினார்."
    )

    result = splitter.split(text)

    assert len(result) == 3


def test_empty_document():
    splitter = SentenceSplitter()

    result = splitter.split("")

    assert result == []


def test_whitespace_document():
    splitter = SentenceSplitter()

    result = splitter.split("    ")

    assert result == []


def test_newline_sentences():
    splitter = SentenceSplitter()

    text = (
        "சாம்பசிவம் நாவலத்திற்கு பங்களித்தார்.\n"
        "அவர் யாழ்ப்பாணத்தில் வாழ்ந்தார்."
    )

    result = splitter.split(text)

    assert len(result) == 2

def test_paragraph_three_sentences():
    splitter = SentenceSplitter()

    text = (
        "சாம்பசிவம் நாவலத்திற்கு பங்களித்தார். அவர் யாழ்ப்பாணத்தில் வாழ்ந்தார். அவர் ஆசிரியராக பணியாற்றினார்."
    )

    result = splitter.split(text)

    assert len(result) == 3

    assert result == [
        "சாம்பசிவம் நாவலத்திற்கு பங்களித்தார்.",
        "அவர் யாழ்ப்பாணத்தில் வாழ்ந்தார்.",
        "அவர் ஆசிரியராக பணியாற்றினார்."
    ]

def test_trim_spaces():
    splitter = SentenceSplitter()

    text = "   சாம்பசிவம் நாவலத்திற்கு பங்களித்தார்.   "

    result = splitter.split(text)

    assert result == [
        "சாம்பசிவம் நாவலத்திற்கு பங்களித்தார்."
    ]

def test_multiple_spaces():
    splitter = SentenceSplitter()

    text = (
        "சாம்பசிவம் நாவலத்திற்கு பங்களித்தார்.     "
        "அவர் யாழ்ப்பாணத்தில் வாழ்ந்தார்."
    )

    result = splitter.split(text)

    assert len(result) == 2


def test_question_mark():
    splitter = SentenceSplitter()

    text = (
        "அவர் யார்? "
        "அவர் ஆசிரியர்."
    )

    result = splitter.split(text)

    assert len(result) == 2

def test_exclamation_mark():
    splitter = SentenceSplitter()

    text = (
        "அருமை! "
        "அவர் வெற்றி பெற்றார்."
    )

    result = splitter.split(text)

    assert len(result) == 2