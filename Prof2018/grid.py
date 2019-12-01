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

def print_grid(grid):
    for line in grid:
        for row in line:
            print(row, end=" ")
        print()

def get_pos(move, pos):
    x,y = pos
    if move == RIGHT:
        if x < 4:
            x += 1
        else:
            x = 0
    elif move == LEFT:
        if x > 0:
            x -= 1
        else:
            x = 4
    elif move == UP:
        if y > 0:
            y -= 1
        else:
            y = 4
    elif move == DOWN:
        if y < 4:
            y += 1
        else:
            y = 0
    return (x,y)

def update_grid(pos):
    y,x = pos
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[x][y] = POSITION  # Current position
    return grid

# Main program starts here
# In your implementation, you have to use the functions and the constants given above

def main():
    grid = initialize_grid()
    pos = (0,0)
    print_grid(grid)
    move = get_move()
    while move != QUIT:
        pos = get_pos(move, pos)
        grid = update_grid(pos)
        print_grid(grid)
        move = get_move()



main()