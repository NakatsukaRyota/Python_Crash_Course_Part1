ryota = {
    "last_name": "Nakatsuka",
    "first_name": "Ryota",
    "age": 24,
    "city": "Osaka"
    }

yako = {
    "last_name": "Nakatsuka",
    "first_name": "yako",
    "age": 14,
    "city": "Osaka"
}

coco = {
    "last_name": "Nakatsuka",
    "first_name": "coco",
    "age": 11,
    "city": "Osaka"
}

people = [ryota, yako, coco]

for person in people:
    print("\n")
    print(person["last_name"])
    print(person["first_name"])
    print(person["age"])
    print(person["city"])
    
    