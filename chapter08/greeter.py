def get_formatted(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nあなたの名前を教えて下さい。")
    print(" ('q'を入力すると終了します) ")
    l_name = input("姓を入力してください: ")
    if l_name == "q":
        break

    f_name = input("名を入力してください: ")
    if f_name == "q": 
        break

    formatted_name = get_formatted(f_name, l_name)
    print(f"\nこんにちは{formatted_name}!")

    