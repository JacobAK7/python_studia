class IgnorujBledy:
    def __init__(self, ignorowane_bledy):
        self.ignorowane_bledy = ignorowane_bledy

    def __enter__(self):
        return self

    def __exit__(self, typ_bledu, wart_bledu, traceback):
        if typ_bledu in self.ignorowane_bledy:
            print(f"Ignoruję wyjątek: {typ_bledu.__name__}")
            return True
        return False

# import logging
# logging.basicConfig(level=logging.INFO, format='%(message)s')
# logger = logging.getLogger(__name__)


with IgnorujBledy((ZeroDivisionError, KeyError)):
    print(10 / 0)

print("Program kontynuuje działanie po bloku 'with'.")

with IgnorujBledy((KeyError,)):
    print([1, 2, 3][5])
