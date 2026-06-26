from domain.triple import Triple

from knowledge_graph.graph_loader import (
    GraphLoader
)

loader = GraphLoader()

triple = Triple(
    subject="சாம்பசிவம்",
    subject_type="PERSON",

    predicate="LIVED_IN",

    object="யாழ்ப்பாணம்",
    object_type="LOCATION"
)

loader.insert(
    triple
)

print(
    "Triple inserted."
)