def open_file(file_name):
    try:
        return open(file_name, "r")
    except FileNotFoundError:
        print("Filename {} not found!".format(file_name))
        return None

def get_year(state_list):
    year = input("Enter year: ")
    if year in state_list[0]:
        return year
    else:
        print("Invalid year!")
        return get_year(state_list)

def make_state_list(file_obj):
    state_list = []
    for line in file_obj:
        line = line.strip().split()
        if line[1].isalpha():
            line[0] = line[0] + " " + line[1]
        line.pop(1)
        state_list.append(line)
    return state_list

def get_name_pop_list(year, state_list):
    state_tuple_list = []
    first_line = True
    for state_pop in state_list:
        if first_line:
            year_index = state_list[0].index(year)
            first_line = False
        else:
            state_tuple_list.append((int(state_pop[year_index]), state_pop[0]))
    return state_tuple_list

def print_results(state_tuple_list):
    print("Minimum: {}\nMaximum: {}".format(min(state_tuple_list), max(state_tuple_list)))

def main():
    file_name = input("Enter filename: ")
    file_obj = open_file(file_name)
    if file_obj:
        state_list = make_state_list(file_obj)
        year = get_year(state_list)
        state_tuple_list = get_name_pop_list(year, state_list)
        print_results(state_tuple_list)

main()