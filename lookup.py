from db.database import Database
from helper.WriteAJson import writeAJson
from dataset.pessoa_dataset import dataset as pessoa_dataset
from dataset.carro_dataset import dataset as carro_dataset

pessoas = Database(
    database="consesionaria",
    collection="pessoas",
    dataset=pessoa_dataset
)
pessoas.resetDatabase()

carros = Database(
    database="consesionaria",
    collection="carros",
    dataset=carro_dataset
)
carros.resetDatabase()

result1 = carros.collection.aggregate([
    {"$lookup":
        {
            "from": "pessoas",  # outra colecao
            "localField": "dono_id",  # chave estrangeira
            "foreignField": "_id",  # id da outra colecao
            "as": "dono"  # nome da saida
        }
     }
])

writeAJson(result1, "result1")

result4 = db.collection.aggregate([
    {"$project": {
        "_id": 0,
        "cliente": 1,
        "desconto": {
            "$cond": {"if": {"$gte": ["$total", 10]}, "then": 0.1, "else": 0.05}
        }
    }}
])
