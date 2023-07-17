# Pruebas en pytest
import pytest
from Calculadora import Calculadora

@pytest.fixture
def test_calculadora():
    return Calculadora()

def test_suma(test_calculadora):
    assert test_calculadora.sumar(2, 3) == 5

def test_suma2(test_calculadora):
    assert test_calculadora.sumar(10, 20) == 30

def test_suma2(test_calculadora):
    assert test_calculadora.sumar(2, 10) == 12

def test_resta(test_calculadora):
    assert test_calculadora.restar(5, 3) == 2

def test_resta2(test_calculadora):
    assert test_calculadora.restar(10, 1) == 9

def test_multiplicacion(test_calculadora):
    assert test_calculadora.multiplicar(4, 3) == 12

def test_division(test_calculadora):
    assert test_calculadora.dividir(10, 2) == 5
    with pytest.raises(ValueError):
        test_calculadora.dividir(10, 0)