from database.db_aluno import DbAluno

db_aluno = DbAluno()

class Aluno:

    def listar_provas(self, id_aluno) -> dict or tuple:
        if not db_aluno.does_id_aluno_exist(id_aluno):
            return "Id não existe ou informado incorretamente.", 400
        dict_info = db_aluno.retonra_provas_existentes()
        if not dict_info:
            return "Falha no carregamento das provas (banco de dados).", 400
        return dict_info, 200

    def listar_informacoes_prova(self, id_aluno, id_prova):
        if not db_aluno.does_id_aluno_exist(id_aluno):
            return "O id_aluno não existe ou informado incorretamente.", 400
        if not db_aluno.does_id_prova_exist(id_prova):
            return "Prova inexistente ou id informado incorretamente.", 400

        lista_info = db_aluno.buscar_info_prova(id_prova)
        titulo_prova =  lista_info[0]
        total_perguntas = lista_info[1]
        return f"id_prova = {id_prova} " \
               f"\nTítulo da prova: {titulo_prova} " \
               f"\nTotal de perguntas: {total_perguntas}", 200

    def realizar_prova(self, dict_respostas):
        id_aluno = dict_respostas["id_aluno"]
        id_prova = dict_respostas["id_prova"]
        lista_respostas = dict_respostas["lista_respostas"]

        if not db_aluno.does_id_aluno_exist(id_aluno):
            return "O id_aluno não existe ou informado incorretamente.", 400
        if not db_aluno.does_id_prova_exist(id_prova):
            return "Prova inexistente ou id informado incorretamente.", 400

        dict_prova_cadastrada = db_aluno.retornar_prova_cadastrada(id_prova)
        if not dict_prova_cadastrada:
            return "Falha no carregamento dos dados do gabarito da prova (banco de dados)", 400

        lista_alternativas = dict_prova_cadastrada["lista_alternativas"]
        lista_pesos = dict_prova_cadastrada["lista_pesos"]

        if len(lista_respostas) != len(lista_alternativas):
            return f"Diferença no total de alternativas respondidas ({len(lista_respostas)}) " \
                   f"e total de questões cadastradas ({len(lista_alternativas)})!!", 400
        if len(lista_alternativas) != len(lista_pesos):
            return "Problemas com os dados cadastrados da prova!! Total de questões e total" \
                   "de pesos diferentes.", 400

        nota = self.calcula_nota(lista_alternativas,lista_respostas,lista_pesos)

        mensagem = f"LANÇAMENTO DE NOTA\n Id_prova: {id_prova}:" \
                   f"\nId_aluno(a): {id_aluno}\nNota: {nota}\n"

        if db_aluno.persistir_nota_aluno(id_aluno, id_prova, lista_respostas, nota):
            mensagem += "Dados armazenados com sucesso."
        return mensagem, 400


    def calcula_nota(self,lista_alternativas,lista_respostas,lista_pesos):
        nota = 0.0
        for i in range(len(lista_alternativas)):
            if lista_respostas[i] == lista_alternativas[0]:
                nota += lista_pesos[i]
        return nota
