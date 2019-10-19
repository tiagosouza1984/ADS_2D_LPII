from typing import List

__alunos__ = ['tiago.souza@aluno.faculdadeimpacta.com.br',
              'gerson.gonzales@aluno.faculdadeimpacta.com.br']


class Pessoa:
    '''
    Abstração de pessoa:
    '''
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade


class Funcionario(Pessoa):
    '''
    Classe Abstrata funcionário.
    '''
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)

    def calcula_salario(self) -> float:
        '''
        Calcula o salário do Mês para o funcionário
        '''
        raise NotImplementedError

    def altera_carga_horaria(self, nova_carga_horaria: int) -> None:
        '''
        altera a carga horária do funcionário, respeitando o limite,
        de horas por categoria.
        Caso o numero informado seja inválido, da raise em um ValueError
        '''
        raise NotImplementedError

    def consulta_carga_horaria(self) -> int:
        '''
        Devolve a carga horária de trabalho do funcionário
        '''

        raise NotImplementedError

    def aumenta_salario(self) -> None:
        '''
        Da um aumento de 5% no valor da hora trabalhada para o funcionário
        '''
        raise NotImplementedError


class Programador(Funcionario):
    '''
    Funcionário do tipo programador, salario base por hora 35,00.
    Regime de trabalho deve estar entre 20 e 40h semanais,
    caso contrário devolve um ValueError.
    Para efeito de cálculo de pagamento o mês possui 4,5 semanas
    '''
    def __init__(self, nome: str, idade: int, email: str,
                 carga_horaria_semanal: int = 40):
        super().__init__(nome, idade)
        self._email = email
        self.altera_carga_horaria(carga_horaria_semanal)
        self._salary_hour = 35.00

    def calcula_salario(self):
        '''
        Calcula o salário do Mês para o funcionário
        '''
        return self._salary_hour * self._carga_horaria_semanal * 4.5

    def altera_carga_horaria(self, nova_carga_horaria):

        if nova_carga_horaria < 20 or nova_carga_horaria > 40:
            raise ValueError("Carga horária inválida")
        else:
            self._carga_horaria_semanal = nova_carga_horaria

    def consulta_carga_horaria(self):
        '''
        Devolve a carga horária de trabalho do funcionário
        '''
        return self._carga_horaria_semanal

    def aumenta_salario(self):
        '''
        Da um aumento de 5% no valor da hora trabalhada para o funcionário
        '''
        self._salary_hour += self._salary_hour * 0.05


class Estagiario(Funcionario):
    '''
    Funcionário do tipo estagiário, salario base por hora 15,50
    e auxilio alimentação de 250 reais por mês.
    Regime de trabalho deve estar entre 16h e 30h semanais,
    caso contrário da raise em um ValueError.
    Para efeito de cálculo de salário o mês possui 4,5 semanas
    '''
    def __init__(self, nome: str, idade: int, email: str,
                 carga_horaria_semanal: int = 20):
        super().__init__(nome, idade)
        self._email = email
        self.altera_carga_horaria(carga_horaria_semanal)
        self._salary_hour = 15.50

    def calcula_salario(self):
        '''
        Calcula o salário do Mês para o funcionário
        '''
        return self._salary_hour * self._carga_horaria_semanal * 4.5 + 250.00

    def altera_carga_horaria(self, nova_carga_horaria):
        if nova_carga_horaria < 16 or nova_carga_horaria > 30:
            raise ValueError("Carga horária inválida")
        else:
            self._carga_horaria_semanal = nova_carga_horaria

    def consulta_carga_horaria(self):
        '''
        Devolve a carga horária de trabalho do funcionário
        '''
        return self._carga_horaria_semanal

    def aumenta_salario(self):
        '''
        Da um aumento de 5% no valor da hora trabalhada para o funcionário
        '''
        self._salary_hour += self._salary_hour * 0.05


class Empresa:
    '''
    Classe empresa, gerencia diversos funcionários
    '''
    def __init__(self, nome: str, cnpj: int, area_atuacao: str,
                 equipe: List[Funcionario] = []):
        self._nome = nome
        self._cnpj = cnpj
        self._area_atuacao = area_atuacao
        self._equipe = []

        for i in range(len(equipe)):
            self._equipe.append(equipe[i])

    def contrata(self, novo_funcionario: Funcionario):
        '''
        Contrata um novo funcionário para a empresa
        '''
        self._equipe.append(novo_funcionario)

    def lista_fucionarios(self) -> List[Funcionario]:
        '''
        Devolve um lista com todos os funcionarios
        '''
        return self._equipe

    def folha_pagamento(self):
        '''
        Devolve o montante total gasto com pagamento dos funcionários
        '''
        
        self._folha = 0
        for i in range(len(self._equipe)):
            self._folha += self._equipe[i].calcula_salario()
        return self._folha

    def dissidio_anual(self):
        '''
        Aumenta o valor da hora trabalhada em 5% para todos os funcionários
        '''
        for i in range(len(self._equipe)):
            self._equipe[i].aumenta_salario()


if __name__ == "__main__":
    est = Estagiario("Tiago", 35, "tiago.souza@wikimee.com")
    pgr = Programador("Luba", 35, "tiago.souza@wikimee.com")
    empresa = Empresa("Alvosoft", 12333456000124, "t.i", pgr)
    empresa.contrata(est)
    print(empresa.lista_fucionarios())
    print(empresa.folha_pagamento())
