from classes import Televisao


def test_cria_desligada():
    tv = Televisao("LG")
    assert not tv.ligada
    assert tv.canal is None


def test_ligar():
    tv = Televisao("samsung")
    tv.ligar()
    assert tv.ligada
    assert tv.canal is not None


def test_aumenta_canal():
    tv = Televisao("samsung")
    tv.ligar()
    canal_anterior = tv.canal
    tv.aumenta_canal()
    assert tv.canal == canal_anterior + 1


def test_aumenta_canal_desligada():
    tv = Televisao("samsung")
    tv.aumenta_canal()
    assert not tv.ligada
    assert tv.canal is None


def test_diminui_canal():
    tv = Televisao("samsung")
    tv.ligar()
    canal_anterior = tv.canal
    tv.diminui_canal()
    assert tv.canal == canal_anterior - 1


def test_diminui_canal_desligada():
    tv = Televisao("samsung")
    tv.diminui_canal()
    assert not tv.ligada
    assert tv.canal is None


def test_pula_canal():
    tv = Televisao("samsung")
    tv.ligar()
    tv.pula_canal(10)
    assert tv.canal == 10


def test_pula_canal_desligada():
    tv = Televisao("samsung")
    tv.pula_canal(10)
    assert not tv.ligada
    assert tv.canal is None


def test_desligar():
    tv = Televisao("samsung")
    tv.ligar()
    tv.desligar()
    assert not tv.ligada
    assert tv.canal is None
