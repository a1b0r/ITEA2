dic_countries = {"Ukraine": "Kyiv", "Poland": "Krakow", "Belarus": "Minsk", "Italy": "Rome", "France": "Paris"}
#dic_countries = dict(Ukraine="Kyiv", Poland="Krakow")
list_countries = ["Israel", "Island", "Ukraine", "Poland", "Belarus"]

for countries in list_countries:
    if countries in dic_countries:
        print(dic_countries[countries])
