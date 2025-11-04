from funciones.division_guzman import division # type: ignore

def test_division_normal():
   
    assert division(10, 5) == 2.0
  
    assert division(7, 2) == 3.5

def test_division_por_cero():
  
    assert division(10, 0) is None

def test_division_con_negativos():
   
    assert division(-10, 2) == -5.0