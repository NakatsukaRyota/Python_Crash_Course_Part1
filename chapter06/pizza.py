pizza = {
    "crust": "レギュラー",
    "toppings": ["マッシュルーム", "エクストラチーズ"]
}

print(f"あなたが注文したのは{pizza['crust']}生地のピザで、"
    "トッピングは以下のとおりです。")

for topping in pizza["toppings"]:
    print(f"\t{topping}")
