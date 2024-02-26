import pandas


def mijnmethode():
    pokemons = pandas.read_csv("Pokemon.csv")
    print(pokemons)
    return "Dit heeft Dennis geschreven!"
