from banco import Conta, Cliente

ct1 = Conta([], 1, 350.00)
print(ct1.mensagem)
ct1.mensagem = "mudei atributo"
print(ct1.set_mensagem(ct1.mensagem))

#list comprehension
a = [x**3 for x in range(3)]
print(a)

cl1 = Cliente("Tiago", 988085661, "tiago.souza@alvosoft.com.br")
print(cl1.email())