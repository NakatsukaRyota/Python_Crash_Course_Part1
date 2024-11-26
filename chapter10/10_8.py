from pathlib import Path

path_cat = Path("cats.txt")
path_dog = Path("dogs.txt")

try:
    contents_cat = path_cat.read_text(encoding='utf-8')
    contents_dog = path_dog.read_text(encoding='utf-8')
except FileNotFoundError:
    print("ファイルが見つかりません。")
else:
    print("\nネコの名前")
    for line in contents_cat.splitlines():
        print(f"-{line}")
    
    print("\nイヌの名前")
    for line in contents_dog.splitlines():
        print(f"-{line}")