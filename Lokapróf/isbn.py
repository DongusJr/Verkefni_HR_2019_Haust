ISBN = "X-XXX-XXXXX-X"  # The format of the ISBN, X represents digits and - are simply "-"

def check_if_valid(user_input):
    ''' Function that checks if the user number is a valid ISBN depending on how the constants ISBN is 
        returns True if the user number has the right format
        returns False if the user number is incorrect '''
    if len(user_input) != len(ISBN):  # If they are not the same length
        return False
    else:
        for l_index, letter in enumerate(ISBN):
            if letter == "X":  # Check if the constant has an X, if it does the user's number has to have a digit in that index
                if not user_input[l_index].isdigit():  # Same index as the X
                    return False
            elif letter == "-": # If it's a hyphen, then the user number needs to have a hyphen too
                if user_input[l_index] != "-":
                    return False
    return True

def main():
    ''' Main function of this program '''
    user_input = input("Enter an ISBN: ")
    while user_input != "q":  # Main loop
        valid_format = check_if_valid(user_input)
        if valid_format:
            print("Valid format!")
        else:
            print("Invalid format!")
        user_input = input("Enter an ISBN: ")  # Continue the loop unless the user enters "q"

main()