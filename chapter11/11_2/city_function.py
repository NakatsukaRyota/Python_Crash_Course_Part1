def city_country(city, country, population=""):
    if population:
        message = f"{city.title()}, {country.title()} - 人口 {population}"
    else:
        message = f"{city.title()}, {country.title()}"
    return message