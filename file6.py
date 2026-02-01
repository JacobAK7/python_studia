data: str = input("Podaj zdanie/słowo ")
count: int = 0
samogloski = ['A','I','O','U','E']
for x in data:
    if x.upper() in samogloski:
        count += 1
    print(x.upper())
print("liczba samogłosek: ", count)