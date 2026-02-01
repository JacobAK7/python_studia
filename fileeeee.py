from time import time


def raport(**slownik):
    for x in slownik:
        print(x,":" ,slownik[x])

data = {
    "imie" : "Jan",
    "stanowisko" : "Programista",
    "miasto" : "Krakow"
}

dane = {
    "adres" : "123@wp.pl",
    "tytul" : "test123",
    "tresc" : "abcdefghijklmnoprst",
    "from" : ""
}

#raport(**data)

def wyslij_email(email, tekst, *, wazne=False, tytul = "Brak tytulu"):
    print("Wysylasz maila na mail: ", email)
    if (wazne == True):
        print("Wiadomosc umieszczona w folderze wazne!")
    print(f'Tresc maila: \n{tytul}\n\n{tekst}')

# wyslij_email("abc@wp.pl", "qwertyuioplkjhgfdsa", wazne = True, tytul = "Test123")

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def changelower(func):
    def myinner2():
        return func().lower()
    return myinner2

@changecase
def myfunction():
  return "Hello Sally"

@changelower
def otherfunction():
  return "I AM Speed!"

def changecase2(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase2
def myfunction2(nam):
  return "Hello " + nam


def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Wykonano funkcje: {func.__name__} w czasie: {(t2-t1):.4f}s')
        return result
    return wrap_func


@timer_func
def long_time(n):
    for i in range(n):
        for j in range(100000):
            i*j


def myGen():
    yield 1
    yield 2
    yield 3

def fibonaci():
  a, b = 1, 1
  while True:
    yield a
    a, b = b, a + b

x = lambda a, b : a*b

#print(x(5,6))

y = iter(["apple", "banana", "mackow"])
# print(next(y))
# print(next(y))
# print(next(y))

def myfunc8(n):
  return len(n)

z = map(myfunc8, ('apple', 'banana', 'mackoooow'))
# print(next(z))
# print(next(z))
# print(next(z))

# gen = fibonaci()
# for x in range(10):
#   print(next(gen))

imiona = ["jan", "jakub", "mikolaj", "bartek", "karol", "marek"]

# for x in range(len(imiona)):
#     cap = lambda tmp = imiona[x] : tmp.capitalize()
#     print(cap(imiona[x]))

arr = ["jan", True, 1, 4.5]

def datatype(n):
    if (isinstance(n, str)):
        return "String"
    elif (isinstance(n, int)):
        return "Int"
    else:
        return "Other type"

def dekorator(func):
    def wyinner(*args):
        for i in args:
            if (isinstance(i, str) == True):
                return "String"
            elif (isinstance(i, int) == True):
                return "Intiger"
            else:
                return "Other type"

for x in arr:
    print(datatype(x))