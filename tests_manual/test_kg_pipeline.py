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
ஐக்கிய சங்க ஆசுபத்திரித் தொண்டின் ஆரம்ப முயற்சிகள் ஸ்ரீமான் K. கனகரத்தினம் அவர்கள் 2110 53 ல் இலங்கை றேடியோவில் நிகழ்த்திய சொற்பொழிவு. 

"""

triples = pipeline.run(
    document
)

for triple in triples:

    print(triple)