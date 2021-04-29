from flask import Flask, request
from app.escola import Escola
from app.aluno import Aluno
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "ESCOLA FUNDAMENTAL GÊNESIS"

@app.route("/matricular/<chave_escola>/", methods=["POST"])
def post_matricula(chave_escola):
    """
    :param chave_escola:
    :return: str com mensagem de sucesso + id_aluno ou Erro
    """
    #CHECAR CHAVE DA ESCOLA

    raw_request = request.data.decode("utf-8")
    dict_matricula = json.loads(raw_request)

    response = Escola.matricular_aluno(dict_matricula)
    return response

@app.route("/listaralunos/<chave_escola>/", methods=["GET"])
def get_listar_alunos(chave_escola):
    """
    :param chave_escola:
    :return: str com listagem dos alunos ou Erro
    """
    # CHECAR CHAVE DA ESCOLA

    response = Escola.listar_alunos()
    return response

@app.route("/cadastrarprova/<chave_escola>/", methods=["POST"])
def post_cadastrar_prova(chave_escola):
    """
    Envia o dict prova_cadastrada para app.escola processar os dados
    :param chave_escola:
    :return: str mensagem de cadastro com sucesso ou erro.
    """
    # CHECAR CHAVE DA ESCOLA

    raw_request = request.data.decode("utf-8")
    prova_cadastrada = json.loads(raw_request)

    response = Escola.cadastrar_prova(prova_cadastrada)
    return response

@app.route("/listarprovas/<id_aluno>/", methods = ["GET"])
def get_listar_provas(id_aluno):
    """
    :param id_aluno:
    :return: str com listagem de provas ou Erro.
    """
    response = Aluno.listar_provas(id_aluno)
    return response

@app.route("/listarquestoesprova/<id_aluno>/<id_prova>/", methods = ["GET"])
def get_listar_info_prova(id_aluno, id_prova):
    """
    :param id_aluno:
    :param id_prova:
    :return: str nome, id e total de perguntas da prova ou Erro
    """
    response = Aluno.listar_informacoes_prova(id_aluno, id_prova)
    return response

@app.route("/realizarprova/", methods = ["POST"])
def post_realizar_prova(id_aluno):
    """
    :param id_aluno:
    :return: nota ou mensagem de erro.
    """
    raw_request = request.data.decode("utf-8")
    dict_respostas = json.loads(raw_request)

    response = Aluno.realizar_prova(dict_respostas)
    return response




