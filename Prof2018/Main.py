def text_reader(textfile):
    unread_list = []
    with open(textfile, "r") as f:
        for line in f:
            unread_list.append(line.strip("\n").split(" "))
    return unread_list

names_flights = text_reader("flights.txt")
john_count = sum(x.count("John") for x in names_flights)

print(names_flights)
print("John count: " + str(john_count))

