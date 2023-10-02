import os
from pymongo import MongoClient
cliente_mongo = MongoClient(os.environ["host_mongo"], int(os.environ["port_mongo"]))
banco_de_dados = cliente_mongo.noticiasflaskinhas
