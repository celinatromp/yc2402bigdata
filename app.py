from flask import Flask 
import felix
import asef
import celina
import dennis

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/tweedetest")
def tweedetest():
    return "<p>Dit is mijn tweede test</p>"

@app.route("/derdetest/<pokemonnaam>")
def derdetest(pokemonnaam):
    return felix.mijnmethode(pokemonnaam)

@app.route("/testcelina")
def testcelina():
    return celina.mijnmethode()

@app.route("/testasef")
def testasef():
    return asef.mijnmethode()

@app.route("/testdennis")
def testdennis():
    return dennis.mijnmethode()

@app.route("/testdennis/<jaar>")
def salary_vs_company_size(jaar):
    return dennis.data_to_json(dennis.salary_vs_company_size(jaar))

@app.route("/taalprijs")
def salary_vs_language():
    return celina.language_salary()