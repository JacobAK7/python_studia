zakupy = []

while True:
    message = input("Podaj produkt do listy zakupów lub zakończ ")
    if (message.lower() != "koniec" ):
        zakupy.append(message.lower())
        continue
    else:
        zakupy.sort()
        # print("lista zakupów: ", zakupy)
        print(f'Liczba produktów na liście: {len(zakupy)}')
        print("Lista zakupów:")
        # for i in range(len(zakupy)):
        #     # print(i+1, ".", zakupy[i])
        #     print(f'{i + 1}. {zakupy[i]}')
        for x, name in enumerate(zakupy):
            print(f'{x+1}. {name.capitalize()}')
        break