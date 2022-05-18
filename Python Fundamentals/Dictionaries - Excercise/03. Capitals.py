country_names = input().split(", ")
capital_names = input().split(", ")

result = dict(zip(country_names, capital_names))


for country, capital in result.items():
    print(f"{country} -> {capital}")
    