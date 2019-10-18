# Linguagem de Programação II
# AC03 ADS2D - Retas
#
# alunos: julio.fernando@alunofaculdadeimpacta.com.br
#         tiago.souza@aluno.faculdadeimpacta.com.br


import math


class Ponto():
    '''
    Implementa a abstração de um ponto no plano Cartesiano 2D,
    que possui como atributos as coordenadas x e y
    '''

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def desloca(self, dx: float, dy: float) -> None:
        '''
        Desloca o ponto em dx no eixo x e dy no eixo y
        '''
        self.x += dx
        self.y += dy

    def distancia(self, ponto: 'Ponto') -> float:
        '''
        Calcula a distância euclidiana em relação a outro ponto
        passado como argumento
        '''
        res = (self.x - ponto.x)**2 + (self.y - ponto.y)**2
        return(math.sqrt(res))


class Reta():
    '''
    Cria a abstração de uma reta no plano cartesiano 2D e tem como atributos
    o coeficiente linear "a" e a instersecção com o eixo y "b".
    '''
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def pertence(self, ponto: Ponto) -> bool:
        '''
        Devolve 'True' se o ponto pertence a reta e 'False' caso contrário
        '''
        if ponto.y == self.a * ponto.x + self.b:
            return True
        else:
            return False

    def eh_paralela(self, outra_reta: 'Reta') -> bool:
        '''
        Retorna 'True' se a reta é paralela a 'outra_reta' e 'False'
        caso contrário
        '''
        if self.a == outra_reta.a:
            return True
        else:
            return False

    def interseccao(self, outra_reta: 'Reta') -> Ponto:
        '''
        Retorna o ponto de intersecção com a outra_reta (passada como
        argumento) caso não haja intersecção retorna 'None'.
        '''
        if self.eh_paralela(outra_reta):
            return None
        else:
            x = (outra_reta.b - self.b) / (self.a - outra_reta.a)
            y = (self.a * x) + self.b
            return Ponto(x, y)

    def perpendicular(self, ponto: Ponto) -> 'Reta':
        '''
        BÔNUS:
        Cria uma reta perpencidular à esta reta que passa por ponto
        '''
        a = -1 / self.a
        b = ponto.y - a * ponto.x
        return Reta(a, b)


if __name__ == "__main__":
    p = Ponto(0, 0)
    q = Ponto(3, 4)
    print(q.distancia(p))
    r = Reta(5, 0)
    print(r.pertence(p))
    print(r.pertence(q))
