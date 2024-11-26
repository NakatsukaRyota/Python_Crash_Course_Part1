from pathlib import Path

path = Path("guest_book.txt")
text = ""
while True:
    name = input("あなたの名前を教えて下さい('q'でやめる): ")
    if name == 'q':
        path.write_text(text)
        break
    else:
        text += name
        text += "\n"
