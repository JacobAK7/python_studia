import os

class BezpiecznyZapis:
    def __init__(self, sciezka):
        self.sciezka_docelowa = sciezka
        self.sciezka_tymczasowa = sciezka + ".tmp"
        self.file = None

    def __enter__(self):
        self.file = open(self.sciezka_tymczasowa, "w")
        return self.file

    def __exit__(self, typ_bledu, wart_bledu, traceback):
        if self.file:
            self.file.close()

        if typ_bledu is None:
            if os.path.exists(self.sciezka_docelowa):
                os.remove(self.sciezka_docelowa)

            os.rename(self.sciezka_tymczasowa, self.sciezka_docelowa)

        else:
            if os.path.exists(self.sciezka_tymczasowa):
                os.remove(self.sciezka_tymczasowa)

        return False

with open("konfiguracja.txt", "w") as f:
    f.write("stare dane")

with BezpiecznyZapis("konfiguracja.txt") as f:
    f.write("NOWE DANE")


try:
    with BezpiecznyZapis("konfiguracja.txt") as f:
        f.write("ZAPIS KTÓRY SIĘ NIE UDA")
        raise ValueError("Symulacja błędu")
except:
    print("Błąd wystąpił – plik docelowy został zachowany")

