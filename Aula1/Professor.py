from Pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

    def toString(self):
        return f'''
        nome: {self.nome}
        especialidade: {self.especialidade}
        '''


