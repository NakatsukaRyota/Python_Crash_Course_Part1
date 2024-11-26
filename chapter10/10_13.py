from pathlib import Path
import json

def get_stored_userinformation(path):
    if path.exists():
        contents = path.read_text()
        user_information = json.loads(contents)
        return user_information
    else:
        return None
    
def get_new_user_information(path):
    name = input("あなたの名前を教えて下さい: ")
    age = input("あなたの年齢を教えて下さい: ")
    place = input("あなたの住んでいる場所を教えて下さい: ")
    user_information = {"nane": name, "age": age, "place": place}
    contents = json.dumps(user_information)
    path.write_text(contents)
    return user_information

def greet_user():
    path = Path("user_information")
    user_information = get_stored_userinformation(path)
    if user_information:
        print(f"\nあなたの登録情報")
        for name, value in user_information.items():
            print(f"{name}: {value}")
    else:
        user_information = get_new_user_information(path)
        print("\n情報を登録しました。")

greet_user()
