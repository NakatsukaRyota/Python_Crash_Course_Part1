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

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type="アイスクリーム"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def get_flavors(self):
        print(f"\n以下のフレーバーが提供できます。")
        for flavor in self.flavors:
            print(f"-{flavor.title()}")

my_ice = IceCreamStand("31アイスクリーム")
my_ice.flavors = ["バニラ", "抹茶", "ポッピングシャワー", "オレンジ"]
my_ice.get_flavors()