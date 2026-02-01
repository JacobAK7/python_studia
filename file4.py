#wzrost >140 and >=18 or zgoda = true
height = input("Czy masz ponad 1.40 metrów wzrostu? ") #tak
age = input("Masz skończone 18lat? ") #tak
zgoda = input("Czy masz zgode rodziców? ")#tak

if height.lower() == 'tak' and(age.lower() == 'tak' or zgoda.lower() == 'tak'):
    message = "Możesz wejść!"
else:
    message = "Nie możesz wejść!"

print(message)
