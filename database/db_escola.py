import pymongo
import pandas as pd

class DbEscola():

    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.conn['escola_genesis']
        self.alunos_genesis = self.db['alunos_genesis']
        self.cadastro_provas_genesis = self.db['cadastro_provas_genesis']
        self.provas_realizadas_genesis = self.db['provas_realizadas_genesis']

    def valida_nome_aluno(self, nome) -> str:
        """
        :return: nome validado, upper e inexistente no banco e upper OU False
        """
        if len(nome) == 0: #CHECAR SE NÃO É STRING TAMBÉM
            return False
        nome = nome.upper()
        resultado = self.alunos_genesis.find({'nome':nome})
        resultado = resultado.count()
        if resultado > 0:
            return False
        return nome

    def valida_data_nascimento(self, data_nascimento) -> str:
        """
        AINDA PRECISA FAZER
        checa se não é nulo
        transforma no formato correto
        checa se não é hoje
        :return: data_nascimento ou False
        """
        return data_nascimento

    def does_id_aluno_exist(self, id_aluno) -> bool:
        resultado = self.alunos_genesis.find({'id_aluno':id_aluno})
        resultado = resultado.count()
        if resultado > 0:
            return True

    def persistir_aluno(self, dict_matricula) -> bool:
        executa = self.alunos_genesis.insert_one(dict_matricula)
        if executa.inserted_id: #vÊ se realmente conseguiu
            return True

    def retornar_alunos(self) -> dict:
        """
        :return: json dos alunos
        """
        resultado = self.alunos_genesis.find({})
        dict_dados = pd.DataFrame(resultado)
        #o astype(str) é para evitar dar pau
        dict_dados = dict_dados.astype(str).to_json(orient="records")
        return dict_dados

    def valida_id_prova(self, id_prova) -> str:
        """
        :return: id_prova em upper com 8 char ou False
        """
        id_prova = id_prova.upper()[0:8]
        resultado = self.cadastro_provas_genesis.find({'id_prova':id_prova})
        resultado = resultado.count()
        if resultado > 0:
            return False
        else:
            return id_prova

    def persistir_prova_cadastrada(self, dict_dados) -> bool:
        executa = self.cadastro_provas_genesis.insert_one(dict_dados)
        if executa.inserted_id:  # vÊ se realmente conseguiu
            return True







# DbEscola().persistir_aluno({"id_aluno":"2021LI111",
#                             "nome":"LIVIA DELGADO",
#                             "data_nascimento":"01/01/2000"})
#DbEscola().persistir_prova_cadastrada(["QUIM001", "Química 3",2, ["B","B"],[4,6]])
