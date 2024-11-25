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

class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\n管理者には以下の権限が与えられています。")
        if self.privileges:
            for privilege in self.privileges:
                print(f"-{privilege}")
        else:
            print("ユーザーには権限がありません。")

    

class Admin(User):
    def __init__(self, first_name, last_name, age, place):
        super().__init__(first_name, last_name, age, place)
        self.privileges = Privileges()