from S202.dataset import produto_database
from db.database import Database
from helper.WriteAJson import writeAJson
from dataset.pessoa_dataset import dataset as pessoa_dataset

pessoas = Database(
    database="database",
    collection="pessoas",
    dataset=pessoa_dataset
)
pessoas.resetDatabase()

produtos = Database(
    database="database",
    collection="produtos",
    dataset=produto_database
)
produtos.resetDatabase()

compras1 = pessoas.collection.aggregate([
    {"$lookup":
        {
            "from": "produtos",  # outra colecao
            "localField": "dono_id",  # chave estrangeira
            "foreignField": "_id",  # id da outra colecao
            "as": "dono"  # nome da saida
        }
     }
])

writeAJson(compras1, "result1")

