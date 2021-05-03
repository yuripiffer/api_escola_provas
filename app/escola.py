from database.db_escola import DbEscola
import random

db_escola = DbEscola()

class Escola:

    def gerar_id_aluno(self, nome) -> str:
        """
        se os 3 últimos números sortados já existirem, gera um outro.
        """
        while True:
            id_aluno = "2021"
            id_aluno += nome[0:2]
            id_aluno += str(random.randint(100, 999))
            if not db_escola.does_id_aluno_exist(id_aluno):
                return id_aluno

    def matricular_aluno(self, dict_matricula) -> str or tuple:
        nome = dict_matricula["nome"]
        data_nascimento = dict_matricula["data_nascimento"]

        nome = db_escola.valida_nome_aluno(nome)
        if not nome:
            return "OPS! Campo vazio ou já existe um(a) aluno(a) cadastrado com este nome."

        data_nascimento = db_escola.valida_data_nascimento(data_nascimento)
        if not data_nascimento:
            return "OPS! Campo vazio ou data de nascimento inválida."

        id_aluno = self.gerar_id_aluno(nome)
        dict_matricula = dict(id_aluno=id_aluno, nome=nome, data_nascimento=data_nascimento)
        if db_escola.persistir_aluno(dict_matricula):
            return f"""Aluno(a) cadastrado(a) com sucesso!
             nome = {nome}
             id_aluno = {id_aluno}""", 200
        else:
            return "OPS! Falha no armazenamento de dados.", 400


    def listar_alunos(self) -> dict or tuple:
        dict_dados = db_escola.retornar_alunos()
        if not dict_dados:
            return "Falha na coleta de dados com o banco de dados.", 400
        else:
            return dict_dados

    def cadastrar_prova(self, prova_cadastrada) -> tuple:
        """
        Checar como o dicionário é mandando lá
        no rotas_api
        """
        id_prova = prova_cadastrada["id_prova"]
        titulo_prova = prova_cadastrada["titulo_prova"]
        total_perguntas = prova_cadastrada["total_perguntas"]
        lista_alternativas = prova_cadastrada["lista_alternativas"]
        lista_pesos = prova_cadastrada["lista_pesos"]

        id_prova = db_escola.valida_id_prova(id_prova)
        if not id_prova:
            return "OPS! Este id_prova já existe no banco de dados.", 400

        if len(titulo_prova) <4:
            return "OPS! O título da prova tem menos que quatro caracteres.", 400
        if total_perguntas<1 or total_perguntas > 20:
            return "Total de perguntas informadas menor que 1 ou maior que 20.", 400
        if len(lista_alternativas) != len(lista_pesos) or len(
                lista_alternativas) != total_perguntas:
            return "O total de perguntas, pesos e alterenativas corretas não são iguais!", 400
        if not all([True if var.upper() in ["A","B","C","D","E"] else False for var in lista_alternativas]):
            return "Alguma das alternativas passadas não é 'A', 'B', 'C', 'D' ou 'E'.", 400
        lista_alternativas = [i.upper() for i in lista_alternativas]
        if (sum(lista_pesos) != 10) and (0 in lista_pesos):
            return f"A soma do peso da(s) {total_perguntas} pergunta(s) é diferente de 10.", 400

        dict_dados = dict(id_prova=id_prova,
                          titulo_prova=titulo_prova,
                          total_perguntas=total_perguntas,
                          lista_alternativas=lista_alternativas,
                          lista_pesos=lista_pesos)
        if db_escola.persistir_prova_cadastrada(dict_dados):
            return f"Prova {id_prova} cadastrada com sucesso!", 200
        else:
            return "Prova NÃO cadastrada!! Problemas com o armazenamento dos dados.", 400





