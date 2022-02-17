from Aluno import Aluno
from Aula import Aula
from Professor import Professor


aluno1 = Aluno(
    nome="Bruno",
    matricula="34",
    curso="GES",
    periodo=7
)
aluno2 = Aluno(
    nome="Leonardo",
    matricula="44",
    curso="GES",
    periodo=7
)
aluno3 = Aluno(
    nome="Davi",
    matricula="54",
    curso="GES",
    periodo=7
)

alunos = [aluno1, aluno2, aluno3]

professor = Professor(nome="Renzo", especialidade="Computacao")

aula = Aula(assunto="MongoDB", professor=professor, alunos=alunos )

print(aula.getListaPresenca())