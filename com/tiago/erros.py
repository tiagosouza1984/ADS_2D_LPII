'''
condition = True
while(condition):
    numero  = float(input('digite um número diferente de zero: '))
    try:
        divisao =1 / numero
        condition = False
    except ZeroDivisionError:
        condition = True
    except NameError:
        print("essa variável não existe")
    else:
        print(divisao)

raise SyntaxError ( "erro de sintax")

from reta import Reta
try:
    r = Reta(1, 1)
except Exception:
    print("deu problema")
else:
    print(r.a, r.b)
'''
class Teste:
    def __init__ (self, a : int):
        if type(a) is not int:
            raise TypeError('a deve ser um int')
        self.set_atr(a)

    def get_atr(self):
        return self._atr

    def set_atr(self, novo_a):
    if type(novo_a) is not int:
        self._atr= novo_a

if __name__ == "__main__":
    try:
        var = Teste(1)
    except TypeError:
        print("Deu ruim")
    else:
        try:
            var.set_atr("c")
        except TypeError:
            var.get_atr()
