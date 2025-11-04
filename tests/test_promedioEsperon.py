from funciones.promedioesperon import promedioesperon

def test_promedioEsperon():
    assert promedio([2, 4, 6]) == 4
    assert promedio([]) is None
