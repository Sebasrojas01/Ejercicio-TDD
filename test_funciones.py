from funciones import encontrar_numero_menor

def test_encontrar_numero_menor():
    assert encontrar_numero_menor([1,3,5,6,7]) == 1
    assert encontrar_numero_menor([3,7,2,7,4]) == 2
    assert encontrar_numero_menor([0,6,8,2,77]) == 0