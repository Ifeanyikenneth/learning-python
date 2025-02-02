travel_log = [
  {
    "country": "Nigeria", 
    "cities_visited": ["Shibiri", "Ojo", "Etegbin"], 
    "total_visit": 12},
  {
    "country": "France", 
    "cities_visited": ["Berlin", "hamburg", "Stuttguart"], 
    "total_visit": 42
    },
]

def add_new_counrty(country_visited, times_visited, cities_visit):
  new_country = {}
  new_country["country"] = country_visited
  new_country["total_visit"] = times_visited
  new_country["cities_visited"] = cities_visit
# note: still remember in other to add to a list we are using the .append()
  travel_log.append(new_country)


add_new_counrty("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


