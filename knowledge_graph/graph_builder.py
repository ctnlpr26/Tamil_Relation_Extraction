from knowledge_graph.graph_schema import (
    ENTITY_TO_NODE
)


class GraphBuilder:

    def build(self, triple):

        return {

            "subject": triple.subject,
            "subject_label":
                ENTITY_TO_NODE[
                    triple.subject_type
                ],

            "relation":
                triple.predicate,

            "object":
                triple.object,

            "object_label":
                ENTITY_TO_NODE[
                    triple.object_type
                ]
        }