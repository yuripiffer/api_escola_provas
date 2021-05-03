from flask import Flask, request
from app.escola import Escola
from app.aluno import Aluno
import json

"""
CORREÇÕES NECESSÁRIAS:
1. 
A data de nascimento está sendo armazenada como 
04\/10\/1991 ... consertar essa barra invertida

2.
No cadastro da prova, tá passando mais de 10 pontos
(p.ex pesos como [3,5,5,1] que dá 14 e não 10

3.
O mesmo aluno pode fazer a prova mais de uma vez.

4.
Corrigir os códigos (400, 500, 200...)
"""


def valida_chave_escola(chave_escola):
    #mudar
    if chave_escola == "abc":
        return True


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "ESCOLA FUNDAMENTAL GÊNESIS"

@app.route("/matricular/<chave_escola>/", methods=["POST"])
def post_matricula(chave_escola):
    """
    Espera um dicionário com nome e data_nascimento:
    {"nome": "Felipe moraes","data_nascimento": "01/06/2001"}
    :param chave_escola: valor informado ali em cima
    :return: str com mensagem de sucesso + id_aluno ou Erro
    """
    if not valida_chave_escola(chave_escola):
        return "Chave de escola inválida"

    raw_request = request.data.decode("utf-8")
    dict_matricula = json.loads(raw_request)

    response = Escola().matricular_aluno(dict_matricula)
    return response

@app.route("/listaralunos/<chave_escola>/", methods=["GET"])
def get_listar_alunos(chave_escola):
    """
    :param chave_escola:
    :return: str com listagem dos alunos ou Erro
    """
    if not valida_chave_escola(chave_escola):
        return "Chave de escola inválida"

    response = Escola().listar_alunos()
    return response

@app.route("/cadastrarprova/<chave_escola>/", methods=["POST"])
def post_cadastrar_prova(chave_escola):
    """
    Espera dicionário como o exemplo abaixo:
    {"id_prova" : "HIST034",
     "titulo_prova" : "Historia da Arte 2",
     "lista_alternativas" : ["A", "C", "B", "A"],
     "lista_pesos" : [1.5,3,3,2.5],
     "total_perguntas" : 4
    }
    :param chave_escola:
    :return: str mensagem de cadastro com sucesso ou erro.
    """
    if not valida_chave_escola(chave_escola):
        return "Chave de escola inválida"

    raw_request = request.data.decode("utf-8")
    prova_cadastrada = json.loads(raw_request)

    response = Escola().cadastrar_prova(prova_cadastrada)
    return response

@app.route("/listarprovas/<id_aluno>/", methods = ["GET"])
def get_listar_provas(id_aluno):
    """
    :param id_aluno: ex: "2021FA665"
    :return: dict com listagem de provas ou Erro.
    """
    response = Aluno().listar_provas(id_aluno)
    return response

@app.route("/listarquestoesprova/<id_aluno>/<id_prova>/", methods = ["GET"])
def get_listar_info_prova(id_aluno, id_prova):
    """
    :param id_aluno: ex: "2021FA665"
    :param id_prova: ex: "FISI001"
    :return: str nome, id e total de perguntas da prova ou Erro
    """
    response = Aluno().listar_informacoes_prova(id_aluno, id_prova)
    return response

@app.route("/realizarprova/", methods = ["POST"])
def post_realizar_prova():
    """
    Espera um dicionário do tipo:
    {
    "id_aluno":"2021FE782",
    "id_prova":"MATE012",
    "lista_respostas":["A","b","D","A"]
    }
    :param id_aluno: ex: "2021FA665"
    :return: nota ou mensagem de erro.
    """
    raw_request = request.data.decode("utf-8")
    dict_respostas = json.loads(raw_request)

    response = Aluno().realizar_prova(dict_respostas)
    return response





app.run(debug=True)

# retorno = get_listar_alunos(123)
# print(retorno)