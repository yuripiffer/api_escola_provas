

class Aluno():

    def listar_provas(id_aluno):
        """
        API GET - passar o /id_aluno/ na rota para acessar a info

        VALIDAÇÃO
        checar se id_aluno existe, caso contrário retorna uma mensagem de
        que não é possível acessar tais informaões

        BUSCA NO BANCO DE DADOS
        puxa da pasta database (de alunos ou escola???) para aqui o dicionário de provas existentes
        - id_prova
        - titulo_prova
        Caso o dict nao seja vazio
        cria uma string com as provas cadastradas

        :param id_aluno: int
        :return:string com provas cadastradas
        """
        pass

    def listar_questoes_prova(id_aluno, id_prova):
        """
        API GET - passar o /id_aluno/id_prova/ rota para acessar a info

        VALIDAÇÃO
        checar se id_aluno existe, caso contrário retorna uma mensagem de erro
        checar se id_prova existe, caso contrário retorna uma mensagem de erro

        BUSCA NO BANCO DE DADOS
        puxa pela pasta database (database.aluno ou database.escola) o dicionário da prova com dicionário das questões

        manipula esse dicionário para retonar um texto do tipo
        texto_alternativas =
        '''id_prova: FISI02
        Questão 1 - Alternativas: A, B, C
        Questão 2 - Alternativas: 2 - 1, 2, 3, 4, 5 ...'''

        :param id_aluno:
        :param id_prova:
        :return: texto_alternativas
        """
        pass

    def realizar_prova(id_aluno, id_prova, prova_respostas):
        """
        API POST - passar o /id_aluno/id_prova/ rota para acessar a info

        VALIDAÇÃO
        checar se id_aluno existe, caso contrário retorna uma mensagem de erro
        checar se id_prova existe, caso contrário retorna uma mensagem de erro

        RECEBIMENTO DO CORPO
        Recebe um prova_respostas do tipo:
        prova_respostas = {
        "id_prova":"FISI02",
        "1":"C",
        "2":"B"
        }

        Checa se em provas_respostas existem keys de todas as questões e se há values nelas (mesmo que vazio)
        CASO NÃO:
            Se não foram, precisa retonar uma mensagem de erro e não persistir.
        CASO SIM:
            FUNÇÃO QUE DEVERÁ ESTAR NO database.aluno:
            passa esse dicionário prova_respostas que recebeu para a função que estará no database.aluno
            Armazena no db de provas_realizadas
            | id_prova | id_aluno | dict_passado | nota

        Cálculo de nota:
            CHAMA do database.aluno a função que traz o dict prova_cadastrada com as respostas corretas , ex:

        prova_cadastrada = {
        "id_prova":"FISI02",
        "titulo_prova":"Física Newtoniana 02 - Prova parcial",
            "1":{
        "Alternativas":["A", "B", "C", "D","E"],
        "Resposta correta": "A",
        "Peso": "3.5"},
            "2":{
        "Alternativas":["A", "B", "C", "D","E"],
        "Resposta correta": "C",
        "Peso": "5"},
            "3":{
        "Alternativas":["A", "B", "C"],
        "Resposta correta": "B",
        "Peso": "1.5"}
        }

        nota_aluno = 0.0
        compara para as mesmas keys de prova_respostas e prova_cadastrada
        IF prova_respostas[key] == prova_cadastrada[key]["Resposta correta"]:
            nota_aluno += prova_cadastrada[key]["Peso"]

        Persiste a nota no db de provas_realizadas
        retonra para o aluno a nota.
        """
        pass