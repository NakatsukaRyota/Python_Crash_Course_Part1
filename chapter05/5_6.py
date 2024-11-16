age = 24

if age < 2:
    person = "赤ちゃん"
elif age < 4:
    person = "幼児"
elif age < 13:
    person = "子ども"
elif age < 20:
    person = "ティーンエイジャー"
elif age < 65:
    person = "大人"
else:
    person = "高齢者"

print(f"あなたは{person}です。")