pets = []

dog = {
    "name": "dog",
    "type": "mammalian"
}
pets.append(dog)

cat = {
    "name": "cat",
    "type": "mammalian"
}
pets.append(cat)

lizard = {
    "name": "lizard",
    "type": "reptiles"
}
pets.append(lizard)

for pet in pets:
    print("\n")
    print(pet["name"])
    print(pet["type"])
    print("{pet['name']}は{pet['type']}です。")
