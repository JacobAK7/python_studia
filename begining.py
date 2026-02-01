wiek = input("Podaj swój wiek ")

wiek = int(wiek)

if wiek >= 18:
    message = 'pełnoletni'
elif wiek <= 18 and wiek > 0:
    message = 'niepełnoletni'
else:
    message = 'błędne dane!'

print(message)
