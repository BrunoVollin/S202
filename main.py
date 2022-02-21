from db.database import Database
from helper.WriteAJson import writeAJson

db = Database()

tipos = ["Grass", "Poison"]
pokemons = db.executeQuery({ "type": {"$in": tipos}, "next_evolution": {"$exists": True} })

writeAJson(data=pokemons, name="Pokemons")
