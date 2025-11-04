from funciones.promedioesperon import promedioesperon

def test_promedioesperon():
    assert promedioesperon([2, 4, 6]) == 4
    assert promedioesperon([]) is None