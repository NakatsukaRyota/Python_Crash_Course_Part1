class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"\nレストランの情報")
        print(f"レストラン名: {self.restaurant_name.title()}")
        print(f"レストランの種類: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\nレストラン:{self.restaurant_name.title()}がオープンしました。")

    def set_number_served(self, num):
        if num >= 0:
            self.number_served = num
        else:
            print("0以上の値を指定してください。")

    def increment_number_served(self, num):
        self.number_served += num

restaurant = Restaurant("すーさんのインドカレー", "インドカレー")

print(restaurant.number_served)
restaurant.number_served = 100
print(restaurant.number_served)

restaurant.set_number_served(200)
print(restaurant.number_served)

restaurant.increment_number_served(100)
print(restaurant.number_served)