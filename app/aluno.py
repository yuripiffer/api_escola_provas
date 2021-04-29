from database.db_aluno import DbAluno

class Aluno():

    def listar_provas(self, id_aluno):
        if not DbAluno.does_id_aluno_exist(id_aluno):
            return "Id não existe ou informado incorretamente."
        dados_provas = DbAluno.retonra_provas_existentes()
        if not dados_provas:
            return "Falha no carregamento das provas (banco de dados)."

        # MANIPUlar dados_provas para apresentar na front
            #return string com provas cadastradas
        pass

    def listar_informacoes_prova(self, id_aluno, id_prova):
        if not DbAluno.does_id_aluno_exist(id_aluno):
            return "O id_aluno não existe ou informado incorretamente."
        if not DbAluno.does_id_prova_exist(id_prova):
            return "Prova inexistente ou id informado incorretamente."

        lista_info = DbAluno.buscar_info_prova(id_prova)
        titulo_prova =  lista_info[0]
        total_perguntas = lista_info[1]
        return f"id_prova = {id_prova} " \
               f"\nTítulo da prova: {titulo_prova} " \
               f"\nTotal de perguntas: {total_perguntas}"

    def realizar_prova(self, dict_respostas):
        id_aluno = dict_respostas["id_aluno"]
        id_prova = dict_respostas["id_prova"]
        lista_respostas = dict_respostas["lista_respostas"]

        if not DbAluno.does_id_aluno_exist(id_aluno):
            return "O id_aluno não existe ou informado incorretamente."
        if not DbAluno.does_id_prova_exist(id_prova):
            return "Prova inexistente ou id informado incorretamente."

        dict_prova_cadastrada = DbAluno.retornar_prova_cadastrada(id_prova)
        if not dict_prova_cadastrada:
            return "Falha no carregamento dos dados do gabarito da prova (banco de dados)"

        lista_alternativas = dict_prova_cadastrada["lista_alternativas"]
        lista_pesos = dict_prova_cadastrada["lista_pesos"]

        if len(lista_respostas) != len(lista_alternativas):
            return f"Diferença no total de alternativas respondidas ({len(lista_respostas)}) " \
                   f"e total de questões cadastradas ({len(lista_alternativas)})!!"
        if len(lista_alternativas) != len(lista_pesos):
            return "Problemas com os dados cadastrados da prova!! Total de questões e total" \
                   "de pesos diferentes."

        nota = self.calcula_nota(lista_alternativas,lista_respostas,lista_pesos)

        mensagem = f"LANÇAMENTO DE NOTA\n Id_prova: {id_prova}:" \
                   f"\nId_aluno(a): {id_aluno}\nNota: {nota}\n"

        if DbAluno.persistir_nota_aluno(id_aluno, id_prova, lista_respostas, nota):
            mensagem += "Dados armazenados com sucesso."
        return mensagem


    def calcula_nota(self,lista_alternativas,lista_respostas,lista_pesos):
        nota = 0.0
        for i in range(len(lista_alternativas)):
            if lista_respostas[i] == lista_alternativas[0]:
                nota += lista_pesos[i]
        return nota
