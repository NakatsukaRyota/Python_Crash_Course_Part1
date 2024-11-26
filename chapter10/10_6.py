print("数を2つ教えて下さい。割り算します。")
print("終了するには'q'を入力してください。")

while True:
    first_number = input("\n1番目の数: ")
    if first_number == 'q':
        break
    second_number = input("\n2番目の数: ")
    if second_number == 'q':
        break
    try:
        first_number = int(first_number)
        second_number = int(second_number)
    except ValueError:
        print("数字を入力してください。")
    else:
        answer = first_number + second_number
        print(f"\n答えは{answer}です。")