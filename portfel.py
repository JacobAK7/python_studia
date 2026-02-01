class Portfel:
    def __init__(self):
        self.saldo:int = 0

    def wplata(self, kwota:int)->int:
        if kwota <= 0:
            raise ValueError("Wplata musi być większa od zera")
        self.saldo += kwota

    def stan(self)->int:
        return self.saldo
