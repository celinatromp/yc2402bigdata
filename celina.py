import pandas

def mijnmethode():
    pokemons = pandas.read_csv("Pokemon.csv")
    print(pokemons)
    return "dit komt uit het bestand celina"

print (mijnmethode()) + str(4+5)