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
    c1 = 'Yearly brutto salary (without bonus and stocks) in EUR'
    c2 = 'Company size'
    columns = [c1, c2]
    df = get_data(columns, jaar).rename(columns={c1: 'YearlyBrutoSalary', c2: 'CompanySize'})
    no_na = df[df['CompanySize'].notna()]
    mydata = no_na.groupby('CompanySize').mean()

    return mydata.round(2)


def small_company(beroep="devops", jaar="2020"):
    df = pd.read_csv('IT_Salary_Survey_EU_' + str(jaar) + '.csv')
    total = 0
    YearlyBrutoSalaryColumn = 'Yearly brutto salary (without bonus and stocks) in EUR'
    extra_small_company = 'up to 10'

    small_company = '11-50'
    small_company_salary = []

    medium_company = '51-100'
    medium_company_salary = []

    large_company = '101-1000'
    large_company_salary = []

    extra_large_company = '1000+'
    extra_large_company_salary = []

    for i, line in df.iterrows():
        if str(line['Position ']).lower() == beroep:
            if line['Company size'] == extra_small_company or line['Company size'] == small_company:
                small_company_salary.append(line[YearlyBrutoSalaryColumn])
            
            if line['Company size'] == medium_company:
                medium_company_salary.append(line[YearlyBrutoSalaryColumn])
                
    return print(small_company_salary)


small_company()


def data_to_json(data):
    result = data.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed, indent=4)


#print(set(get_data(['Yearly brutto salary (without bonus and stocks) in EUR', 'Company size'], 2020)))
#print(salary_vs_company_size(2020))
#print(data_to_json(salary_vs_company_size(2020)))
