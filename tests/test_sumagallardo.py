from funciones.sumagallardo import sumagallardo

def test_sumagallardo_basico():
    assert sumagallardo(3, 5) == 8
    assert sumagallardo(-2, 2) == 0
    assert sumagallardo(1.5, 2.5) == 4.0

def test_sumagallardo_tipado():
    assert isinstance(sumagallardo(1, 2), (int, float))
    assert isinstance(sumagallardo(1.2, 3.4), float)

