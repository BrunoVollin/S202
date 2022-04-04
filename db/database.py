from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
import logging


class Graph:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        data = []
        with self.driver.session() as session:
            results = session.run(query, parameters)
            for record in results:
                data.append(record)
            return data

    @staticmethod
    def _execute(tx, query):
        try:
            data = []
            result = tx.run(query)
            for record in result:
                data.append(record)

        except ServiceUnavailable as exception:
            logging.error(f"{query} gerou um erro: \n {exception}")
            raise

        return data

    def read(self, query):
        with self.driver.session() as session:
            result = session.read_transaction(self._execute, query)
            return result

    def write(self, query):
        with self.driver.session() as session:
            result = session.write_transaction(self._execute, query)
            return result


