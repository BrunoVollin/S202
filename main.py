from db.database import Database
from helper.WriteAJson import writeAJson

db = Database(database="mercadinho", collection="ordens_produtos")
db.resetDatabase()

result1 = db.collection.aggregate([
    {"$group": {"_id": "$cliente", "total": {"$sum": "$total"}}},
    {"$sort": {"total": -1}}
])

writeAJson(result1, "ascasc")
