message = input("Podaj tagi oddzielajac je przecinkami")

lista = message.split(",")

new_list = []

for j in range(len(lista)):
    new_list.append(lista[j].strip())

new_list.sort()

unique = set(new_list)

print("Wszystkie tagi posortowane: ")
for x in range(len(new_list)):
    print(f'{x+1}. #{new_list[x]}')

print("Unikalne tagi: ")
for i in sorted(unique):
    print(f'#{i}')
