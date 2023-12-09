# escribe "pytest" en la consola y ejecuta todos los test

from src.codificador import codificador

def test_caracteres_no_repetidos():
    assert codificador("din") == "((("

def test_caracteres_repetidos():
    assert codificador("eee") == ")))"