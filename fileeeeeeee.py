from narzedziaFirmowe import pomiar, formatowanie
from functools import reduce

lista = [
    {"nazwa": "Banany", "cena": 5},
    {"nazwa": "Pomarancze", "cena": 10},
    {"nazwa": "jablka", "cena": 7},
    {"nazwa": "gruszki", "cena": 3},
    {"nazwa": "ziemniaki", "cena": 25},
    {"nazwa": "pomidory", "cena": 15}
]

oceny = [
    {"imie": "Jan", "ocena": 3},
    {"imie": "Jakub", "ocena": 3},
    {"imie": "Mikolaj", "ocena": 4},
    {"imie": "Antek", "ocena": 5},
    {"imie": "Kasia", "ocena": 2},
    {"imie": "Marek", "ocena": 4}
]


a = [1, 2, 3, 4, 5, 7]

sortedList = sorted(lista, key=lambda s : s["cena"])


def eleganckaLista():
    for x in range(len(sortedList)):
        print(sortedList[x]["nazwa"], ":", sortedList[x]["cena"])

def czyZdaliWszyscy():
    zdali = True
    for x in range(len(oceny)):
        if (oceny[x]["ocena"] < 3):
            zdali = False
            break
        else:
            continue
    return zdali


@pomiar.timer_func
def long_time(n):
    for i in range(n):
        for j in range(100000):
            i*j

@formatowanie.changecase
def myTextFunc():
    text = "mikolaj mackow"
    return text

def add(x, y):
    return x + y

# long_time(1000)
# print(myTextFunc())

#print(czyZdaliWszyscy())
# print("Suma zbioru A: ",reduce(lambda x, y: x+y, a))
# print("Najwieksza liczba ze zbioru A: ",reduce(lambda x, y: x if x>y else y ,a))

#from enum import Enum
# class HealthStatus(Enum):
#     HOME = "HOME"
#     DOCTOR = "DOCTOR"
#     HOSPITAL = "HOSPITAL"