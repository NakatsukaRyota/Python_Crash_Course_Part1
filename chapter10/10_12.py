from pathlib import Path
import json


path = Path("your_favorite_number.json")
if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"あなたの好きな数字は{favorite_number}ですね！")
else:
    favorite_number = input("あなたの好きな数字を教えて下さい: ")
    path = Path("your_favorite_number.json")
    contents = json.dumps(favorite_number)
    path.write_text(favorite_number)
    print("ありがとうございます。記憶しておきます！")