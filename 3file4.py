def podmien_imie(sciezka, nowe_imie):
    with open(sciezka, "r+", encoding="utf-8") as plik:
        zawartosc = plik.readline()
        nowa_tresc = zawartosc.replace("[IMIE]", nowe_imie)
        plik.seek(0)
        plik.write(nowa_tresc)

def podmien_imie_bezpiecznie(sciezka, nowe_imie):
    with open(sciezka, "r+") as plik:
        zawartosc = plik.readline()
        nowa_tresc = zawartosc.replace("[IMIE]", nowe_imie)
        plik.seek(0)
        plik.write(nowa_tresc)
        plik.truncate()

with open("szablon.txt", "w") as f:
    f.write("Witaj, [IMIE]!")

print("=== Zła wersja ===")
podmien_imie("szablon.txt", "Anna")        # krótsze
print(open("szablon.txt").read())

with open("szablon.txt", "w") as f:
    f.write("Witaj, [IMIE]!")

podmien_imie("szablon.txt", "Krzysztof")   # dłuższe
print(open("szablon.txt").read())


print("\n=== Poprawna wersja ===")
with open("szablon.txt", "w") as f:
    f.write("Witaj, [IMIE]!")

podmien_imie_bezpiecznie("szablon.txt", "Anna")
print(open("szablon.txt").read())

with open("szablon.txt", "w") as f:
    f.write("Witaj, [IMIE]!")

podmien_imie_bezpiecznie("szablon.txt", "Krzysztof")
print(open("szablon.txt").read())
