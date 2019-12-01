# Constants
DIM = 4 # dimension of the board DIMxDIM
EMPTYSLOT = 0
QUIT = 0

def initialize_board():
    ''' Creates the initial board according to the user input.
    The board is a list of lists.
    The list contains DIM elements (rows), each of which contains DIM elements (columns)'''
    numbers = input().split()
    numbers = [int(number) for number in numbers]
    puzzle_board = []
    index = 0
    for _ in range(DIM):
        row = numbers[index:index + DIM]
        index += DIM
        puzzle_board.append(row)

    return puzzle_board
    

def display(puzzle_board):
    ''' Display the board, printing it one row in each line '''
    print()
    for i in range(DIM):
        for j in range(DIM):
            if puzzle_board[i][j] == EMPTYSLOT:
                print("\t", end="")
            else:
                print(str(puzzle_board[i][j]) + "\t", end="")
        print()
    print()

def find_pos(board, value):
    ''' Function that takes a board and a value from user and outputs the position of that value as a tuple '''
    for number, line in enumerate(board):
        if value in line:  # y
            y = number
            x = line.index(value)  # Where the value is in the list is the x value
            return (x, y)
        
def update_board(board, player_inp):
    ''' Function that takes in a board and the players input and outputs a new board with the player movement implemented '''
    x_inp, y_inp = find_pos(board, player_inp)  # Players choice position
    x_0, y_0 = find_pos(board, EMPTYSLOT)  #  Empty space position
    if check_valid(board, player_inp):  # check if valid
        board[y_0][x_0] = player_inp  # New position
        board[y_inp][x_inp] = EMPTYSLOT  # now this is empty
    return board

def check_valid(board, player_inp):
    ''' Function that checks the position of players input and empty slot and returns whether it can move there or not '''
    x_0, y_0 = find_pos(board, EMPTYSLOT)
    x_inp, y_inp = find_pos(board, player_inp)
    # If the slot is exactly 1 away from the empty slot then we know it can go there
    if (abs(x_0 - x_inp) == 1 or abs(y_0 - y_inp) == 1) and not ((abs(x_0 - x_inp) >= 1 and abs(y_0 - y_inp) >= 1)):
        return True
    else:
        return False

def main():
    ''' Main function of this program '''
    board = initialize_board()
    display(board)
    player_input = int(input())
    while player_input != 0:  # Loops here
        board = update_board(board, player_input)  # update
        display(board)                             # display
        player_input = int(input())                # input

main()