from domain.entity_pair import EntityPair
from domain.relation_prediction import RelationPrediction
from domain.triple import Triple


class TripleBuilder:

    def build(
        self,
        pair: EntityPair,
        relation: RelationPrediction
    ) -> Triple:

        # return Triple(
        #     subject=pair.entity1.text,
        #     predicate=relation.relation,
        #     object=pair.entity2.text
        # )
        return Triple(
            subject=pair.entity1.text,
            subject_type=pair.entity1.label,

            predicate=relation.relation,

            object=pair.entity2.text,
            object_type=pair.entity2.label
        )