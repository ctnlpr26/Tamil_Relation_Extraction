
from itertools import combinations

from domain.entity_pair import EntityPair
from schemas.relation_schema import ALLOWED_ENTITY_PAIRS


class PairGenerator:

    def generate(self, entities):

        candidate_pairs = []

        for entity1, entity2 in combinations(entities, 2):

            pair_type = (
                entity1.label,
                entity2.label
            )

            if pair_type in ALLOWED_ENTITY_PAIRS:

                candidate_pairs.append(
                    EntityPair(
                        entity1=entity1,
                        entity2=entity2
                    )
                )

        return candidate_pairs