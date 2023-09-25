from pymongo import MongoClient
cliente_mongo = MongoClient('localhost', 27017)
banco_de_dados = cliente_mongo.noticiasflaskinhas
