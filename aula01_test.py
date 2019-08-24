import aula01 as a1


def test_eh_primo_8():
    primos = a1.listaPrimos(8)
    assert len(primos) == 4
