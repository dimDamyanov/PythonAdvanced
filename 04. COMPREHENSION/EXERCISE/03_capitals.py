countries = input()
capitals = input()
country_capital_dict = {country: capital for country, capital in zip(countries.split(', '), capitals.split(', '))}
for country, capital in country_capital_dict.items():
    print(f'{country} -> {capital}')
