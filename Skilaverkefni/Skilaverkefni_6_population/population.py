# Functions

def get_year_index(year_lst):
    ''' Function that request year and then returns the index of it in the text file'''
    # Dont need try and except for this loop because all we compare are strings
    year_input = input("Enter year: ")
    if year_input in year_lst:
        return year_lst.index(year_input)  # return the index of the year
    else:
        print("Invalid year!")
        return get_year_index(year_lst)  # If it is an invalid year


def make_list(file_input):
    ''' Function that reads the given textfile and converts it to a list with population and state at a certain year'''
    pop_year_lst = []
    got_year_index = False  # Boolean for the get_year_index function
    try:
        with open(file_input) as file:  # Open, read then close the file
            for line in file:
                line_lst = line.strip().split()  # Remove whitespace and newlines

                if not got_year_index:  #  If we don't know what year we want, then we get it
                    year_index = get_year_index(line_lst) # The line_lst should look like: ["States", year1, year2, ...]
                    got_year_index = True
                    
                else:
                    if line_lst[1].isalpha():  # Fix the list if the state name is two words, i.e."New York"
                        line_lst = fix_state_name(line_lst)
                    pop_year_lst.append((int(line_lst[year_index]), line_lst[0]))  # Add the population and state as a tuple into the list

        return pop_year_lst

    except FileNotFoundError:
        print("Filename {} not found!".format(file_input))
        return None

def print_min_max(pop_year_lst):
    ''' Prints the minimum and maximum population from each state at a ceratain year '''
    print("Minimum: {}\nMaximum: {}".format(min(pop_year_lst), max(pop_year_lst)))

def fix_state_name(line_lst):
    ''' Takes states names that are two words and combines them into one string '''
    line_lst[0] = line_lst[0] + " " + line_lst[1]
    line_lst.pop(1)  # Remove the second word, because it's in the way
    return line_lst

def main(file_input):
    ''' The main function of this program '''
    population_list = make_list(file_input)  # Population list looks like: [(a,b),(c,d),...]
    if population_list != None:
        print_min_max(population_list)

#Main

file_input = input("Enter filename: ")

main(file_input)