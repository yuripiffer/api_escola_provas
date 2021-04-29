
class DbAluno():

    #monta conexão com o db e collection correta

    def does_id_aluno_exist(self, id_aluno):
        """
        Checa no banco de dados se esse id_aluno existe ou não
        :param id_aluno:
        :return: bool
        """
        pass

    def retonra_provas_existentes(self):
        """
        Vai no banco de dados e retorna as provas existentes
        COMO RETORNA ESSES DADOS??
        :return: dict,
        """

    def does_id_prova_exist(self, id_escola):
        """
        Checa no db se id_escola existe
        :return: bool
        """
    def buscar_info_prova(self, id_prova):
        """
        Busca no db o titulo_prova e total de perguntas da prova
        :return: ["titulo_prova", "total_perguntas"] ou False
        """

    def retornar_prova_cadastrada(self, id_prova):
        """
        retorna
            {"cadastro_prova" = {
            "id_prova" = "HIST034",
            "titulo_prova" = "Historia da Arte 2",
            "lista_alternativas" = ["A", "C", "B", "A"]
            "lista_pesos" = [1.5,3,3,2.5],
            "total_perguntas" = 4
            }
        :param id_prova:
        :return:
        """
        pass

    def persistir_nota_aluno(self, id_aluno, id_prova, lista_respostas, nota):
        #armazenar
        # se conseguir, return True
        # se não conseguir, return False

        pass