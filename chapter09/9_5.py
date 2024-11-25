class User:
    def __init__(self, first_name, last_name, age, place):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.place = place
        self.login_attempts = 0


    def describe_user(self):
        print(f"\nユーザーの情報")
        print(f"-性:{self.last_name}")
        print(f"-名:{self.first_name}")
        print(f"-年齢:{self.age}")
        print(f"-場所:{self.place}")

    def greet_user(self):
        name = f"{self.first_name} {self.last_name}"
        print(f"\nこんにちは、{name.title()}さん！")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
    
user = User("ryota", "nakatsuka", 24, "Osaka")
user.increment_login_attempts()
print(user.login_attempts)
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)

user.reset_login_attempts()
print(user.login_attempts)

