from pipeline.extraction_pipeline import (
    ExtractionPipeline
)

from knowledge_graph.graph_loader import (
    GraphLoader
)


class KGExtractionPipeline(
    ExtractionPipeline
):

    def __init__(self):

        super().__init__()

        self.graph_loader = GraphLoader()

    def run(self, document):

        triples = super().run(
            document
        )

        for triple in triples:

            self.graph_loader.insert(
                triple
            )

        return triples