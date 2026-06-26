from pipeline.kg_extraction_pipeline import (
    KGExtractionPipeline
)

pipeline = KGExtractionPipeline()

# document = """
# சாம்.ஏ.சபாபதி யாழ்ப்பாணத்தில் வாழ்ந்தார்
# """

document = """
சாம்.ஏ.சபாபதி யாழ்ப்பாணத்தில் வாழ்ந்தார். சாம்.ஏ.சபாபதி யாழ்ப்பாண நூலகத்தின் உருவாக்கத்தில் பிரதானமான பங்களிப்புச்செய்தார். 
யாழ்ப்பாணம் இலங்கையின் வடக்கே உள்ளது.

"""

triples = pipeline.run(
    document
)

for triple in triples:

    print(triple)