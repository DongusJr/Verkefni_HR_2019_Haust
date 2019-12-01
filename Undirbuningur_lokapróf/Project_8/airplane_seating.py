A = 65
TAKEN = "X"

def make_seat_list(rows, seats):
    seat_list = []
    seat_letters = [chr(i) for i in range(A, (A + seats))]
    for i in range(rows):
        seat_list.append(seat_letters[:])
    return seat_list

def display_seats(seat_list):
    for row in range(len(seat_list)):
        print((row + 1), end="   ")
        for number, seat in enumerate(seat_list[row]):
            if number == (len(seat_list)//2):
                print("  ", end="")
            print(seat, end=" ")
        print()

def check_if_valid(row, seat, rows, seat_list):
    if (int(row) < 1 or int(row) > rows):
        print("Seat number is invalid")
        return True
    elif seat not in seat_list[int(row)-1]:
        print("seat number is invalid")
        return True
    else:
        return False

def replace_seat_list(row, seat, seat_list):
    seat_index = seat_list[int(row)- 1].index(seat)
    seat_list[int(row) - 1][seat_index] = TAKEN
    return seat_list 

def main():
    rows = int(input("Enter number of rows: "))
    seats = int(input("Enter number of seats in each row: "))
    total_seats = rows*seats
    seat_list = make_seat_list(rows, seats)
    running = True
    seat_count = 0
    display_seats(seat_list)
    while running:
        seat_not_valid = True
        while seat_not_valid:
            row, seat = input("Input seat number: ").split(" ")
            seat_not_valid = check_if_valid(row, seat, rows, seat_list)
        seat_list = replace_seat_list(row, seat, seat_list)
        seat_count += 1
        display_seats(seat_list)
        if seat_count == total_seats:
            running = False
        else:
            continue_str = input("More seats (y/n)? ").lower()
            if continue_str != "y":
                running = False
        


main()