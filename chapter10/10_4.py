from pathlib import Path

guests = input("あなたの名前を教えて下さい: ")

path = Path("guests.txt")
path.write_text(guests)