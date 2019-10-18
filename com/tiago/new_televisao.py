from aula_11_09 import Televisao

tv_sala = Televisao()
tv_quarto = Televisao()
tv_sala.ligar()
tv_quarto.ligar()

tv_sala.marca = 'Sony'
tv_sala.pula_canal(3)
print(tv_sala.marca)
print(tv_sala.canal)
