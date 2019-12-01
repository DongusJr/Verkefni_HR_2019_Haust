def get_dict(file_obj):
    flyers_dict = {}
    for line in file_obj:
        person, country = line.strip().split(" ")
        if person not in flyers_dict:
            flyers_dict[person] = {country}
        else:
            flyers_dict[person].add(country)
    return flyers_dict

def get_max_travel(flyers_dict):
    max_count = 0
    max_person = ""
    for person, countries in sorted(flyers_dict.items(), reverse=True):
        if len(countries) > max_count:
            max_count = len(countries)
            max_person = person
    return (max_person, max_count)

def print_flyers(flyers_dict):
    for person, countries in sorted(flyers_dict.items()):
        print("{}:".format(person))
        for country in sorted(countries):
            print("\t{}".format(country))

    m_person, m_count = get_max_travel(flyers_dict)
    print("\n\n{} has been to {} countries".format(m_person, m_count))

def main():
    file_obj = open("flights.txt", "r")
    flyers_dict = get_dict(file_obj)
    print_flyers(flyers_dict)

main()