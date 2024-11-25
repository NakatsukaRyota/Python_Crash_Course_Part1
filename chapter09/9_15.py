import random

list = ["a", "b", "c", "d", "e", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

my_ticket = [2, "b", 5, 0]
count = 0

while True:
    nums = random.sample(list, 4)
    print(f"\n当選番号は{nums}です。")

    if my_ticket == nums:
        print("\n当選しました！おめでとうございます！")
        print(f"{count}回繰り返しました。")
        break
    count += 1
