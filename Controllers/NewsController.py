import json
import sys
sys.path.append("..")
from NoticiasFlaskinhas import app
import Infra.NoticiaDao as dao
from flask import request, make_response, Response, jsonify, abort
import datetime
from Models.Noticia import Noticia

@app.route("/noticias")
def getAll():
    conteudo = dao.getAll()
    return Response(json.dumps(conteudo, default=str), mimetype="application/json")

@app.route('/noticias/<string:id>')
def getById(id):
    conteudo = dao.getById(id)
    return Response(json.dumps(conteudo, default=str), mimetype="application/json")

@app.route('/noticias/<string:id>', methods=['DELETE',])
def deleteById(id):
    noticia = dao.getById(id)
    resultado = dao.delete(id)
    if resultado.deleted_count == 1:
        return Response(json.dumps(noticia, default=str), mimetype="application/json")
    else:
        resposta = jsonify({'erro': 'Notícia não encontrada.'})
        resposta.status_code = 404  # HTTP 400 (Bad Request)
        return resposta

@app.route('/noticias/<string:id>', methods=['PUT',])
def updateById(id):
    if 'titulo' not in request.form or 'conteudo' not in request.form:
        resposta = jsonify({'erro': 'Título e conteúdo são campos obrigatórios.'})
        resposta.status_code = 400  # HTTP 400 (Bad Request)
        return resposta
    titulo = request.form['titulo']
    conteudo = request.form['conteudo']
    result = dao.update(id,titulo,conteudo)
    if result.modified_count == 1:
        return Response(json.dumps(dao.getById(id), default=str), mimetype="application/json")
    else:
        resposta = jsonify({'erro': 'Notícia não encontrada.'})
        resposta.status_code = 404  # HTTP 400 (Bad Request)
        return resposta

@app.route('/noticias/criar', methods=['POST',])
def save():
    if 'titulo' not in request.form or 'conteudo' not in request.form:
        resposta = jsonify({'erro': 'Título e conteúdo são campos obrigatórios.'})
        resposta.status_code = 400  # HTTP 400 (Bad Request)
        return resposta

    titulo = request.form['titulo']
    conteudo = request.form['conteudo']
    data_publicacao = datetime.datetime.today()
    noticia = Noticia(titulo,conteudo,data_publicacao)

    id = dao.save(noticia)
    resposta = make_response('', 201)
    resposta.headers['Location'] = "/noticias/"+id
    return resposta