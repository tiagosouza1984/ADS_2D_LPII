from classes import Televisao


class Controle:
    def __init__(self, televisao: Televisao):
        self.tv = televisao

    def liga_desliga(self):
        if self.tv.is_ligada():
            self.tv.desligar()
        else:
            self.tv.set_ligada(True)
    
    def aumenta_canal(self):
        self.tv.aumenta_canal()
    
    def diminui_canal(self):
        self.tv.diminui_canal

    def troca_canal(self, canal):
        self.tv.pula_canal(canal)


if __name__ == '__main__':
    tv_sala = Televisao('LG')
    controle_sala = Controle(tv_sala)

    print(tv_sala.is_ligada())
    controle_sala.liga_desliga()
    print(tv_sala.is_ligada())


if __name__ == '__main__':
    tv_sala = Televisao('LG')
    controle_sala = Controle(tv_sala)
    print(tv_sala.is_ligada())
    controle_sala.liga_desliga()
    
    tv_sala.aumenta_canal()
    print(tv_sala.canal)
