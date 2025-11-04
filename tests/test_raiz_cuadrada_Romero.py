from funciones.raiz_cuadrada_Romero import raiz_cuadrada

def test_raiz_cuadrada_Romero():
    assert raiz_cuadrada(9) == 3
    assert raiz_cuadrada(-4) is None