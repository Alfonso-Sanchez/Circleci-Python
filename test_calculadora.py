import operaciones


def test_pruebas():
    assert operaciones.suma(3, 3) == 6
    assert operaciones.resta(2, 1) == 1
    assert operaciones.multi(3, 4) == 12
    assert operaciones.div(10, 5) == 2
    assert operaciones.raiz(25) == 5
    assert operaciones.factorial(5) == 120
