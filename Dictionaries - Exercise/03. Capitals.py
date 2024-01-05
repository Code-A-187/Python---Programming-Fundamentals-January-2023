# Input

countries = input().split(", ")
capitals = input().split(", ")

# Logic

capital_by_country = {countries[idx]: capitals[idx] for idx in range(len(countries))}

# capital_by_country = {}
# for idx in range(len(countries)):
#     country = countries[idx]
#     capital = capitals[idx]
#     capital_by_country[country] = capital

# Output

for country, capital in capital_by_country.items():
    print(f"{country} -> {capital}")
