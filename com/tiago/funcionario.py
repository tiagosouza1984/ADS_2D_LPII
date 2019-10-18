
class Funcionario:
    def __init__(self):
        self.nome = None
        self.email = None
        self.idade = None
        self.setor = None
        self.funcao = None


if __name__ == "__main__":
    employee01 = Funcionario()
    #employee01.nome = "Fecarol"
    employee02 = Funcionario()
    #print(employee01.nome)
    print(dir (employee01))
