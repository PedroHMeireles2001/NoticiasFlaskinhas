import flask
from flask import Flask
from flask_cors import CORS

app = Flask("Noticias Flaskinhas")
from Controllers.NewsController import *

def run_app():
    CORS(app)
    app.run(debug=True)

if __name__ == '__main__':
    run_app()