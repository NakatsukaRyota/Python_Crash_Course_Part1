from User import User

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