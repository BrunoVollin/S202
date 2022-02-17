from Pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, matricula, curso, periodo):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.periodo = periodo

    def toString(self):
        return f'''
        nome: {self.nome}
        matricula: {self.matricula}
        curso: {self.curso}
        periodo: {self.periodo}
        '''


