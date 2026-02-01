from dataclasses import dataclass
from functools import total_ordering
from traceback import print_tb


@dataclass
class PunktData:
    x: int
    y: int

class PunktLekki:
    __slots__ = ('x', 'y')   # tylko te dwa atrybuty są dozwolone

    def __init__(self, x, y):
        self.x = x
        self.y = y

class BrakPunktowZyciaError(Exception):
    def __init__(self, message):
        super().__init__(message)

class IteratorEkwipunku:
    def __init__(self, lista_przedmiotow):
        self.lista = lista_przedmiotow
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.lista):
            raise StopIteration
        element = self.lista[self.index]
        self.index += 1
        return element

class Ekwipunek:
    def __init__(self):
        self._przedmioty = {}

    def __len__(self):
        return len(self._przedmioty)

    def __setitem__(self, klucz, wartosc):
        self._przedmioty[klucz] = wartosc

    def __getitem__(self, klucz):
        return self._przedmioty[klucz]

    def __delitem__(self, klucz):
        del self._przedmioty[klucz]

    def __repr__(self):
        return f"Ekwipunek({self._przedmioty})"

    def __iter__(self):
        # Tworzymy iterator, przekazując listę wartości
        return IteratorEkwipunku(list(self._przedmioty.values()))

class Bron:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.dostepne_ulepszenia = []
    def dodaj_ulepszenie(self, ulepszenie):
        self.dostepne_ulepszenia.append(ulepszenie)
    def __repr__(self):
        return f"{self.nazwa} (ulepszenia: “f”{self.dostepne_ulepszenia})"

class Miecz(Bron): pass
class Topor(Bron): pass

@total_ordering
class Gracz:
    Gracze = 0

    def __init__(self, nick, hp):
        Gracz.Gracze += 1
        self.nick = nick
        self.__hp = hp
        self.Class = None
        self.Ekwipunek = Ekwipunek()

    def __str__(self):
        return f'\nNick: {self.nick}\nYour HP: {self.__hp}'

    def __repr__(self):
        return f'Gracz(nick=\'{self.nick}\', hp={self.__hp})'

    def __eq__(self, other):
        if isinstance(other, Gracz):
            return self.nick == other.nick
        return False

    def __lt__(self, other):
        if isinstance(other, Gracz):
            return self.__hp < other.__hp
        return False

    def hit(self, damage):
        self.__hp -= damage
        if self.__hp <= 0:
            return "\nYou are dead!"
        return f'\n{self.nick} has been hit!\ncurrent hp: {self.__hp}'

    def przedstaw_sie(self):
        return f'Jestem {self.Class}'

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if value >= 0:
            self.__hp = value

    @classmethod
    def stworz_berserkera(cls, nick):
        return cls(nick, 50)

class NieujemnaLiczba:
    def __set_name__(self, owner, name):
        self._nazwa_atrybutu = name

    def __get__(self, instance, value):
        return instance.__dict__.get(self._nazwa_atrybutu)

    def __set__(self, instance, value):
        if value < 0:
            instance.__dict__[self._nazwa_atrybutu] = 0
        else:
            instance.__dict__[self._nazwa_atrybutu] = value

class Warrior(Gracz):
    sila = NieujemnaLiczba()

    def __init__(self, nick, hp, sila_value):
        super().__init__(nick, hp)
        self.sila = sila_value
        self.Class = "Warrior"

    def __add__(self, other):
        new_name = self.nick + ' ' + other.nick
        new_sila = self.sila + other.sila
        new_hp = self.hp + other.hp
        new_warrior = Warrior(new_name, new_hp, new_sila)
        return new_warrior

    def calcDamage(self):
        return self.sila*1.5

    def atakuj(self):
        if self.hp <= 0:
            raise BrakPunktowZyciaError(f"Postać {self.nick} nie może atakować! Brak punktów życia.")
        else:
            print(f"{self.nick} atakuje z siłą {self.sila}!")

    def przedstaw_sie(self):
        return super().przedstaw_sie()

class Mage(Gracz):

    mana = NieujemnaLiczba()


    def __init__(self, nick, hp, mana_value):
        super().__init__(nick, hp)
        self.mana = mana_value
        self.Class = "Mage"

    def calcDamage(self):
        return self.mana*2

    def przedstaw_sie(self):
        return super().przedstaw_sie()

p = PunktLekki(1, 2)

#p.z = 3
#
#print(p.z)

#print(p.__dict__)

print(p.x)      # ✔ poprawnie wyświetla: 1
print(p.y)      # ✔ poprawnie wyświetla: 2

miecz = Miecz("Stalowy Miecz")
topor = Topor("Krasnoludzki Topór")
print(f"Przed modyfikacją: {miecz}, {topor}")
# Dodajemy ulepszenie TYLKO do miecza
miecz.dodaj_ulepszenie("Ostrzenie")
# Pytanie: Co zostanie wyświetlone poniżej?
print(f"Po modyfikacji: {miecz}, {topor}")
