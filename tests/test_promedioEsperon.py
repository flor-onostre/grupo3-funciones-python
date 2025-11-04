from funciones.promedio import PromedioEsperon

def test_promedioEsperon():
    assert promedio([2, 4, 6]) == 4
    assert promedio([]) is None
