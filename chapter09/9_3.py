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

user = User("ryota", "nakatsuka", 24, "Osaka")
user.describe_user()
user.greet_user()

user = User("coco", "nakatsuka", 11, "Osaka")
user.describe_user()
user.greet_user()