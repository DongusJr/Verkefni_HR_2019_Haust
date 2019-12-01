def open_file(file_name):
    try:
        return open(file_name, "r")
    except FileNotFoundError:
        return None

def make_name_dict(file_obj):
    name_dict = {}
    for line in file_obj:
        name, country = line.strip().split()
        if name in name_dict:
            name_dict[name].add(country)
        else:
            name_dict[name] = {country}
    return name_dict

def count_countries(name_dict):
    max_name = ""
    max_count = 0
    for name, count_set in name_dict.items():
        if len(count_set) == max_count:
            if name[0] < max_name[0]:
                max_name = name
        elif len(count_set) > max_count:
            max_count = len(count_set)
            max_name = name
    return (max_name, max_count)

def print_dict(name_dict, max_tuple):
    for name, countries in name_dict.items():
        print("{}:".format(name))
        for country in sorted(countries):
            print("\t{}".format(country))
    print("\n{} has been to {} countries".format(max_tuple[0], max_tuple[1]))

def main():
    file_name = input("Whats the name of the file? ")
    file_obj = open_file(file_name)
    if file_obj:
        name_dict = make_name_dict(file_obj)
        max_tuple = count_countries(name_dict)
        print_dict(name_dict, max_tuple)


main()