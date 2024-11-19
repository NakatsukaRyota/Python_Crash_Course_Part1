sandwich_orders = ["tsuna", "mayo", "anko", "tamago"]

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"{sandwich}ができました。")

    finished_sandwiches.append(sandwich)

print("\n出来上がったサンドイッチ:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()}")