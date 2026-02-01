from traceback import print_tb

pracownicy = [
    {"imie" : "ania", "stanowisko" : "specjalista", "pensja" : 2500},
    {"imie" : "tomek", "stanowisko" : "manager", "pensja" : 1500},
    {"imie" : "mikolaj", "stanowisko" : "junior", "pensja" : 1000},
    {"imie" : "jan", "stanowisko" : "specjalista", "pensja" : 3600}
]

srednia_pensja = 0
max = 0

for i in range(len(pracownicy)):
    srednia_pensja = srednia_pensja + pracownicy[i]["pensja"]
    #print(pracownicy[i]["pensja"])

srednia_pensja2 = srednia_pensja/len(pracownicy)
print("średnia pensja to: ", srednia_pensja2)

for j in range(len(pracownicy)):
    tmp = pracownicy[j]["pensja"]
    if max < tmp:
        max = tmp
    else:
        continue

print("max pensja: " ,max)

lista = []

for x in range(len(pracownicy)):
    if pracownicy[x]["stanowisko"] == "specjalista":
        lista.append(pracownicy[x]["imie"])
    else:
        continue

print(lista)