from database.db_escola import DbEscola
import random

class Escola():

    def gerar_id_aluno(self, nome):
        while True:
            id_aluno = ""
            #id_aluno = gerar o ano (tipo, 2020, 2021...)
            id_aluno += nome[0:2]
            id_aluno += random.randint(100,999)
            if not DbEscola.existe_id_aluno(id_aluno):
                return id_aluno

    def matricular_aluno(self, dict_matricula):
        nome = dict_matricula["nome"]
        data_nascimento = dict_matricula["data_nascimento"]

        nome = DbEscola.valida_nome_aluno(nome)
        if not nome:
            return "OPS! Campo vazio ou já existe um(a) aluno(a) cadastrado com este nome."
        if not data_nascimento:
            return "OPS! Campo vazio ou data de nascimento inválida."

        id_aluno = self.gerar_id_aluno(nome)
        dict_matricula = dict(id_aluno=id_aluno, nome=nome, data_nascimento=data_nascimento)
        if DbEscola.persistir_aluno(dict_matricula):
            return f"Aluno(a) cadastrado(a) com sucesso!\n nome = {nome}\n id_aluno = {id_aluno}"
        else:
            return "OPS! Falha no armazenamento de dados."



    def listar_alunos(self):
        alunos = DbEscola.retornar_alunos()
        if not alunos:
            return "Falha na coleta de dados com o banco de dados."
        #else:
            # retonar esses alunos em algum formato
            # id_aluno | nome
            # id_aluno | nome
            # id_aluno | nome
        pass


    def cadastrar_prova(self, prova_cadastrada):
        """
        RECEBIMENTO DO CORPO
        Recebe o dicionário prova_cadastrada
        {
        "id_prova" = "HIST034",
        "titulo_prova" = "Historia da Arte 2",
        "lista_alternativas" = ["A", "C", "B", "A"]
        "lista_pesos" = [1.5,3,3,2.5],
        "total_perguntas" = 4
        }
        """
        id_prova = prova_cadastrada["id_prova"]
        titulo_prova = prova_cadastrada["titulo_prova"]
        total_perguntas = prova_cadastrada["total_perguntas"]
        lista_alternativas = prova_cadastrada["lista_alternativas"]
        lista_pesos = prova_cadastrada["lista_pesos"]

        id_prova = DbEscola.valida_id_prova(id_prova)
        if not id_prova:
            return "OPS! Este id_prova já existe no banco de dados."

        if len(titulo_prova) <4:
            return "OPS! O título da prova tem menos que quatro caracteres."
        if total_perguntas<1 or total_perguntas > 20:
            return "Total de perguntas informadas menor que 1 ou maior que 20."
        if len(lista_alternativas) != len(lista_pesos) or len(
                lista_alternativas) != total_perguntas:
            return "O total de perguntas, pesos e alterenativas corretas não são iguais!"
        if not all([True if var.upper() in ["A","B","C","D","E"] else False for var in lista_alternativas]):
            return "Alguma das alternativas passadas não é 'A', 'B', 'C', 'D' ou 'E'."
        lista_alternativas = [i.upper() for i in lista_alternativas]
        if (sum(lista_pesos) != 10) and (0 in lista_pesos):
            return f"A soma do peso da(s) {total_perguntas} pergunta(s) é diferente de 10."

        lista_dados = [id_prova, titulo_prova, total_perguntas, lista_alternativas, lista_pesos ]
        if DbEscola.persistir_prova_cadastrada(lista_dados):
            return f"Prova {id_prova} cadastrada com sucesso!"
        else:
            return "Prova NÃO cadastrada!! Problemas com o armazenamento dos dados."





