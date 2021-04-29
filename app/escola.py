
class Escola():

    def matricular_aluno(chave_escola):
        """
        API POST
        Checa se a chave_escola é válida

        Recebe no corpo do texto:
        - nome
        - data de nascimento

        manipula o nome em upper e checa se não etá vazio
        manipula a data de nascimento

        - chama a funcao_gerar_matricula e atribui uma matrícula
        - chama de database.escola a função que checa se o id_aluno existe ou ainda não existe.

        SE EXISTE:
        - modifica a matrícula até ser aceita...

        SE NÃO EXISTE:
        envia para database.escola persistir esse dado. É esperado o id_aluno como chave do dict:
        {
        "2021YUR001":{
            "nome" = "JOÃOZINHO DA SILVA"
            "data_nascimento" = "1991/10/04"}
        }


        :return: Mensagem de Sucesso + informação do id_aluno
        """
        pass


    def listar_alunos(chave_escola):
        """
        API GET
        Checa se a chave_escola é válida

        Puxar de database.aluno
        O dado chega assim:
        {
        "2021YUR001":{
            "nome" = "JOÃOZINHO DA SILVA"
            "data_nascimento" = "1991/10/04"},
        "2021ANA002":{
            "nome" = "ANA PAULA CARDOSO"
            "data_nascimento" = "1990/02/07"},
        "2021FLA002":{
            "nome" = "FLAVIO BITTENCOURT SOARES"
            "data_nascimento" = "1996/06/12"},
        }

        manipula esses dados para texto para mandar para a front:
        texto = '''
        id_aluno | nome
        id_aluno | nome
        id_aluno | nome
        '''

        :return: texto
        """



    def cadastrar_prova(prova_cadastrada):
        """
        API POST
        Checa se a chave_escola é válida


        RECEBIMENTO DO CORPO
        Recebe o dicionário prova_cadastrada
        VERIFICAÇÕES
        checa se a prova tem titulo
        checa se a prova tem id (e se é único)  - transforma em upper
        Checa se a prova não está vazia (se existem keys), se tem menos que 20 keys e se as keys são int
        transforma todos os valores em upper
        checa se todas os values pertencem à lista ["A", "B", "C", "D", "E", ""]
        Checa se todas as perguntas tem um peso int >0
        checa se a soma dos pesos é igual a 10

        O QUE É ESPERADO de prova_cadastrada:
        {"id_prova":"FISI02",
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

        ARMAZENAMENTO
        passa esse dicionário para database.escola que vai armazenar

        :return: mensagem de sucesso ou erro.
        """
        pass




