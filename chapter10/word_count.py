from pathlib import Path

def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"ファイル{path}には約{num_words}の単語が含まれます。")

path = Path("alice.txt")
count_words(path)

filenames = ["alice.txt", "siddhartha.txt", "moby_dick.txt",
            "little_women.txt"]
for filename in filenames:
    path = Path(filename)
    count_words(path)
    
