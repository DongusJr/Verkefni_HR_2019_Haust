def menu_selection():
    return input("Menu: \nadd(a), remove(r), find(f): ")

def execute_selection(choice, a_dict):
    if choice == "a":
        add_user(a_dict)
    elif choice == "r":
        remove_user(a_dict)
    else:
        find_user(a_dict)

def add_user(a_dict):
    key_input = input("Key: ")
    value_input = input("Value: ")
    if key_input not in a_dict:
        a_dict[key_input] = value_input
    else:
        print("Error. Key already exists.")

def remove_user(a_dict):
    remove_key_input = input("key to remove: ")
    if remove_key_input in a_dict:
        del a_dict[remove_key_input]
    else:
        print("Key not found.")

def find_user(a_dict):
    key_input = input("Key to locate: ")
    if key_input in a_dict:
        print("Value: {}".format(a_dict[key_input]))
    else:
        print("Key not found.")

def dict_to_tuples(a_dict):
    return a_dict.items()

# Do not change this main function
def main():
    more = True
    a_dict = {}
    
    while more:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more = again.lower() == 'y'
    
    dictlist = dict_to_tuples(a_dict)
    print(sorted(dictlist))

main()