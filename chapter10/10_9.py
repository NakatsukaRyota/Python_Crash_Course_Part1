from pathlib import Path

path_cat = Path("cats.txt")
path_dog = Path("dogs.txt")
path_list = [path_cat, path_dog]

for path in path_list:
    try:
        contents_cat = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        print("名前")
        for line in contents_cat.splitlines():
            print(f"-{line}")