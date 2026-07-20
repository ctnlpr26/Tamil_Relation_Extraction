from neo4j import GraphDatabase


class Neo4jClient:

    def __init__(self):

        self.driver = GraphDatabase.driver(
            "neo4j+s://4ed7b5c3.databases.neo4j.io",
            auth=("4ed7b5c3", "i2L_TO0lmfO1SMpDv7aW6SKHIiSxQgjFBMm3QgNvGOg")
        )

    def close(self):

        self.driver.close()

    def insert_relation(
        self,
        data
    ):

        with self.driver.session() as session:

            session.execute_write(
                self._create_relation,
                data
            )

    @staticmethod
    def _create_relation(
        tx,
        data
    ):

        query = f"""
        MERGE (s:{data['subject_label']}
        {{name:$subject}})

        MERGE (o:{data['object_label']}
        {{name:$object}})

        MERGE (s)-[:{data['relation']}]->(o)
        """

        tx.run(
            query,
            subject=data["subject"],
            object=data["object"]
        )