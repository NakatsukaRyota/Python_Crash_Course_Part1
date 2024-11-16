my_foods = ["ピザ", "だんご", "ケーキ"]
friend_foods = my_foods[:]

my_foods.append("チョコレート")
friend_foods.append("アイスクリーム")


print("私が好きな食べもの")
for food in my_foods:
    print(food)

print("\n友だちが好きな食べ物")
for food in friend_foods:
    print(food)

