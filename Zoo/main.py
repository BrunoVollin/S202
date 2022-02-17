from Pato import Pato
from Leao import Leao
from Zoologico import Zoologico

pato = Pato(nome="duck", idade=1, genero="M", corBico="Laranja")

leao = Leao(nome="dalva", genero="F", idade=2, selvagem=False)

animais = [pato, leao]

zoo = Zoologico(animais=animais)

print(zoo.getAnimais())