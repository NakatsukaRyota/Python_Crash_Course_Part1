prompt = "トッピングを指定してください: "
prompt += "\n終了するには'終了'と入力してください "

message = ""

while message != "終了":
    message = input(prompt)
    if message != "終了":
        print(f"{message}をトッピングに追加しました。")
    else:
        break

