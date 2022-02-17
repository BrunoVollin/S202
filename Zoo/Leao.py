from Animal import Animal


class Leao(Animal):
    def __init__(self, idade, genero, nome, selvagem):
        self.idade = idade
        self.genero = genero
        self.nome = nome
        self.selvagem = selvagem
    
    def correr(self):
        return f"O leão {self.nome} está correndo"
    
    def toString(self):
        return f'''
        idade: {self.idade}
        genero: {self.genero}
        nome: {self.nome}
        selvagem: {self.selvagem}    
        '''
