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
    
my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriprive_name())

my_new_car.update_odometer(23_500)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()