meu_numero = 5
meu_dict = {'chave1': meu_numero}
# acessar item do dicionario
# print(meu_dict)
meu_dict['nova_chave'] = 'novo_valor'
# checar se existe chave
# print(chave1in meu_dict)
# Dicionário aninhado (dicionário dentro de outro dicionário)
lista_contatos = {
    'id_0': {
        'nome': 'Tiago', 'email':
        'tiago.souza@aluno.faculdadeimpacta.com.br',
        'idade': meu_numero, 'sexo': 'masculino'
    },
    'id_1': {
        'nome': 'Fernanda', 'email':
        'fernanda.teixeira@aluno.faculdadeimpacta.com.br',
        'idade': '19', 'sexo': 'feminino'
    }
}


for chave, valor in lista_contatos.items():
    print("Usuário:", chave)
    for chave_name in valor:
        print(chave_name, valor[chave_name])
# print(lista_contatos['Tiago']['nome'], [lista_contatos['Tiago']['email']])
##################################
lista = list("tiago")
dicionario = {'joão': 2, 'Maria': 4, 'José': 9, 'Pedro': 12}
novalista = []
# classe enumerate() retorna posição(índice) e valor da posição
'''
for indice, valor in enumerate(lista):
    print(indice, valor)
# função itens() é semelhante a enumerate
for chave, valor in dicionario.items():
    print(f"o valor de {chave} é {valor}")
'''
