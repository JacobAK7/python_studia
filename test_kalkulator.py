import pytest
from kalkulator import dodaj, dziel, srednia

# def test_dodawania_liczb_dodatnich():
#     assert dodaj(2, 3) == 5
#
# def test_dodawania_liczb_ujemnych():
#     assert dodaj(-2, -3) == -5

#=====================================================

def test_dzielenia_przez_zero_powinno_rzucic_blad():
    with pytest.raises(ValueError):
        dziel(10, 0)

def test_poprawnego_dzielenia():
    assert dziel(10, 2) == 5

#======================================================

# @pytest.mark.parametrize("a, b, wynik",[
#                              (2,3,5),
#                              (3,3,6),
#                              (-1,-1,-2),
#                              (200,0,200),
# ])
#
# def test_dodaj_wiele(a,b,wynik):
#     assert dodaj(a,b) == wynik



def test_srednia():
    assert srednia([1,2,3]) == 2.0

def test2_srednia():
    assert srednia([]) == None