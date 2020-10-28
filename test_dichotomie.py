import dichotomie


def test_dichotomie() -> None:
    '''teste la fonction dichotomie'''
    tableau = [1, 2, 3]
    assert dichotomie.dichotomie(tableau, 1)
    assert dichotomie.dichotomie(tableau, 2)
    assert dichotomie.dichotomie(tableau, 3)
    assert not dichotomie.dichotomie(tableau, 4)
    assert not dichotomie.dichotomie(tableau, 0)
