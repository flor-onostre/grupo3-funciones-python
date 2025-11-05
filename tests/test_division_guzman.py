from funciones.division_guzman import division_guzman

def test_dividir():
 assert division_guzman(10, 2) == 5
 assert division_guzman(5, 0) is None