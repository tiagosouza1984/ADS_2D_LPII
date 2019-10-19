class Televisao:
    def __init__(self):
        self.marca = "marca"
        self.ligada = False
        self.canal = None
        self.max_canal = 500

    # parâmetro self precisa ser obrigatório no primeiro método de uma classe
    def ligar(self):
        if self.ligada is False:
            self.ligada = True
            self.canal = 1

    def aumenta_canal(self):
        if self.ligada:
            self.pula_canal(self.canal + 1)

    def diminui_canal(self):
        if self.ligada:
            self.pula_canal(self.canal - 1)

    def pula_canal(self, novo_canal):
        if self.ligada and novo_canal > 0 and novo_canal < self.max_canal:
            self.canal == novo_canal

    def desligar(self):
        if self.ligada:
            self.ligada = False
            self.canal = None
