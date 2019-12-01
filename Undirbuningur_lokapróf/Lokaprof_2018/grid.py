# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'

def get_move():
    ''' Returns a move corresponding to the user input direction '''
    move = input('Move: ')
    
    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move

def initialize_grid():
    ''' Returns an initialized grid for the given dimension '''
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[0][0] = POSITION  # Current position
    return grid

def update_grid(grid, move, x, y):
    grid[y][x] = EMPTY
    if move == "r":
        if x < 4:
            x += 1
        else:
            x = 0
    if move == "l":
        if x > 0:
            x -= 1
        else:
            x = 4
    if move == "d":
        if y < 4:
            y += 1
        else:
            y = 0
    if move == "u":
        if y > 0:
            y -= 1
        else:
            y = 4
    grid[y][x] = POSITION
    return x, y


def display_grid(grid):
    for line in grid:
        for square in line:
            print(square, end=" ")
        print()

def main():
    pos_x, pos_y = 0,0
    grid = initialize_grid()
    display_grid(grid)
    move = get_move()
    while move != QUIT:
        pos_x, pos_y = update_grid(grid, move, pos_x, pos_y)
        display_grid(grid)
        move = get_move()

main()
# Main program starts here
# In your implementation, you have to use the functions and the constants given above