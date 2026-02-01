wiek = input("Podaj wiek ")

wiek = int(wiek)

if wiek > 0 and wiek < 200:
    if wiek < 13 :
        message = 'dziecko'
    elif wiek >= 13 and wiek < 18:
        message = 'niepełnoletni'
    elif wiek >= 18:
        message = 'pełnoletni'
else:
    message = 'błędne dane!'
print(message)