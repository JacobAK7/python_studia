while True:
    message = input("Podaj komende ")
    if message.lower().startswith("#"):
        print("krzyżyk")
        continue
    elif message.lower() == 'koniec':
        print("oficjalny koniec programu :)")
        break
    else:
        print(message)