from Animal import Animal


class Pato(Animal):
    def __init__(self, idade, genero, nome, corBico):
        self.idade = idade
        self.genero = genero
        self.nome = nome
        self.corBico = corBico
    
    def nadar(self):
        return f"O Pato {self.nome} está nadando"
    
    def toString(self):
        return f'''
        idade: {self.idade}
        genero: {self.genero}
        nome: {self.nome}
        corBico: {self.corBico}    
        '''
