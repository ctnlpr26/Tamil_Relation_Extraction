# pipeline/entity_marker.py

from domain.entity import Entity


class EntityMarker:

    START_E1 = "[E1]"
    END_E1 = "[/E1]"

    START_E2 = "[E2]"
    END_E2 = "[/E2]"

    def mark(
        self,
        sentence: str,
        entity1: Entity,
        entity2: Entity
    ) -> str:

        marked_sentence = sentence

        entities = sorted(
            [entity1, entity2],
            key=lambda x: x.start,
            reverse=True
        )

        for entity in entities:

            if entity == entity1:

                marked_sentence = (
                    marked_sentence[:entity.start]
                    + f"{self.START_E1} "
                    + entity.text
                    + f" {self.END_E1}"
                    + marked_sentence[entity.end:]
                )

            else:

                marked_sentence = (
                    marked_sentence[:entity.start]
                    + f"{self.START_E2} "
                    + entity.text
                    + f" {self.END_E2}"
                    + marked_sentence[entity.end:]
                )

        return marked_sentence