from pathlib import Path

print("--- ファイル全体を読み込みます:")
path = Path('learning_python.txt')
contents = path.read_text(encoding="utf-8")

print("\n--- 各行をループします:")
lines = contents.replace("Python", "Golang").splitlines()
for line in lines:
    print(line)