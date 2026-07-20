# import json
# from pathlib import Path


# class RelationSchemaLoader:

#     def __init__(self):

#         path = Path(
#             "schemas/relation_schemas.json"
#         )

#         with open(path,
#                   encoding="utf-8") as f:

#             self.schemas = json.load(f)

#     def get_relations(
#             self,
#             entity1_type,
#             entity2_type
#     ):

#         key = (
#             f"{entity1_type}_{entity2_type}"
#         )

#         if key not in self.schemas:
#             return ["NONE"]

#         return self.schemas[key]["relations"]

import json


class RelationSchemaLoader:

    def __init__(self):

        with open(

            "schemas/relation_schemas.json",

            encoding="utf-8"

        ) as f:

            self.schemas = json.load(f)

    def get_relations(

        self,

        entity1_type,

        entity2_type

    ):

        key = (
            f"{entity1_type}_{entity2_type}"
        )

        if key not in self.schemas:

            return ["NONE"]

        return self.schemas[key][
            "relations"
        ]