from funciones.raiz_cuadrada_Romero import raiz_cuadrada_Romero

def test_raiz_cuadrada():
    assert raiz_cuadrada_Romero(9) == 3
    assert raiz_cuadrada_Romero(-4) is None