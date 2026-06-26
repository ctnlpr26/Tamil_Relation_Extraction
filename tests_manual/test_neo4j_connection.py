from knowledge_graph.neo4j_client import (
    Neo4jClient
)

client = Neo4jClient()

print(
    "Neo4j connection successful."
)

client.close()