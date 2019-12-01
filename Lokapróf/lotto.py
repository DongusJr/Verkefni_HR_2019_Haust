MAX_NUMBER = 40
MIN_NUMBER = 1
LEN_ROW = 5

def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        print("File {} not found!".format(filename))
        return None

def make_lotto_list(file_obj):
    ''' Function that makes a two dimentional list that represents the lotto table given by the file '''
    lotto_list = []
    for line in file_obj:
        line = line.strip().split(" ")
        lotto_list.append(line)  # Append the row of numbers to the lotto list
    return lotto_list

def check_if_valid(numbers):
    ''' Function that checks if the user input is valid
        returns True if it is valid else it returns False '''
    if len(numbers) != LEN_ROW:  # The amount of numbers given by user need to equal to length of each row in the lotto
        return False
    for number in numbers:
        if not number.isdigit():  # Check if they are all digits
            return False
        elif int(number) < MIN_NUMBER or int(number) > MAX_NUMBER:  # Make sure they are in range
            return False
    # the numbers given or ok if they get through here
    return True

def update_lotto_list(lotto_list, user_numbers):
    ''' Function that marks '*' to the correctly guessed number by user '''
    for number in user_numbers:
        for row in lotto_list:
            if number in row:  # If one of the user_number is in one of the lotto rows
                number_index = row.index(number)
                row[number_index] += "*"
    return lotto_list

def print_results(lotto_list):
    ''' Function that prints out the lotto table with the user guesses marked '''
    for row in lotto_list:
        for number in row:
            print(number, end=" ")
        print()  # Newline


def main():
    ''' Main function of this program '''
    filename = input("Enter file name: ")
    file_obj = open_file(filename)
    if file_obj:  # If the file_obj is not None
        lotto_list = make_lotto_list(file_obj)
        file_obj.close()  # Don't need the filestream anymore
        user_numbers = input("Enter winning numbers: ").split(" ")  # user winning numbers in a list
        numbers_are_valid = check_if_valid(user_numbers)
        if numbers_are_valid:
            lotto_list = update_lotto_list(lotto_list, user_numbers)
            print_results(lotto_list)
        else:  # If file_obj = None
            print("Winning numbers are invalid!") 

main()