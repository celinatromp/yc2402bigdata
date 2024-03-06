import pandas
teller = 0

def mijnmethode():
    pokemons = pandas.read_csv("Pokemon.csv")
    teller += 1
    print(teller)
    print(pokemons)
    return "dit komt uit het bestand celina"

print (mijnmethode() + str(4+5))