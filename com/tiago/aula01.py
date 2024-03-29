

def ehPrimo(num):
    '''
    Função que retorna true se é primo e false caso contrário
    ps: número 2 não entra no "for", ele já é considerado
    primo
    '''
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def ListaPrimos2(num):
    '''
    Função que retorna lista de primos até o número passado
    no parâmetro da função
    '''
    primos = []
    for i in range(2, num):
        if ehPrimo(i):
            primos.append(i)
    return primos


def listaPrimos(num):
    primos = []
    for i in range(2, num):
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False

        if primo:
            primos.append(i)
    return primos


if __name__ == "__main__":
    print(ListaPrimos2(5))
