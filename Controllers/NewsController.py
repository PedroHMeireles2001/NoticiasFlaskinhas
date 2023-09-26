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
        return makeErrorResponse(404,"Notícia não encontrada")

@app.route('/noticias/<string:id>', methods=['PUT',])
def updateById(id):
    if not validateRequest(request):
        return makeErrorResponse(400, "Título e conteúdo são campos obrigatórios")

    titulo, conteudo = extractRequest(request)
    result = dao.update(id,titulo,conteudo)

    if result.modified_count == 1:
        return Response(json.dumps(dao.getById(id), default=str), mimetype="application/json")
    else:
        return makeErrorResponse(404,"Notícia não encontrada")

@app.route('/noticias/criar', methods=['POST',])
def save():
    if not validateRequest(request):
        return makeErrorResponse(400, "Título e conteúdo são campos obrigatórios")

    titulo, conteudo = extractRequest(request)
    data_publicacao = datetime.datetime.today()
    noticia = Noticia(titulo,conteudo,data_publicacao)

    id = dao.save(noticia)
    resposta = make_response('', 201)
    resposta.headers['Location'] = "noticias/"+id
    return resposta

def validateRequest(req):
    if 'titulo' not in req.form or 'conteudo' not in req.form:
        return False
    return True

def makeErrorResponse(code=400,msg=""):
    resposta = jsonify({'erro': msg})
    resposta.status_code = code
    return resposta

def extractRequest(req):
    if not validateRequest(req):
        return ("","")
    titulo = request.form['titulo']
    conteudo = request.form['conteudo']
    return (titulo, conteudo)