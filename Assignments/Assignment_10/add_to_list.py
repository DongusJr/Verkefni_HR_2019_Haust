the_list = []
# Your functions should appear here
def add_to_list(lst, a_input): 
    lst.append(a_input)
    return lst
    
def main(the_list):
    get_input = input("Enter value to be added to list: ")
    
    if get_input == "exit":
        the_list *= 3
        for item in the_list:
            print(item)
        exit()

    the_list = add_to_list(the_list,get_input)
    main(the_list)
# Main program starts here
# It should mostly be a sequence of function calls
main(the_list)
