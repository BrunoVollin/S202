class Zoologico():
    def __init__(self, animais):
        self.animais = animais

    def getAnimais(self):
        listaAnimais = "Lista de animais\n"

        for animal in self.animais:
            listaAnimais += animal.toString()
        
        return listaAnimais