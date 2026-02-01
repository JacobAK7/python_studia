points = input("Podaj ilość zdobytyc punktów ")
points = int(points)

if points >= 0 and points <= 100:
    if points <= 50:
        ocena = '2'
    elif points <=60:
        ocena = '3'
    elif points <=70:
        ocena = '3.5'
    elif points <=80:
        ocena = '4'
    elif points <=90:
        ocena = '4.5'
    elif points >90:
        ocena = '5'
    else:
        ocena = "błąd!"
    print("twoja ocena to: ", ocena)
else:
    print("błędne dane!")