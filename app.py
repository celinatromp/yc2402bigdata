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

@app.route("/derdetest")
def derdetest():
    return felix.mijnmethode()

@app.route("/testcelina")
def testcelina():
    return celina.mijnmethode()

@app.route("/testasef")
def testasef():
    return asef.mijnmethode()

@app.route("/testdennis")
def testdennis():
    return dennis.mijnmethode()