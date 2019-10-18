import aula01 as a1


def divisores(N):
    divisores = []
    if a1.ehPrimo(N):
        return [N]
    for p in a1.ListaPrimos2(N):
        while N % p == 0:
            divisores.append(p)
            N = N / p
    return divisores


if __name__ == "__main__":
    print(divisores(6))
    print(divisores(512))
    print(divisores(19))
