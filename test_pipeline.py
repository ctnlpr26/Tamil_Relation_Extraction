from pipeline.sentence_splitter import SentenceSplitter

splitter = SentenceSplitter()

document = """
சாம்பசிவம் நாவலத்திற்கு பங்களித்தார்.
அவர் யாழ்ப்பாணத்தில் வாழ்ந்தார்.
அவர் ஆசிரியராக பணியாற்றினார்.
"""

sentences = splitter.split(document)

for idx, sentence in enumerate(sentences, start=1):
    print(f"{idx}. {sentence}")