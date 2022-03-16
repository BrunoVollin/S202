from db.database import Database
from helper.WriteAJson import writeAJson
from dataset.produto_database import dataset

db = Database(database="database", collection="produtos", dataset=dataset)
db.resetDatabase()

result1 = db.collection.aggregate([
    {"$lookup":
        {
            "from": "pessoas",
            "localField": "cliente_id",
            "foreignField": "_id",
            "as": "comprador"
        }
     },
    {"$group": {"_id": "$comprador", "total": {"$sum": "$total"}}},
    {"$sort": {"total": 1}},
    {"$unwind": '$_id'},
    {"$project": {
        "_id": 0,
        "nome": "$_id.nome",
        "total": "$total",
        "desconto" : {
            "$cond": {"if": {"$gte": ["$total", 10]}, "then": True, "else": False}
        }
    }}
])

writeAJson(result1, "result1")
