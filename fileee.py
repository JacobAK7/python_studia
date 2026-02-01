import math
print("Start\n")


def imie(name):
    print(f'Witaj {name}')
def dodaj(a, b):
    suma = int(a) + int(b)
    return suma
def raport(imie, stanowisko = "domyślna", miasto = "Domyślna"):
    """
        wyswietla imie, stanowisko i miasto.

        Args:
            imie (string): imie pracownika.
            stanowisko (string): stanowisko pracownika default = "domyslna,
            miasto (string): miasto pracownika default = "domyslne"

        Returns:
            str: wiadomosc ze wszystkimi danymi
        """
    message = f'Imie: {imie}\nStanowisko: {stanowisko}\nMiasto: {miasto}\n----------------'
    return message
def licz_pole(figura, a=0, b=0, h=0, r=0):
    a = int(a)
    b = int(b)
    h = int(h)
    r = int(r)
    figura = figura.lower()
    if figura == "kwadrat":
        wynik = a * a
    elif figura == "trojkat":
        wynik = 0.5 * a * h
    elif figura == "prostokat":
        wynik = a * b
    elif figura == "kolo":
        wynik = math.pi ** r
    else:
        wynik = "Bledna figura!!!!"
    return wynik
def rozdziel(fullName):
    nameArr = fullName.split(" ")
    imie = nameArr[0]
    nazwisko = nameArr[1]
    return imie, nazwisko
# co_liczymy = input("Podaj figure: ").lower()
# co_liczymy = str(co_liczymy)
#
#
# if co_liczymy == "kwadrat":
#     a = input("Podaj bok: ")
#     print(licz_pole(figura = co_liczymy, a=int(a)))
# elif co_liczymy == "trojkat" :
#     a = input("Podaj bok: ")
#     h = input("Podaj wysokosc: ")
#     print(licz_pole(figura=co_liczymy, a=int(a), h=int(h)))
# elif co_liczymy == "kolo":
#     r = input("Podaj r: ")
#     print(licz_pole(figura=co_liczymy, r=int(r)))
# elif co_liczymy == "prostokat":
#     a = input("Podaj pierwszy bok: ")
#     b = input("Podaj drugi bok: ")
#     print(licz_pole(figura=co_liczymy, a=int(a), b=int(b)))
def function4(*liczby):
    suma = sum(liczby)
    return suma
def my_function(**myvar):
    if len(myvar) == 0:
        print("Empty :(")
    else:
        for x in myvar:
            print(x.capitalize(),":" , myvar[x])
# print(raport(imie = "janusz", stanowisko="menager", miasto="Warszawa"))
# print(raport(imie="Mikolaj", stanowisko="Programista"))
# print(raport(imie="Bartek", miasto="Gdansk"))

# hhh = input("Podaj swoje imie i nazwisko: ")
#
# print("Imie to: ", rozdziel(hhh)[0])
# print("Nazwisko to: ", rozdziel(hhh)[1])

# print(function4(1, 2, 3, 4, 5, 6, 7, 221, 567, 54))
# print(function4(1, 2, 3))

# my_function(name = "Jakub", age = 19, city = "Krakow")
# my_function()
def odejmij(a, b):
    roznica = int(a) - int(b)
    return roznica

def operacja(a, b, operacja):
     print(f'funkcja to {operacja.__name__}')
     return operacja(a,b)

print(operacja(5, 3, dodaj))
print(operacja(5, 3, odejmij))


print("\nKoniec")