def make_album(arthist, title, number=0):

    album = {"arthist": arthist, 
            "title": title,
    }
    if number:
        album["number"] = number

    return album

album = make_album("ryo", "Dynamite")
print(album)

album = make_album("coco", "Smart")
print(album)

album = make_album("reo", "Crazy", 10)
print(album)