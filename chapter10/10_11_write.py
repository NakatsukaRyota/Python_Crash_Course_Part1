from pathlib import Path
import json

favorite_number = input("あなたの好きな数字を教えて下さい: ")
path = Path("your_favorite_number.json")
contents = json.dumps(favorite_number)
path.write_text(favorite_number)

print("ありがとうございます。記憶しておきます！")