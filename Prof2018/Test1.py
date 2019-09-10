def get_list():
    with open("flights.txt", 'r') as f:
        list_of_names_and_flights = []
        list_of_names_and_flights_no_dupes = []
        for line in f:
            list_of_names_and_flights.append(line.strip('\n').split(" "))
        # --- Removes Dupes---
        for i in list_of_names_and_flights:
            if i not in list_of_names_and_flights_no_dupes:
                list_of_names_and_flights_no_dupes.append(i)
        return list_of_names_and_flights_no_dupes


def get_names_list(inp_list):
    # -- gets a list of names no dupes --
    names_list = []
    for i in inp_list:
        if i[0] not in names_list:
            names_list.append(i[0])
    return names_list


def finds_amount(imp_list):
    # -- finds the biggest traveler --
    names_dupes = []
    biggest_traveler = 0
    # -- Creates a list with duplicate names --
    for i in imp_list:
        names_dupes.append(i[0])
    # -- Checks the names agains a list with dupes --
    for i in get_names_list(get_list()):
        if names_dupes.count(i) > biggest_traveler:
            biggest_traveler = names_dupes.count(i)
            biggest_traveler_name = i
        else:
            pass
    return ("{} has been to {} countries".format(biggest_traveler_name, biggest_traveler))

def print_travelers(get_list, names_list):
    for i in names_list: 
        print(i + ":")
        for x in get_list:

            if i == x[0]:
                print("\t" + x[1])

max_str = finds_amount(get_list())

names_flights_list = sorted(get_list())
names_list = sorted(get_names_list(names_flights_list))

print_travelers(names_flights_list, names_list)
print(max_str)