# # pipeline/ner_stage.py

# from models.ner.ner_model import TamilNERModel
# from domain.entity import Entity


# class NERStage:

#     def __init__(self):

#         self.model = TamilNERModel()

#     def extract(self, sentence: str):

#         predictions = self.model.predict(sentence)

#         entities = []

#         # for pred in predictions:

#         #     entities.append(
#         #         Entity(
#         #             text=pred["word"],
#         #             label=pred["entity_group"],
#         #             start=pred["start"],
#         #             end=pred["end"]
#         #         )
#         #     )

#         # return entities

#         # pipeline/ner_stage.py

#         for pred in predictions:

#             entity_text = sentence[
#                 pred["start"]:pred["end"]
#             ]

#             entities.append(
#                 Entity(
#                     text=entity_text,
#                     label=pred["entity_group"],
#                     start=pred["start"],
#                     end=pred["end"]
#                 )
#             )
#         return entities

# pipeline/ner_stage.py

# from models.ner.ner_model import TamilNERModel
# from domain.entity import Entity

# from utils.entity_postprocessor import (
#     normalize_entity_text,
#     normalize_entity_label
# )


# class NERStage:

#     def __init__(self):

#         self.model = TamilNERModel()

#     def extract(self, sentence: str):

#         predictions = self.model.predict(sentence)

#         entities = []

#         for pred in predictions:

#             entity_text = sentence[
#                 pred["start"]:pred["end"]
#             ]

#             entity_text = normalize_entity_text(
#                 entity_text
#             )

#             entity_label = normalize_entity_label(
#                 pred["entity_group"]
#             )

#             entities.append(
#                 Entity(
#                     text=entity_text,
#                     label=entity_label,
#                     start=pred["start"],
#                     end=pred["end"]
#                 )
#             )

#         return entities

# pipeline/ner_stage.py

from models.ner.ner_model import TamilNERModel
from domain.entity import Entity

from utils.entity_postprocessor import (
    normalize_entity_text,
    normalize_entity_label
)

from utils.entity_merger import (
    merge_adjacent_entities
)


class NERStage:

    def __init__(self):

        self.model = TamilNERModel()

    def extract(self, sentence: str):

        predictions = self.model.predict(sentence)

        entities = []

        for pred in predictions:

            start = pred["start"]
            end = pred["end"]

            entity_text = sentence[start:end]

            # Tamil pulli recovery
            if end < len(sentence):

                next_char = sentence[end]

                if next_char == "்":
                    entity_text += next_char
                    end += 1

            entity_text = normalize_entity_text(
                entity_text
            )

            entity_label = normalize_entity_label(
                pred["entity_group"]
            )

            entities.append(
                Entity(
                    text=entity_text,
                    label=entity_label,
                    start=start,
                    end=end
                )
            )

        entities = merge_adjacent_entities(
            entities
        )

        return entities