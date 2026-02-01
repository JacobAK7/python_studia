thisdict = {
    "name": "Jakub",
    "surname": "Płaszczyk",
    "age": 19,
    "city": "Kraków"
}

thisdict["test"] = "test1"
thisdict.update({"city": "Wolbrom"})

for x in thisdict:
    print(f'{x} : {thisdict[x]}')