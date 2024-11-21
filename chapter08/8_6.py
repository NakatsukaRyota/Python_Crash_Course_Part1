def city_country(city, country):
    message = f"{city.title()}, {country.title()}"
    return message

message = city_country("Osaka", "Japan")
print(message)

message = city_country("Paris", "France")
print(message)

message = city_country("London", "U.K.")
print(message)