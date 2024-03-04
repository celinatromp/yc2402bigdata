import pandas as pd
import requests
from json import loads, dumps


def mijnmethode():
    df = pd.read_csv("Pokemon.csv")
    print(df.tail(1))

    # API call from catfact
    paginaresult = requests.get("https://catfact.ninja/fact")
    facts = paginaresult.json()
    return '<h1>Random cat fact: </h1>' + facts['fact']


def get_data(columns, jaar):
    df = pd.read_csv('IT_Salary_Survey_EU_' + str(jaar) + '.csv')
    mydata = df[columns]

    return mydata


def salary_vs_company_size(jaar):
    abc = 'Yearly brutto salary (without bonus and stocks) in EUR'
    columns = [abc, 'Company size']
    df = get_data(columns, jaar)
    no_na = df[df['Company size'].notna()]
    mydata = no_na.groupby('Company size').mean()

    return mydata.round(2)


def salary_vs_company_size2(jaar):
    index = pd.MultiIndex.from_arrays(get_data(jaar), names=('Position ', 'Yearly brutto salary (without bonus and stocks) in EUR', 'Company size'))
    abc = 'Yearly brutto salary (without bonus and stocks) in EUR'
    columns = ['Yearly brutto salary (without bonus and stocks) in EUR', 'Company size']
    df = pd.DataFrame({'Company size'}, index=index)
    no_na = df[df['Company size'].notna()]
    mydata = no_na.groupby('Company size').mean()

    return mydata.round(2)


def data_to_json(data):
    result = data.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed, indent=4)


#print(set(get_data(['Yearly brutto salary (without bonus and stocks) in EUR', 'Company size'], 2020)))
#print(salary_vs_company_size(2020))
print(data_to_json(salary_vs_company_size(2020)))
