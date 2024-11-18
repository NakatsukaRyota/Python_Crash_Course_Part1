favorite_places = {
    "ryta": ["Osaka", "Hokkaido", "Nagoya"],
    "coco": ["Home", "park"],
    "reo": ["Home", "park"]
}

for name, places in favorite_places.items():
    print("\n")
    print(f"{name.title()}の好きな場所")
    for place in places:
        print(f"\t{place.title()}")
