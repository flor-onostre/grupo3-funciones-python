from funciones.PromedioEsperon import PromedioEsperon

def test_promedioesperon():
    assert PromedioEsperon([2, 4, 6]) == 4
    assert PromedioEsperon([]) is None