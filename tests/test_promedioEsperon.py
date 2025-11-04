from funciones.PromedioEsperon import promedioesperon

def test_promedioesperon():
    assert PromedioEsperon([2, 4, 6]) == 4
    assert PromedioEsperon([]) is None 