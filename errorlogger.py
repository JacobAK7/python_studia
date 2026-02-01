from datetime import datetime

class Logger:
    def __init__(self, sciezka):
        self.sciezka = sciezka
        self.file = None

    def log(self, wiadomosc: str):
        teraz = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        wpis = f"[{teraz}] {wiadomosc}\n"
        self.file.write(wpis)

    def __enter__(self):
        self.file = open(self.sciezka, "a", encoding="utf-8")
        return self

    def __exit__(self, typ_bledu, wart_bledu, traceback):
        if self.file:
            self.file.close()

        return False

def licz_bledy(nazwa_pliku_logu: str) -> int:
    licznik = 0
    try:
        with open(nazwa_pliku_logu, 'r', encoding='utf-8') as plik:
            for linia in plik:
                linia_upper = linia.strip().upper()
                if 'ERROR:' in linia_upper:
                    licznik += 1
        return licznik

    except FileNotFoundError:
        print(f"Błąd: plik '{nazwa_pliku_logu}' nie został znaleziony.")
        return 0

    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")
        return 0


with Logger("logi.txt") as log:
    log.log("Working.")


try:
    with Logger("logi.txt") as log:
        x = 5 / 0  # błąd
except Exception as e:
    with Logger("logi.txt") as log:
        log.log(f"Error: {e}")



ile_errorow = licz_bledy("logi.txt")
print(f"Liczba błędów w logach: {ile_errorow}")
