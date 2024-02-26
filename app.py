from flask import Flask 
import felix

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