from copy import deepcopy

from normalization.normalization_pipeline import (
    NormalizationPipeline
)


class TripleNormalizer:

    def __init__(self):

        self.pipeline = (
            NormalizationPipeline()
        )

    def normalize(
        self,
        triple
    ):

        triple = deepcopy(triple)

        triple.subject = self.pipeline.process_text(
            triple.subject
        )

        triple.object = self.pipeline.process_text(
            triple.object
        )

        return triple