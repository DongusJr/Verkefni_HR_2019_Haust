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

def find_pos(puzzle_board, value):
    for number, line in enumerate(puzzle_board):
        if value in line:
            y = number
            x = line.index(value)
            return x, y

def check_valid(puzzle_board, user_move):
    if user_move > DIM**2:
        return False
    x_0, y_0 = find_pos(puzzle_board, 0)
    x_u, y_u = find_pos(puzzle_board, user_move)
    if abs(x_0-x_u) <= 1 and abs(y_0-y_u) <= 1 and not (abs(x_0-x_u) == 1 and abs(y_0-y_u) == 1):
        return True
    else:
        return False

def update_board(puzzle_board, user_move):
    x_0, y_0 = find_pos(puzzle_board, 0)
    x_u, y_u = find_pos(puzzle_board, user_move)
    puzzle_board[y_0][x_0] = puzzle_board[y_u][x_u]
    puzzle_board[y_u][x_u] = EMPTYSLOT
    return puzzle_board

def main():
    puzzle_board = initialize_board()
    display(puzzle_board)
    user_move = int(input())
    while user_move != QUIT:
        if check_valid(puzzle_board, user_move):
            puzzle_board = update_board(puzzle_board, user_move)
        display(puzzle_board)
        user_move = int(input())

main()