# Functions

def print_min_max(year_index):
    ''' Print the maximum and minimum for certain year'''
    # Save the min and max population for the states
    min_state = [float("inf"), None]  # Index 0: population, Index 1: name of state
    max_state = [float("-inf"), None]
    # Find min and max
    for i in range(1, len(pop_list)):
        if pop_list[i][year_index] > max_state[0]:
            max_state[0] = pop_list[i][year_index]
            max_state[1] = pop_list[i][0]
        if pop_list[i][year_index] < min_state[0]:
            min_state[0] = pop_list[i][year_index]
            min_state[1] = pop_list[i][0]
    
    print("Minimum: ({}, '{}')\nMaximum: ({}, '{}')".format(min_state[0], min_state[1], max_state[0], max_state[1]))

def get_input():
    ''' Function that takes input and loops if you enter an invalid year'''
    try:
        year_input = int(input("Enter year: "))
        if year_input in pop_list[0]:
            for i in range(1,len(pop_list[0])):
                if year_input == pop_list[0][i]:
                    year_index = i  # Save the index of the year for calculations
            print_min_max(year_index)  # Print
        else:
            raise # invalid int, get input again
    except:  # For Value_error and integer out of place
        print("Invalid year!")
        get_input()  # Loop

# List of states and years, empty
pop_list = []

#Main


try:
    input_file = input("Enter filename: ")
    # Opens the file, adds it to inner_list, then adds into the later list for two dimentional list, then closes the file
    with open(input_file, "r") as file:
        for line in file:
            inner_pop_list = line.strip().split()  # Remove whitespace and newline
            if inner_pop_list[0].isalpha() and inner_pop_list[1].isalpha():
                inner_pop_list[0] = inner_pop_list[0] + " " + inner_pop_list[1]  # If there are two word states i.e. New York, add them together
                inner_pop_list.pop(1)  # Remove the later word because it's useless now
            for i in range(1, len(inner_pop_list)):
                inner_pop_list[i] = int(inner_pop_list[i])  # Indexes from 1-3 should be integers
            pop_list.append(inner_pop_list)  # Two dimentional list
        get_input() # Gets input, then prints
except FileNotFoundError:
    print("File name {} not found!".format(input_file))
