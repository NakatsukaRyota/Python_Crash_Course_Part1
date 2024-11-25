class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nレストランの情報")
        print(f"レストラン名: {self.restaurant_name.title()}")
        print(f"レストランの種類: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\nレストラン:{self.restaurant_name.title()}がオープンしました。")

restaurant = Restaurant("すーさんのインドカレー", "インドカレー")
restaurant.describe_restaurant()

restaurant = Restaurant("すき家", "牛丼")
restaurant.describe_restaurant()

restaurant = Restaurant("ポムの樹", "オムライス")
restaurant.describe_restaurant()