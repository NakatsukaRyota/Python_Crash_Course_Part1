num = input("数字を入力してください: ")
num = int(num)

if num % 10 == 0:
    print(f"{num}は10の倍数です。")
else:
    print(f"{num}は10の倍数ではないです。")
    