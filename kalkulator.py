from mypy.util import Sized


def dodaj(a:int, b:int)->int:
    return a + b

def dziel(a:int, b:int)->float:
    if b == 0:
        raise ValueError("Nie można dzielić przez zero!")
    return a/b

def srednia(liczby:list[float])->float | None:
    if liczby == []:
        return None
    else:
        return sum(liczby)/len(liczby)