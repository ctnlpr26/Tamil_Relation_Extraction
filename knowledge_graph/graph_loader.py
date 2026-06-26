from knowledge_graph.neo4j_client import (
    Neo4jClient
)

from knowledge_graph.graph_builder import (
    GraphBuilder
)


class GraphLoader:

    def __init__(self):

        self.client = Neo4jClient()
        self.builder = GraphBuilder()

    def insert(self, triple):

        data = self.builder.build(
            triple
        )

        self.client.insert_relation(
            data
        )