class Televisao:
    '''
    Classe Televisão
    Implementa a abstração de uma televisão
    Recebe como argumento de criação a marca da Televisão
    '''
    def __init__(self, marca: str):
        self.marca = marca
        self._ligada = False
        self.canal = None
        self.max_canal = 300

    def set_ligada(self, ligada: bool):
        if type(ligada) is bool:
            self._ligada = ligada
        else:
            print('Ligada só pode ser booleano')

    #método getter - só devolve o valor de um atributo sem modificá-lo
    def is_ligada(self):
        return self._ligada

    def ligar(self):
        '''
        Liga a tv se ela não estiver ligada.
        Inicializa o canal para 2.
        '''
        self._ligada = True
        self.canal = 2

    def aumenta_canal(self):
        self.pula_canal(self.canal + 1)

    def diminui_canal(self):
        self.pula_canal(self.canal - 1)

    def pula_canal(self, novo_canal):
        if self._ligada and novo_canal > 0 and novo_canal <= self.max_canal:
            self.canal = novo_canal

    def desligar(self):
        if self.ligada:
            self.ligada = False
            self.canal = None