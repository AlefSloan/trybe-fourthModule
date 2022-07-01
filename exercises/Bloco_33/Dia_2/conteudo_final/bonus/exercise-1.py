import json
import random

number_of_tries = 1
pokemons_list = []

with open('source-for-exercise/bonus-exercise-1/pokemons.json') as file:
    pokemons = json.load(file)['results']

for pokemon in pokemons:
    pokemons_list.append(pokemon['name'])

choosen_pokemon = random.choice(pokemons_list)

guess_pokemon = input('Qual é esse pokemon? ')

while guess_pokemon != choosen_pokemon:
    print(choosen_pokemon[:number_of_tries])
    guess_pokemon = input('Tente novamente, qual é esse pokemon? ')
    number_of_tries += 1


print(f"Parabéns, você acertou o pokemon correto { choosen_pokemon }")
