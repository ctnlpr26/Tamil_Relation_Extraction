# from pipeline.extraction_pipeline import (
#     ExtractionPipeline
# )

# from knowledge_graph.graph_loader import (
#     GraphLoader
# )


# class KGExtractionPipeline(
#     ExtractionPipeline
# ):

#     def __init__(self):

#         super().__init__()

#         self.graph_loader = GraphLoader()

#     def run(self, document):

#         triples = super().run(
#             document
#         )

#         for triple in triples:

#             self.graph_loader.insert(
#                 triple
#             )

#         return triples

from pipeline.extraction_pipeline import (
    ExtractionPipeline
)

from knowledge_graph.graph_loader import (
    GraphLoader
)

from normalization.triple_normalizer import (
    TripleNormalizer
)


class KGExtractionPipeline(
    ExtractionPipeline
):

    def __init__(self):

        super().__init__()

        self.graph_loader = GraphLoader()

        self.normalizer = TripleNormalizer()

    def run(
        self,
        document
    ):

        triples = super().run(
            document
        )

        normalized_triples = []

        print("\n")
        print("=" * 80)
        print("TRIPLE NORMALIZATION")
        print("=" * 80)

        for triple in triples:

            normalized_triple = (
                self.normalizer.normalize(
                    triple
                )
            )

            print("\nRAW        :", triple)
            print("NORMALIZED :", normalized_triple)

            normalized_triples.append(
                normalized_triple
            )

        print("\n")
        print("=" * 80)
        print("INSERTING INTO NEO4J")
        print("=" * 80)

        for triple in normalized_triples:

            self.graph_loader.insert(
                triple
            )

        return normalized_triples