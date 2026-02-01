from datetime import datetime

def oblicz_wiek_z_pliku(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r') as file:
            zawartosc = file.read().strip()

        rok_urodzenia = int(zawartosc)

        aktualny_rok = datetime.now().year

        wiek = aktualny_rok - rok_urodzenia

        if wiek < 0:
            return "Błąd: Wiek mniejszy od zera."

        return wiek

    except FileNotFoundError:
        return "Błąd: Plik nie został znaleziony."

    except ValueError:
        return "Błąd: Plik zawiera niepoprawne dane."

    except Exception as e:
        return f"Wystąpił nieoczekiwany błąd: {e}"


print(oblicz_wiek_z_pliku("urodziny.txt"))
