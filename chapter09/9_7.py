class User:
    def __init__(self, first_name, last_name, age, place):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.place = place 

    def describe_user(self):
        print(f"\nユーザーの情報")
        print(f"-性:{self.last_name}")
        print(f"-名:{self.first_name}")
        print(f"-年齢:{self.age}")
        print(f"-場所:{self.place}")

    def greet_user(self):
        name = f"{self.first_name} {self.last_name}"
        print(f"\nこんにちは、{name.title()}さん！")


class Admin(User):
    def __init__(self, first_name, last_name, age, place):
        super().__init__(first_name, last_name, age, place)
        self.privileges = ["投稿を追加する",
                            "投稿を削除する",
                            "ユーザーを利用禁止にする"]

    def show_privileges(self):
        print("\n管理者には以下の権限が与えられています。")
        for privilege in self.privileges:
            print(f"-{privilege}")


admin = Admin("ryota", "nakatsuka", 24, "Osaka")
admin.show_privileges()