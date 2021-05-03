import pymongo
import pandas as pd


class DbAluno():
    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.conn['escola_genesis']
        self.alunos_genesis = self.db['alunos_genesis']
        self.cadastro_provas_genesis = self.db['cadastro_provas_genesis']
        self.provas_realizadas_genesis = self.db['provas_realizadas_genesis']

    def does_id_aluno_exist(self, id_aluno) -> bool:
        resultado = self.alunos_genesis.find({'id_aluno':id_aluno})
        resultado = resultado.count()
        if resultado > 0:
            return True

    def retonra_provas_existentes(self) -> dict:
        resultado = self.cadastro_provas_genesis.find({})
        df = pd.DataFrame(resultado)
        dict_info = df[["id_prova", "titulo_prova"]].to_json(orient="records")
        return dict_info

    def does_id_prova_exist(self, id_prova) -> bool:
        resultado = self.cadastro_provas_genesis.find({'id_prova':id_prova})
        resultado = resultado.count()
        if resultado > 0:
            return True

    def buscar_info_prova(self, id_prova) -> list:
        """
        :return: ex: ['HIST003', 'História da Arte - Barroco Italiano', 3.0]
        """
        resultado = self.cadastro_provas_genesis.find({"id_prova":id_prova})
        df = pd.DataFrame(resultado)
        lista_info = df[["id_prova", "titulo_prova", "total_perguntas"]].values.tolist()
        return lista_info[0]

    def persistir_nota_aluno(self, id_aluno, id_prova, lista_respostas, nota) -> bool:
        executa = self.provas_realizadas_genesis.insert_one({
            "id_aluno":id_aluno,
            "id_prova":id_prova,
            "lista_respostas":lista_respostas,
            "nota":nota
        })
        if executa.inserted_id:
            return True

    def retornar_prova_cadastrada(self, id_prova) -> dict or bool:
        resultado = self.cadastro_provas_genesis.find_one({"id_prova":id_prova})
        if resultado == None:
            return False
        df = pd.DataFrame(resultado)
        dict_info = df[["lista_alternativas","lista_pesos"]]
        return dict_info





#print(DbAluno().retornar_prova_cadastrada("MATE012"))



#DbAluno().does_id_aluno_exist("2021JO458")
#DbAluno().does_id_prova_exist("HIST003")
#resultado = DbAluno().retonra_provas_existentes()

# resultado = DbAluno().retonra_provas_existentes()
# print(resultado)
#print(teste)
#DbAluno().persistir_nota_aluno("2021JO243", "GEOG001", ["C","C","B"], 10.0)

