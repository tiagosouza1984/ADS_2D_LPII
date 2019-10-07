class Pai:
    def __init__(self, nome):
        self.nome = nome

    def diz_oi(self):
        print('hello world')
    

class Filho(Pai):
    def andar_de_bicicleta(self):
        print(f'{self.nome} está andando de bicicleta')

class Numero(int):
    def __str__(self):
       return str(self.bit_length())

if __name__ == "__main__":
    p = Pai("Orlando")
    f = Filho("Tiago")
    print(Numero(68))