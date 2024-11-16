favorite_pizzas = ['マルゲリータ', 'クアトロ・フォルマッジ', 'マリナーラ']

# ピザの名前を出力する
for pizza in favorite_pizzas:
    print(pizza)

friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("ビスマルク")
friend_pizzas.append("ハニー")

print("私の好きなピザ")
for pizza in favorite_pizzas:
    print(pizza)

print("\n友だちが好きなピザ")
for pizza in friend_pizzas:
    print(pizza)