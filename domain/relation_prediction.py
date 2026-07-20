from dataclasses import dataclass

@dataclass
class RelationPrediction:
    relation: str
    confidence: float