name_num_dict = {}
continue_str = "y"

while continue_str == "y":
    name_input = input("Name: ")
    number_input = input("Number: ")
    name_num_dict[name_input] = number_input
    continue_str = input("More data (y/n)? ").lower()

print(sorted(name_num_dict.items()))