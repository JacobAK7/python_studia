mikolaj = ["Ala", "Kot", "Bartek", "Marek"]
kuba = ["Bartek", "Karol", "Marek"]

mikolajSet = set(sorted(mikolaj))
kubaSet = set(sorted(kuba))

for i in kubaSet.intersection(mikolajSet):
    print(i)