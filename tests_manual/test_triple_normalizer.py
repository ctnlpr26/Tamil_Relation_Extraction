from domain.triple import Triple

from normalization.triple_normalizer import (
    TripleNormalizer
)


normalizer = TripleNormalizer()

triple = Triple(

    subject="சாம்பசிவம்",
    subject_type="PERSON",

    predicate="LIVED_IN",

    object="யாழ்ப்பாணத்தில்",
    object_type="LOCATION"

)

normalized = normalizer.normalize(
    triple
)

print()

print("Original")

print(triple)

print()

print("Normalized")

print(normalized)