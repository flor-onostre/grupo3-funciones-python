import math

def raiz_cuadrada_Romero(x):
    """Devuelve la raíz cuadrada de un número no negativo.
    Si x es negativo, devuelve None."""
    if x < 0:
        return None
    return math.sqrt(x)