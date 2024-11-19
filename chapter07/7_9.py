sandwich_orders = ['パストラミ', '野菜', 'ハム', 'パストラミ',
                    '玉子', 'ツナ', 'パストラミ']
finished_sandwiches = []

print("すみません。今日はパストラミは売り切れです。")

while "パストラミ" in sandwich_orders:
    sandwich_orders.remove("パストラミ")


while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"{sandwich}ができました。")

    finished_sandwiches.append(sandwich)

print("\n出来上がったサンドイッチ:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()}")