def make_car(maker, model, **car_info):
    car_info["maker"] = maker
    car_info["model"] = model
    return car_info

car = make_car("スバル", "レガシィ", color="ブルー", recorder=True)

print(car)

