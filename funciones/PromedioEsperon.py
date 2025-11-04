def promedio(numeros):
    """Devuelve el promedio de una lista de números."""
    if not numeros:
        return None
    return sum(numeros) / len(numeros)
from funciones.promedio import promedio

def test_promedio():
    assert promedio([2, 4, 6]) == 4
    assert promedio([]) is None
