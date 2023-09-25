from config import banco_de_dados
from bson.objectid import ObjectId
from Models.Noticia import Noticia

colecao = banco_de_dados.noticias

def getById(id):
    object_id = ObjectId(id)
    documento = colecao.find_one({"_id": object_id})
    if documento:
        #minha_instancia = Noticia(documento["titulo"], documento["conteudo"],documento["data_publicacao"])
        return documento
    else:
        return None

def getAll():
    documentos_ordenados = colecao.find().sort("data_publicacao", 1)
    lista_documentos = list(documentos_ordenados)
    return lista_documentos

def save(Noticia):
    instancia_dict = vars(Noticia)
    resultado = colecao.insert_one(instancia_dict)
    return str(resultado.inserted_id)

def delete(id):
    object_id = ObjectId(id)
    resultado = colecao.delete_one({'_id': object_id})
    return resultado

def update(id,titulo,conteudo):
    object_id = ObjectId(id)
    novos_valores = {"titulo":titulo, "conteudo":conteudo}
    resultado = colecao.update_one({"_id": object_id}, {"$set": novos_valores})
    return resultado