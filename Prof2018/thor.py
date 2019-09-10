from collections import defaultdict

name_flights_dict = defaultdict(set)
with open("flights.txt", "r") as data:
    for line in data:
        names_and_flights = line.strip("\n").split(" ")
        name = names_and_flights[0]
        flight = names_and_flights[1]
        name_flights_dict[name].add(flight)

print(name_flights_dict)
def most_traveled(imp_dict):
    traveler_name = ""
    max_traveler_num = 0
    for name in name_flights_dict:
        if len(name_flights_dict[name]) > max_traveler_num:
            max_traveler_num = len(name_flights_dict[name])
            traveler_name = name    
    return ("{} has been to {} countries".format(traveler_name, max_traveler_num))

for name in sorted(name_flights_dict):
    print(name + ":")
    for country in sorted(name_flights_dict[name]):
        print("\t" + country)
print(most_traveled(name_flights_dict))

