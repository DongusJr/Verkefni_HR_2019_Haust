def get_seat_list(row_input, seat_input):
    ''' Function that makes the seat list, also returns the seats available for error checking 
    Input: number of rows and seats from user
    output: A two dimentional seat list along with seat character list '''
    inner_seat_list = [chr(i) for i in range(65, (65 +seat_input))]  # chr(65) = 'A', so if the input is i.e. "3", we get [A, B, C]
    seat_list = []
    for row in range(row_input):
        seat_list.append(inner_seat_list)  # Two dimentional list

    return seat_list, inner_seat_list 

def print_seat_list(seat_list):
    ''' Function that prints out the seat list, arraning it like like a plane would look like '''
    for i in range(len(seat_list)):
        print("{:>2}".format(i+1), end="   ")  # Number of row
        for j, seat in enumerate(seat_list[i], 0):  # We use enumerate number to seperate the seat
            if j == (len(seat_list[i]) // 2):  # split the seats so that there are even number of seats each side
                print("  ", end="")
            print(seat, end=" ")
        print()  # Newline

def replace_seat(seat_list, row, seat):
    ''' Function that replaces the seat that the user gave us into "X" for occupied '''
    # Replace the inner with a new one that replaces the users seat with "X"
    seat_list[int(row) - 1] = [seat_num.replace(seat, "X") for seat_num in seat_list[int(row) - 1]]
    return seat_list

def is_valid_seat(seat_list, valid_seat_list, row, seat):
    ''' Function that checks either if the user gave an appropriate number for the row or an appropriate seat
    input: the seat list, list with valid seats, row and seat input from user
    output: boolean that indicates wheter input are valid or not '''
    try:
        if (1 <= int(row) <= len(seat_list)) and seat in valid_seat_list:  # valid_seat_list : [A, B, ...]
            return True
        else:
            print("Seat number is invalid!")
            return False
    except ValueError:
        print("Seat number is invalid!")
        return False

def is_seat_taken(seat_list, row, seat):
    ''' Function that checks if users input is occupied or not '''
    if seat in seat_list[int(row) - 1]: # Check if the seat has not been replaced by "X"
        return False
    else:
        print("That seat is taken!")
        return True

def is_seat_available(seat_list):
    ''' Function that checks if all the seats are taken '''
    for row in seat_list:
        for seat in row:
            if seat != "X":  # If it finds a seat without "X", then we know it is not full
                return True
    return False
    
def loop(seat_list, valid_seat_list, valid_seat = False, seat_taken = True):  # Reset the booleans for each loop with default assignment
    ''' Function that loops the functionality of the program '''
    while not valid_seat or seat_taken: # Check if it is a valid seat
        row, seat = input("Input seat number (row seat): ").split()
        valid_seat = is_valid_seat(seat_list, valid_seat_list, row, seat)
        if valid_seat: # If we know that the user input is not a valid seat then we don't need to run this function
            seat_taken = is_seat_taken(seat_list, row, seat)
    
    seat_list = replace_seat(seat_list, row, seat)  # Replace the user input
    print_seat_list(seat_list)  # Print the new seat plan
    # Ask the user if he wants to coninue
    if is_seat_available(seat_list):
        continue_str = input("More seats (y/n)? ").lower()
        if continue_str == "y":
            loop(seat_list, valid_seat_list) # Loop

def main():
    ''' Main function of this program '''
    # User input
    row_input = int(input("Enter number of rows: "))
    seat_input = int(input("Enter number of seats in each row: "))
    # Initialize
    seat_list, valid_seat_list = get_seat_list(row_input, seat_input)
    print_seat_list(seat_list)
    loop(seat_list, valid_seat_list)
    
main()