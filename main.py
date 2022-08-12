class Pessoa(object):
    def __init__(self, nome):
        self.nome = nome


class Professor(Pessoa):
    def __init__(self, especialidade, nome):
        Pessoa.__init__(self, nome)
        self.especialidade = especialidade

    def to_string(self):
        return 'O professor %s da especialidade %s' % (self.nome, self.especialidade)


class Aluno(Pessoa):
    def __init__(self, matricula: int, curso: str, periodo: int, nome: str):
        super().__init__(nome)
        self.matricula = matricula
        self.curso = curso
        self.periodo = periodo

    def to_string(self):
        return 'O aluno %s do curso %s do periodo %s' % (self.nome, self.curso, self.periodo)


class Aula:
    def __init__(self, assunto):
        self.assunto = assunto
        self.professor: Professor = None
        self.alunos: list[Aluno] = []

    def getListaPresenca(self) -> str:
        lista = f'''
        Aula de {self.assunto}
            Professor: {self.professor.to_string()}
        '''

        for aluno in self.alunos:
            lista += f'\n    {aluno.to_string()}'
        return lista


a1 = Aluno(25, 'GES', 7, 'Ana')
a2 = Aluno(10, 'GET', 2, 'Maria')

p1 = Professor('Banco de dados', 'Renzo')
Aula1 = Aula('Mongo')
Aula1.professor = p1
Aula1.alunos.append(a1)
Aula1.alunos.append(a2)

print(Aula1.getListaPresenca())
