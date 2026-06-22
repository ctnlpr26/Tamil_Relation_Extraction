# tests_manual/test_end_to_end_manual.py

from pipeline.extraction_pipeline import (
    ExtractionPipeline
)

pipeline = ExtractionPipeline()

document = """
யாழ்ப்பாண போதனா வைத்தியசாலையில் டாக்டர் கந்தசாமி அவர்கள் சுகாதார அமைச்சு அதிகாரிகளுடன் ஆலோசனை நடத்தினார்."""

triples = pipeline.run(document)

for triple in triples:
    print(triple)