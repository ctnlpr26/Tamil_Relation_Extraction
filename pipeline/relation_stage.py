# pipeline/relation_stage.py

from models.relation.labels import RELATIONS
from models.relation.relation_model import get_relation_model
from domain.relation_prediction import RelationPrediction

class RelationStage:

    def __init__(self):

        self.model = get_relation_model()

    def predict(
        self,
        marked_sentence
    ):

        result = self.model.predict(
            marked_sentence,
            RELATIONS
        )

        return RelationPrediction(
            relation=result["labels"][0],
            confidence=float(result["scores"][0])
        )