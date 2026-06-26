from pipeline.extraction_pipeline import (
    ExtractionPipeline
)

pipeline = ExtractionPipeline()

examples = [

    "சாம்.ஏ.சபாபதி யாழ்ப்பாணத்தில் வாழ்ந்தார்.",

    "கா.சிவத்தம்பி யாழ்ப்பாணப் பல்கலைக்கழகத்தில் கற்பித்தார்.",

    "டாக்டர் கந்தசாமி யாழ்ப்பாண போதனா வைத்தியசாலையில் பணியாற்றினார்.",

    "விபுலாநந்த அடிகள் இலங்கையில் தமிழ் கல்விக்காக பங்களித்தார்.",

    "கந்தையா கணேஷ் நாவலர் கலாச்சார மையத்தில் பணியாற்றினார்."
]

for text in examples:

    print("\n" + "=" * 80)
    print(text)
    print("=" * 80)

    triples = pipeline.run(text)

    for triple in triples:
        print(triple)