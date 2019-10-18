# Linguagem de Programação II
# AC06 ADS2D - Faculdade
# alunos: julio.fernando@aluno.faculdadeimpacta.com.br
#         tiago.souza@aluno.faculdadeimpacta.com.br


class Disciplina:
    '''
    Abstração de uma disciplinai, possui os atributos Nome e carga Horária
    '''
    def __init__(self, nome: str, carga_horaria: int) -> None:
        self._nome = nome
        self._carga_horaria = carga_horaria

    def get_nome(self) -> str:
        '''
        Acessor do atributo nome
        '''
        return self._nome

    def get_carga_horaria(self) -> int:
        '''
        Acessor do atributo cargar horaria
        '''
        return self._carga_horaria


class Pessoa:
    '''
    Abstração de uma pessoa no Modelo, classe base para Aluno e Professor
    que contém dados pertencentes a ambos.
    '''
    def __init__(self, nome: str, telefone: int, email: float) -> None:
        self._nome = nome
        self.set_telefone(telefone)
        self.set_email(email)

    def get_nome(self) -> str:
        '''
        Acessor do atributo Nome
        '''
        return self._nome

    def get_telefone(self) -> int:
        '''
        Acessor do atributo telefone
        '''
        return self._telefone

    def set_telefone(self, novo_telefone: int) -> None:
        '''
        Mutador do atributo telefone deve checar se é um número inteiro e,
        caso contrário devolver um TypeError
        '''
        if type(novo_telefone) is not int:
            raise TypeError("O número dever ser inteiro")
        else:
            self._telefone = novo_telefone

    def get_email(self) -> str:
        '''
        Acessor do atributo email
        '''
        return self._email

    def set_email(self, novo_email) -> None:
        '''
        Mutador do atributo eail, deve checar se éum email válido
        (se possuir o caractere '@') e caso contrário devolver
        um ValueError
        '''
        if type(novo_email) is not str or " " in novo_email:
            raise ValueError("O formato de email é inválido")
        elif "@" not in novo_email or novo_email.count("@") != 1:
            raise ValueError("O formato de email é inválido")
        elif novo_email.index("@") < 2 \
                or novo_email.index("@") >= len(novo_email) - 5:
            raise ValueError("O formato de email é inválido")
        else:
            self._email = novo_email


class Aluno(Pessoa):

    def __init__(self, nome: str, telefone: int,
                 email: str, n_matricula: int) -> None:
        self._nome = nome
        self.set_telefone(telefone)
        self.set_email(email)
        self._n_matricula = n_matricula
        self._diciplinas = []

    def get_matricula(self) -> int:
        '''
        Acessor do atributo matricula
        '''
        return self._n_matricula

    def matricular(self, disciplina: Disciplina) -> None:
        '''
        Realiza matrícula do Aluno na disciplina
        '''
        self._diciplinas.append(disciplina)

    def lista_disciplinas(self) -> list:
        '''
        Devolve a lista de disciplinas em que o aluno esta matriculado
        '''
        return self._diciplinas


class Professor(Pessoa):
    '''
    Entidade professor do Modelo
    '''
    def __init__(self, nome, telefone, email):
        super().__init__(nome, telefone, email)
        self._disciplina = []
        self._limite_horas = 200

    def ministra(self, disciplina: Disciplina) -> None:
        '''
        Atribui o professor como ministrante da disiciplina
        Um professor não pode dar mais de 200 horas de aula,
        Caso um professor tente atribuir mais de 200h devolve
        ValueError
        '''
        horas_aula = 0
        for i in self._disciplina:
            horas_aula += i._carga_horaria
        if horas_aula + disciplina._carga_horaria > self._limite_horas:
            raise ValueError(f"Carga horaria superior a {self._limite_horas}")
        else:
            self._disciplina.append(disciplina)

    def lista_disciplinas(self) -> list:
        '''
        lista as disciplinas ministradas pelo professor
        '''
        return self._disciplina
