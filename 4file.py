# class WlasnyIterRange:
#     def __init__(self, tmpRange):
#         self.tmpRange = tmpRange
#         self.curr = tmpRange.start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.curr >= self.tmpRange.stop:
#             raise StopIteration
#         value = self.curr
#         self.curr += 1
#         return value


# class myRange:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#
#     def __iter__(self):
#         return WlasnyIterRange(self)


# class myRange:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#
#     def __iter__(self):
#         biezaca_wartosc = self.start
#         while biezaca_wartosc < self.stop:
#             yield biezaca_wartosc
#             biezaca_wartosc+=1
#
# moj_zakres = myRange(10, 20)
# for l in moj_zakres:
#     print(l)


import csv
import itertools

def czytaj_duzy_csv(sciezka: str):
    with open(sciezka) as file:
        obj = csv.DictReader(file)
        for wiersz in obj:
            wiersz["wiek"] = int(wiersz["wiek"])
            yield wiersz


# osoby_po_40 = (os for os in czytaj_duzy_csv("dane.csv") if os["wiek"] > 40)
# opisy = (f'{os["imie"].upper()} {os["nazwisko"].upper()}' for os in osoby_po_40)

# osoby = (os for os in czytaj_duzy_csv("dane.csv"))
# osoby = sorted((os for os in czytaj_duzy_csv("dane.csv")), key=lambda x: x["nazwisko"])

# for i,j in itertools.groupby(osoby, key=lambda x: x["nazwisko"][0]):
#     print(list(j))

# iter_analiza1, iter_analiza2 = itertools.tee(czytaj_duzy_csv("dane.csv"))
#
# najdluzsze_imie_i_nazwisko = max(iter_analiza1, key=lambda x: len(f'{x["imie"] + x["nazwisko"]}'))
#
# print(najdluzsze_imie_i_nazwisko)
#
# ile_osob = 0
# laczny_wiek=0
# for x in iter_analiza2:
#     ile_osob +=1
#     laczny_wiek += x["wiek"]
#
# print(ile_osob, " x ", laczny_wiek)
# for x in osoby:
#     print(x["nazwisko"])


# a. ŹRÓDŁO – generator czytający plik linia po linii
# def czytaj_logi(sciezka):
#     with open(sciezka, "r", encoding="utf-8") as f:
#         for linia in f:
#             yield linia.strip()
#
#
# # b. FILTR – tylko błędy klienta (4xx)
# def tylko_4xx(linie):
#     for linia in linie:
#         parts = linia.split()
#         status = int(parts[-2])
#         if 400 <= status < 500:
#             yield linia
#
#
# # c. TRANSFORMACJA – (ip, rozmiar_w_bajtach)
# def parsuj(linie):
#     for linia in linie:
#         parts = linia.split()
#         ip = parts[0]
#         rozmiar = int(parts[-1])
#         yield ip, rozmiar
#
#
# # d + e. GRUPOWANIE I AGREGACJA (wymaga sortowania po IP)
# def agreguj_po_ip(dane):
#     # groupby wymaga danych posortowanych
#     dane = sorted(dane, key=lambda x: x[0])
#
#     for ip, grupa in itertools.groupby(dane, key=lambda x: x[0]):
#         suma = sum(rozmiar for _, rozmiar in grupa)
#         yield ip, suma
#
#
# # f. SORTOWANIE KOŃCOWE I TOP 3
# def top_3_ip_po_ruchu(sciezka):
#     potok = czytaj_logi(sciezka)
#     potok = tylko_4xx(potok)
#     potok = parsuj(potok)
#     potok = agreguj_po_ip(potok)
#
#     return sorted(potok, key=lambda x: x[1], reverse=True)[:3]
#
#
# # --- URUCHOMIENIE ---
# wynik = top_3_ip_po_ruchu("logs.txt")
#
# for ip, bajty in wynik:
#     print(ip, bajty)
#
#
# czytaj_duzy_csv("dane.csv")


def monitor_temperatury(prog_alarmowy):
    suma = 0
    licznik = 0
    srednia = 0
    try:
        while True:
            odczyt = yield srednia

            if odczyt is None:
                suma = 0
                licznik = 0
                srednia = 0
                print("Czujnik zresetowany")
            else:
                suma += odczyt
                licznik += 1
                srednia = suma / licznik

                if srednia > prog_alarmowy:
                    print(f"Średnia temperatura {srednia:.2f} przekroczyła próg {prog_alarmowy}")

    finally:
        print("Czujnik wyłączony")



gen = monitor_temperatury(prog_alarmowy=30)
print(next(gen))

print(gen.send(25))
print(gen.send(35))
print(gen.send(40))

print(gen.send(None))

print(gen.send(20))
print(gen.send(22))

gen.close()





