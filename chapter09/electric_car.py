from car import Car

class Battery:

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"この車のバッテリーは{self.battery_size}-kwhです。")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"この車の満充電時の航続距離は約{range}マイルです。")

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()