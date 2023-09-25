import flask
from flask import Flask

app = Flask("Noticias Flaskinhas")
from Controllers.NewsController import *

def run_app():
    app.run(debug=True)

if __name__ == '__main__':
    run_app()