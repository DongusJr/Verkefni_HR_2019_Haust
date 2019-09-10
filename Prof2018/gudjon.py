def get_list():
    names_and_flights = []
    with open("flights.txt", "r") as f:
        for line in f:
            names_and_flights.append(line.strip("\n").split(" "))
        return names_and_flights

def no_dupes_in_list(imp_list):
    no_dupes_list = []
    for name_flight in imp_list:
        if name_flight not in no_dupes_list:
            no_dupes_list.append(name_flight)
        else:
            pass
    return no_dupes_list

def most_travel(imp_list, name_list):
    max_travel = 0
    max_travel_name = ""
    for name in name_list:
        temp_count = sum(x.count(name) for x in imp_list)
        if temp_count > max_travel:
            max_travel = temp_count
            max_travel_name = name
    return ("{} has been to {} countries".format(max_travel_name,max_travel))
            

def get_names_list(imp_list):
    names_list = []
    for name in imp_list:
        if name[0] not in names_list:
            names_list.append(name[0])
        else:
            pass
    return names_list

def print_lists(names_list, names_and_flights_list):
    for name in names_list:
        print("{}:".format(name))
        for flight in names_and_flights_list:
            if name == flight[0]:
                print("\t" + flight[1])
            else:
                pass
    print(most_travel(no_dupes_in_list(get_list()), get_names_list(get_list())))
    
print_lists(sorted(get_names_list(get_list())), sorted(no_dupes_in_list(get_list())))
