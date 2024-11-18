cities = {
    "Osaka": {
        "country": "Japan",
        "population": 275,
        "fact": "Takoyaki"
        },
    
    "Paris": {
        "country": "France",
        "population": 210,
        "fact": " Baguette"
    },

    "Los Angels": {
        "country": "U.S.A",
        "population": 382,
        "fact" : "Hollywood" 
    }
}

for name, info in cities.items():
    print("\n")
    print(f"{name.title()}の情報はこちら")
    print(f"\t国:{info['country']}")
    print(f"\t人口:{info['population']}")
    print(f"\t特徴:{info['fact']}")