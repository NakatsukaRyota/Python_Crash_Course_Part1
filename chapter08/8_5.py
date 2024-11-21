def describe_city(city, country="Japan"):
    print(f"{city.title()}は{country.title()}にあります。")

describe_city("Osaka")
describe_city("Hokkaido")
describe_city("Paris", "France")