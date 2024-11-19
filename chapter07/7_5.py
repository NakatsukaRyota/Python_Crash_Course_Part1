prompt = "あなたの年齢を教えて下さい。料金をお伝えします。"
prompt += "\n終了するには'終了'と入力してください。"

age = ""
while True:
    age = input(prompt)

    if age != "終了":
        age = int(age)
    else:
        break

    if age < 3:
        print(f"{age}歳なので、無料です。")
    elif age <= 12:
        print(f"{age}歳なので、1000円です。")
    else:
        print(f"{age}歳なので、1500円です。")

    