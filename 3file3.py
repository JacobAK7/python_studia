import time

class MiernikCzasu:
    def __init__(self):
        self.start = None
        self.koniec = None
        self.czas = None

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, typ_bledu, wart_bledu, traceback):
        self.koniec = time.perf_counter()
        self.czas = self.koniec - self.start

        return False


with MiernikCzasu() as m:
    suma = 0
    for i in range(4_000_000):
        suma += i

print(f"Czas wykonania: {m.czas:.4f} sekundy")


try:
    with MiernikCzasu() as m:
        print("Zaraz wywołam błąd...")
        time.sleep(5)
        raise ValueError("Test błędu")
except:
    print(f"Czas do momentu błędu: {m.czas:.4f} sekundy")
