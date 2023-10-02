import os
from pymongo import MongoClient
cliente_mongo = MongoClient(os.environ["host_mongo"], s.environ["port_mongo"])
banco_de_dados = cliente_mongo.noticiasflaskinhas
