from db.pokedex import Pokedex
from helper.WriteAJson import writeAJson

pokedex = Pokedex()

pokemons1 = pokedex.getPokemonByName('Pikachu')
pokemons2 = pokedex.getPokemonsByNumber('022')
pokemons3 = pokedex.getPokemonsByEgg('2 km')
pokemons4 = pokedex.getPokemonsByWeaknesses(['Water'])
pokemons5 = pokedex.getPokemonsByCandyCount(100)

print(pokemons1)
print(pokemons2)
print(pokemons3)
print(pokemons4)
print(pokemons5)

writeAJson(pokemons1, 'Pikachu')
writeAJson(pokemons2, '022')
writeAJson(pokemons3, '2 km')
writeAJson(pokemons4, 'Water')
writeAJson(pokemons5, '100')