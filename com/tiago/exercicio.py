'''
3 classes, funcionario, programador e estagiario
atributos: hora_trabalho, qtd_hrs_trab

programador: linguagem_preferida
dar_aumento -. aumenta o salario em 6%
calcula_salario(self)
Estagiario
hora_trabalho* qtd_hrs_trab+ 150 +350
Programador
hora_trabalho* qtd_hrs_trab
'''


class Funcionario:
    def __init__(self, hora_trabalho: float, qtd_hrs_trab: int):
        self.hora_trabalho = hora_trabalho
        self.qtd_hrs_trab = qtd_hrs_trab

    def calcula_salario(self):
        return self.hora_trabalho * self.qtd_hrs_trab

    def dar_aumento(self):
        self.hora_trabalho += self.hora_trabalho * 1.06


class Programador(Funcionario):
    def __init__(
            self, hora_trabalho: float, qtd_hrs_trab: int,
            linguagem_preferida: str):
        self.hora_trabalho = hora_trabalho
        self.qtd_hrs_trab = qtd_hrs_trab
        self.linguagem_preferida = linguagem_preferida


class Estagiario(Funcionario):
    def calcula_salario(self):
        return super().calcula_salario() + 150 + 350


if __name__ == "__main__":
    p = Programador(18.00, 180, 'Python')
    e = Estagiario(9.00, 90)
    print(e.calcula_salario())
    e.dar_aumento()
    print(print(e.calcula_salario()))
