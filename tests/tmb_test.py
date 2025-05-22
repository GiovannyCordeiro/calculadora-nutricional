import pytest  # type: ignore

from calculadora_nutricional.tmb import TMB


# ✅ Caminho feliz
@pytest.mark.parametrize("weight, height, age, gender", [
    (70, 170, 25, "male"),
    (60, 160, 30, "female"),
    (80, 180, 40, "m"),
    (55, 155, 20, "f"),
])
def test_tmb_valid_inputs(weight, height, age, gender):
    tmb = TMB(weight, height, age)
    result = tmb.calc(gender)
    assert isinstance(result, (int))
    assert result > 0


# ❌ Inputs inválidos
def test_tmb_gender_none():
    tmb = TMB(70, 170, 25)
    with pytest.raises(ValueError):
        tmb.calc(None)


def test_tmb_invalid_gender():
    tmb = TMB(70, 170, 25)
    result = tmb.calc("banana")  # Comportamento atual: trata como 'male'
    assert isinstance(result, (int))  # Considera como male_calc()


@pytest.mark.parametrize("weight, height, age", [
    ("peso", 170, 25),
    (70, "altura", 25),
    (70, 170, "idade"),
])
def test_tmb_invalid_types(weight, height, age):
    with pytest.raises((TypeError)):
        tmb = TMB(weight, height, age)
        tmb.calc("male")


# ⚠️ Testes de limites
@pytest.mark.parametrize("weight, height, age", [
    (0, 170, 25),
    (70, 0, 25),
    (70, 170, 0),
    (500, 250, 100),
    (-70, 170, 25),
])
def test_tmb_edge_cases(weight, height, age):
    tmb = TMB(weight, height, age)
    result = tmb.calc("male")
    assert isinstance(result, (int))
