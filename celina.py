import pandas
import math
teller = 0

def mijnmethode():
    pokemons = pandas.read_csv("Pokemon.csv")
    global teller
    teller += 1
    print(teller)
    print(pokemons)
    return "dit komt uit het bestand celina"

print (mijnmethode() + str(4+5))

def language_salary():
    salary_survey = pandas.read_csv("IT_Salary_Survey_EU_2020.csv")
    print(salary_survey)
    python_totaal_salaris = 0
    python_aantal = 0
    js_totaal_salaris = 0
    js_aantal = 0
    java_totaal_salaris = 0
    java_aantal = 0
    for i,regel in salary_survey.iterrows():
        if "Python" == regel["Your main technology / programming language"]:
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            #for regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            python_aantal += 1
            python_totaal_salaris+=regel["Yearly brutto salary (without bonus and stocks) in EUR"]
        elif "JavaScript" == regel["Your main technology / programming language"]:
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            js_aantal += 1
            js_totaal_salaris+=regel["Yearly brutto salary (without bonus and stocks) in EUR"]
        elif "Java" == regel["Your main technology / programming language"]:
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            java_aantal += 1
            java_totaal_salaris+=regel["Yearly brutto salary (without bonus and stocks) in EUR"]
    print(python_aantal)
    print(python_totaal_salaris)
    print(python_totaal_salaris/python_aantal)
    print(js_aantal)
    print(js_totaal_salaris)
    print(js_totaal_salaris/js_aantal)
    return "Average salary Python programmer in 2020: " + str(math.ceil(python_totaal_salaris/python_aantal)) + " EUR, average salary JavaScript programmer in 2020: " + str(math.ceil(js_totaal_salaris/js_aantal)) + " EUR, average salary Java programmer in 2020: " + str(math.ceil(java_totaal_salaris/java_aantal)) + " EUR"
