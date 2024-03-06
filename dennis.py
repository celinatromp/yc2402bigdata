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
    c1 = 'Yearly brutto salary (without bonus and stocks) in EUR'
    c2 = 'Company size'
    columns = [c1, c2]
    df = get_data(columns, jaar).rename(columns={c1: 'YearlyBrutoSalary', c2: 'CompanySize'})
    no_na = df[df['CompanySize'].notna()]
    mydata = no_na.groupby('CompanySize').mean()

    return mydata.round(2)


def small_company(jaar):
    df = pd.read_csv('IT_Salary_Survey_EU_' + str(jaar) + '.csv')
    total = 0
    for i, line in df.iterrows():
        if 'up to 10' == line['Company size']:
            print(line['Company size'])
            total += 1
    return print(total)


small_company(2020)


def data_to_json(data):
    result = data.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed, indent=4)


#print(set(get_data(['Yearly brutto salary (without bonus and stocks) in EUR', 'Company size'], 2020)))
#print(salary_vs_company_size(2020))
#print(data_to_json(salary_vs_company_size(2020)))
