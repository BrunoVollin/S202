from db.database import Database


class Pokedex:
    def __init__(self):
        self.db = Database(database="pokedex", collection="pokemons")
        self.db.resetDatabase()
        self.collection = self.db.collection

    def find(self, filters: dict):
        response = self.collection.find(filters)
        pokemons = []
        for pokemon in response:
            pokemons.append(pokemon)
        return pokemons

    def getAllPokemons(self):
        response = self.collection.find({}, {"name": 1, "_id": 0})
        pokemons = []
        for pokemon in response:
            pokemons.append(pokemon)
        return pokemons

    def getPokemonByName(self, name: str):
        response = self.collection.find({"name": name},
                                        {"_id": 0, "name": 1,
                                         "next_evolution": 1, "prev_evolution": 1,
                                         "type": 1, "weaknesses": 1})
        result = {}
        for pokemon in response:
            result = pokemon
        return result

    def getPokemonsByType(self, type: list):
        response = self.collection.find({"type": {"$all": type}}, {
            "_id": 0, "name": 1, "type": 1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result

    def getPokemonEvolutionsByName(self, name: str):
        pokemon = self.getPokemonByName(name)

        evolutions = [pokemon['name']]
        hasNextEvolutions = ('next_evolution' in pokemon)
        hasPrevEvolutions = ('prev_evolution' in pokemon)

        if hasNextEvolutions:
            nextEvolutions = list(pokemon['next_evolution'])
            for evolution in nextEvolutions:
                evolution = self.getPokemonByName(evolution['name'])
                evolutions.append(evolution['name'])

        if hasPrevEvolutions:
            previousEvolutions = list(pokemon['prev_evolution'])
            for evolution in previousEvolutions:
                evolution = self.getPokemonByName(evolution['name'])
                evolutions.append(evolution['name'])

        return evolutions

    def getPokemonsByNumber(self, num: str):
        response = self.collection.find({"num": num},
                                        {"_id": 0, "num": 1, "name": 1,
                                         "next_evolution": 1, "prev_evolution": 1,
                                         "type": 1, "weaknesses": 1})
        result = {}
        for pokemon in response:
            result = pokemon
        return result

    def getPokemonsByEgg(self, egg: str):
        response = self.collection.find({"egg": egg}, {
            "_id": 0, "name": 1, "egg": 1,
            "type": 1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result

    def getPokemonsByWeaknesses(self, weaknesses: list):
        response = self.collection.find({"weaknesses": {"$all": weaknesses}}, {
            "_id": 0, "name": 1, "weaknesses": 1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result

    def getPokemonsByHeight(self, height: list):
        response = self.collection.find({"height": {"$all": height}}, {
            "_id": 0, "name": 1, "height": 1, "next_evolution": 1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result

    def getPokemonsByCandyCount(self, candy_count: int):
        response = self.collection.find({"candy_count": candy_count},
                                        {"_id": 0, "num": 1, "name": 1,
                                         "next_evolution": 1, "prev_evolution": 1,
                                         "type": 1, "candy_count": 1, "weaknesses": 1})
        result = {}
        for pokemon in response:
            result = pokemon
        return result