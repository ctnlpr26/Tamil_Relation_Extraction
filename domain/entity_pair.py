from dataclasses import dataclass

from domain.entity import Entity


@dataclass
class EntityPair:
    entity1: Entity
    entity2: Entity