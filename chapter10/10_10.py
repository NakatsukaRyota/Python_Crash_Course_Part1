from pathlib import Path

def count_the(path):
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        num_the = contents.lower().count("the")
        print(f"\n'the'の数は{num_the}です。")

def count_the_exactly(path):
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        num_the = contents.lower().count("the ")
        print(f"\n'the'の正確な数は{num_the}です。")


path = Path("alice.txt")
count_the(path)
count_the_exactly(path)