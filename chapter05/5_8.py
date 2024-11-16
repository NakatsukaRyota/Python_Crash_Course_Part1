users = ["yako", "ryo", "admin", "coco", "reo"]

for user in users:
    if user == "admin":
        print(f"こんにちは{user}、状況のレポートを見ますか？")
    else:
        print(f"こんにちは{user}、またログインしてくれてありがとう。")