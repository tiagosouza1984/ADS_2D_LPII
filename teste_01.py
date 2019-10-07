import reta


def test_reta_distancia():
    ponto_a = reta.Ponto(-2, 3)
    ponto_b = reta.Ponto(-5, -9)
    assert ponto_a.distancia(ponto_b) == 12.36931687685298


def test_deslocar():
    ponto = reta.Ponto(3, 4)
    ponto.desloca(5, -2)
    assert ponto.x == 8 and ponto.y == 2


def test_reta_pertence():
    reta1 = reta.Reta(2, -6)
    ponto = reta.Ponto(-5, 2)
    assert reta1.pertence(ponto) == False


def test_reta_interseccao():
    reta1 = reta.Reta(2, 0)
    reta2 = reta.Reta(-1, 0)
    ponto = reta1.interseccao(reta2)
    assert ponto.x == 0 and ponto.y == 0
