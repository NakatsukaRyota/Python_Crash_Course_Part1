from pathlib import Path
import json

path = Path("your_favorite_number.json")
contents = path.read_text()
favorite_number = json.loads(contents)

print(f"あなたの好きな数字は{favorite_number}ですね！")