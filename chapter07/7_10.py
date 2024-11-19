dream_vacation = {}

active = True

while True:
    name = input("あなたのお名前は？")
    response = input("\n世界中どこでも好きなところに行けるとしたらどこに行きたいですか？ ")

    dream_vacation["name"] = response

    repeat = input("\n誰か他に回答してくれる人いますか？(yes/no) ")
    if repeat != "yes":
        break


print("\n---投票結果---")
for name, vacation in dream_vacation.items():
    print(f"{name.title()}さんが行きたいところは{vacation.title()}です。")

