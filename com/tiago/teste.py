class Teste:
    def __init__(self, a: int):
        self.set_atr(a)

    def get_atr(self):
        return self._atr

    def set_atr(self, novo_a):
        if type(novo_a) is not int:
            raise TypeError('a deve ser int')
        self._atr = novo_a


if __name__ == '__main__':
    try:
        var = Teste('D')
    except TypeError:
        print('Deu ruim!')
    else:
        try:
            var.set_atr('c')
        except TypeError:
            print('deu ruim')
        else:
            print(var.get_atr())
