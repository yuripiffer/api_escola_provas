

class DbEscola():

    #monta conexão com o db e collection correta

    def valida_nome_aluno(self, nome):
        """
        checa se não é nulo
        transforma em upper
        retorna false se não houver no banco
        returna o nome manipulado se puder ser colocado no banco
        :return: nome (ou erro)
        """
        return nome

    def valida_data_nascimento(self, data_nascimento):
        """
        checa se não é nulo
        transforma no formato correto
        checa se não é hoje
        :return: data_nascimento ou False
        """
        return data_nascimento

    def existe_id_aluno(self, id_aluno):
        # se já existe
        #     return True
        # se não:
        #     return False
        pass

    def persistir_aluno(self, dict_matricula):
        #recebe
        # {
        #     "nome" = "FULANINHO",
        #     "id_aluno" = "2021YU231",
        #     "data_nascimento" = "04/10/1991"
        # }

        # se persistir:
        #     return True
        # se não:
        #     return False
        pass


    def retornar_alunos(self):
        """
        retonra os dados de todos os alunos do db
        se conseguir:
            return arquivo_alunos (não sei qual o formato que vai voltar)
        se tiver problema:
            return False
        :return:
        """

    def valida_id_prova(self, id_prova):
        """
        id_prova = id_prova.upper()[0:8] ----> (recorta a string em 8)
        chega se a prova já existe no banco de dados
        se existe:
            return False
        se nao existe:
            return id_prova
        :return: id_prova ou False
        """
        pass

    def persistir_prova_cadastrada(self, lista_dados):
        """
        recebe:
        [id_prova, titulo_prova, total_perguntas, lista_alternativas, lista_pesos ]
        Persiste no banco
        if CORRER TUDO BEM:
            return True
        else:
            return False
        """
        pass