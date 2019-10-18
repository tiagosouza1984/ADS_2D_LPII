from banco import Cliente, Banco, Conta

b = Banco("Itau")
cl = Cliente("Tiago", 987314625, "tiago.souza@alvosoft.com.br")
cl2 = Cliente("Brenda", 987252345, "brendaoli@gmail.com")
b.abre_conta(cl, 300)
b.abre_conta(cl2, 500)
c = Conta(b._listaCliente[0], b._listaContas[0], 300)
c1 = Conta(b._listaCliente[1], b._listaContas[1], 300)
print(c.get_saldo())
c.saque(50)
print(c.extrato())
c.deposito(200)
print(c.extrato())
c.saque(25)
print(c.extrato())

print(b._listaContas[0].get_clientes())
print(cl.get_nome().isidentifier())
