contacts = dict()

while True:
    message = input("----------\nPodaj komende: \n[dodaj kontakt]\n[usun kontakt]\n[wyswietl wszystkie]\n[wyswietl kontakt]\n: ")
    if (message.lower() == "dodaj kontakt" or message.lower() == "1"):
        newUsr = input("Podaj jego imie i numer\n:")
        newUsrData = newUsr.split(" ")
        contacts[f'{newUsrData[0]}'] = f'{newUsrData[1]}'
        print(f' Dodano kontakt {newUsrData[0]}!')
        continue
    elif (message.lower() == "wyswietl wszystkie " or message.lower() == "3" ):
        for key, item in sorted(contacts.items()):
            print(f'{key} - {contacts[key]}')
        continue
    elif (message.lower() == "wyswietl kontakt" or message.lower() == "4"):
        oneCont = input("Wprowadz imie kontaktu\n: ")
        print(f'Numer do {oneCont} to: {contacts[oneCont]}')
        continue
    elif (message.lower() == "usun kontakt" or message.lower() == "2"):
        oneCont = input("Wprowadz imie kontaktu do usuniecia\n: ")
        contacts.pop(oneCont)
        print(f' Usunieto kontakt {newUsrData[0]}!')
        continue
    else:
        print("błędna komenda!")
        continue