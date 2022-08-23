
class Pessoa(object):
    def __init__(self, nome)-> None:
        self.nome = nome

class Professor(Pessoa):
    def __init__(self,especialidade, nome) -> None:
        Pessoa.__init__(self,nome)
        self.especialidade = especialidade

    def __str__(self) -> str:
        return f"{self.nome}"

class Aluno(Pessoa):
    def __init__(self, matricula, curso, periodo, nome)-> None:
        super().__init__(nome)
        self.matricula = int(matricula)
        self.curso = curso
        self.periodo = int(periodo)

    def __str__(self) -> str:
        return f"O aluno {self.nome} da matricula {self.matricula} do curso {self.curso} do periodo {self.periodo}"

class Aula:
    def __init__(self, assunto):
        self.assunto = assunto
        self.professor : Professor = None
        self.alunos : list[Aluno] = []

    def getListaPresenca(self) -> str:
        lista = ''
        for aluno in self.alunos:
            lista = lista + f'''
            nome: {aluno.nome}
            matricula: {aluno.matricula}
            curso: {aluno.curso}
            periodo: {aluno.periodo}
            '''
        return lista

    def __str__(self):
        info = f"Aula de {self.assunto}"
        info += f"\n    Professor: {self.professor}"
        info += f"\n    Alunos Presentes:\n {self.getListaPresenca()}"
        return info

a1 = Aluno(25, 'GES', 7,'Ana')
a2 = Aluno(10, 'GET', 2, 'Maria')

p1 = Professor('Banco de dados', 'Renzo')
Aula1 = Aula('Mongo')
Aula1.professor = p1
Aula1.alunos.append(a1)
Aula1.alunos.append(a2)

print(Aula1)