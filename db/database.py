from typing import Collection
import pymongo
from dataset.pokemon_dataset import dataset


class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True  # CASO OCORRA O ERRO [SSL_INVALID_CERTIFICATE]
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
        except Exception as e:
            print(e)

    def resetDatabase(self):
        self.db.drop_collection(self.collection)
        self.collection.insert_many(dataset)


