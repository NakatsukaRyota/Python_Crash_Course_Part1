def make_album(arthist, title, number=0):

    album = {"arthist": arthist, 
            "title": title,
    }
    if number:
        album["number"] = number

    return album


while True:
    print("\nアルバムの情報を入力してください。")
    print("('q'で終了します。)")

    arthist = input("アーティスト名を入力してください。")
    if arthist == "q":
        break
    title = input("タイトルを入力してください。")
    if title == "q":
        break
    number = input("曲数を入力してください。")
    if number == "q":
        break

    album = make_album(arthist, title, number)
    print(album)

