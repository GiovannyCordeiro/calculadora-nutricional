import pytest
from calculadora_nutricional.get import GET

def test_instancia_get():
    get = GET(1600, 3)
    assert get.tmb == 1600
    assert get.nivel_atividade == 3

def test_definir_nivel_atividade_1():
    get = GET(1500, 1)
    assert get.definir_nivel_atividade() == 1.2

def test_definir_nivel_atividade_invalido():
    get = GET(1500, -1)
    assert get.definir_nivel_atividade() == 0

def test_calc_com_tmb_zero():
    get = GET(0, 3)
    assert get.calc() == 0.0

def test_calc_com_nivel_invalido():
    get = GET(1800, 42)
    assert get.calc() == 0
