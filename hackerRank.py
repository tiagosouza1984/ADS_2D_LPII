import re


enter = int(input())
x = 0
flag = False
for i in range(enter):
    v = input()
    # verifica se a string possui letras ou char speciais
    x = re.findall("[^0-9 -]", v)
    if (x):
        flag = True
    # verifica quantidade de char decimais na string
    x = re.findall('\d', v)
    if len(x) != 16:
        flag = True
    # verifica primeiro digito da string
    x = re.findall('\A[0-9]', v)
    if x[0] != '4' and x[0] != '5' and x[0] != '6':
        flag = True
    # procura chars especiais na posição correta
    x = re.findall("[-]", v)
    if (x):
        pattern = '(\d{4})(\-{1})(\d{4})(\-{1})(\d{4})(\-{1})(\d{4})'
        match = re.search(pattern, v)
        if match:
            pass
        else:
            flag = True
    # procura espaços vazios na string
    x = re.findall("\s", v)
    if (x):
        flag = True
    x = re.findall('\d', v)
    z = list(x)
    cont = 0
    # verifica se há + de 3 números iguais em sequencia
    for indice, valor in enumerate(z):
        if indice == 0:
            cont = 1
        if indice > 0:
            if valor in z[indice] != z[indice-1]:
                cont = 1
            else:
                cont += 1
        if cont >= 4:
            flag = True
    # apos chacar tudo estando ok
    if not flag:
        print("Valid")
    else:
        print("Invalid")
        flag = False

