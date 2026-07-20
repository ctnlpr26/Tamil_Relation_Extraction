# pipeline/relation_stage.py

# from models.relation.labels import RELATIONS
# from models.relation.relation_model import get_relation_model
# from domain.relation_prediction import RelationPrediction

# from schemas.relation_schema_loader import (
#     RelationSchemaLoader
# )

# loader = RelationSchemaLoader()

# class RelationStage:

#     def __init__(self):

#         self.model = get_relation_model()

#     def predict(
#         self,
#         marked_sentence
#     ):

#         result = self.model.predict(
#             marked_sentence,
#             RELATIONS
#         )

#         return RelationPrediction(
#             relation=result["labels"][0],
#             confidence=float(result["scores"][0])
#         )

# pipeline/relation_stage.py

from domain.relation_prediction import (
    RelationPrediction
)

from models.relation.relation_model import (
    get_relation_model
)

from schemas.relation_schema_loader import (
    RelationSchemaLoader
)


class RelationStage:

    def __init__(self):

        self.model = get_relation_model()

        self.schema_loader = (
            RelationSchemaLoader()
        )

    def predict(
        self,
        sentence,
        entity1,
        entity2
    ):

        candidate_relations = (
            self.schema_loader.get_relations(
                entity1.label,
                entity2.label
            )
        )

        print(
            "Candidate Relations:",
            candidate_relations
        )

        result = self.model.predict(
            sentence,
            candidate_relations
        )

        return RelationPrediction(

            relation=result["labels"][0],

            confidence=float(
                result["scores"][0]
            )
        )