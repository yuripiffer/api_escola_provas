from flask import Flask, request, render_template   #request sem s
from app.escola import Escola
from app.aluno import Aluno

import MySQLdb
import json
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "ESCOLA FUNDAMENTAL GÊNESIS"

@app.route("/matricular/<chave_escola>/", methods=["GET"])
def rota_matricula(chave_escola):
    """
    :param chave_escola:
    :return: str com mensagem de sucesso + id_aluno ou Erro
    """
    mensagem = Escola.matricular_aluno(chave_escola)
    return mensagem

@app.route("/listaralunos/<chave_escola>/", methods=["GET"])
def rota_listar_alunos(chave_escola):
    """
    :param chave_escola:
    :return: str com listagem dos alunos ou Erro
    """
    mensagem = Escola.listar_alunos(chave_escola)
    return mensagem

@app.route("/cadastrarprova/<chave_escola>/", methods=["POST"])
def rota_cadastrar_prova(chave_escola):
    """
    Envia o dict prova_cadastrada para app.escola processar os dados
    :param chave_escola:
    :return: str mensagem de cadastro com sucesso ou erro.
    """
    raw_request = request.data.decode("utf-8")
    prova_cadastrada = json.loads(raw_request)

    mensagem = Escola.cadastrar_prova(prova_cadastrada)
    return mensagem

@app.route("/listarprovas/<id_aluno>/", methods = ["GET"])
def rota_listar_provas(id_aluno):
    """
    :param id_aluno:
    :return: str com listagem de provas ou Erro.
    """
    mensagem = Aluno.listar_provas(id_aluno)
    return mensagem

@app.route("/listarquestoesprova/<id_aluno>/<id_prova>/", methods = ["GET"])
def rota_listar_questoes_prova(id_aluno, id_prova):
    """
    :param id_aluno:
    :param id_prova:
    :return: str questoes e alternativas ou Erro
    """
    mensagem = Aluno.listar_questoes_prova(id_aluno, id_prova)
    return mensagem

@app.route("/realizarprova/<id_aluno>/<id_prova>/", methods = ["POST"])
def rota_realizar_prova(id_aluno, id_prova):
    """
    :param id_aluno:
    :param id_prova:
    :return: nota ou mensagem de erro.
    """
    raw_request = request.data.decode("utf-8")
    prova_respostas = json.loads(raw_request)

    nota = Aluno.realizar_prova(id_aluno, id_prova, prova_respostas)
    return nota




