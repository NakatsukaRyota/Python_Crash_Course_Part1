class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriprive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"走行距離は{self.odometer_reading}マイルです。")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("走行距離は減らせません。")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("この機能は電気自動車にはありません。")

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

    def fill_gas_tank(self):
        print("この自動車にはガゾリンのタンクはありません。")


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriprive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()