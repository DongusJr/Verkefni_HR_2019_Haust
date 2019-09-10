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
    
def grid_update(movement, x, y):
    if movement == LEFT:
        x -= 1
        if x < 0:
            x = 4
    elif movement == RIGHT:
        x += 1
        if x > 4:
            x = 0
    elif movement == UP:
        y -= 1
        if y < 0:
            y = 4
    elif movement == DOWN:
        y += 1
        if y > 4:
            y = 0
    else:
        return (QUIT, x, y)
    return movement, x, y

def make_grid(x,y):
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[y][x] = POSITION  # Current position
    return grid

def print_grid(grid_ ):
    for i in grid_:
        print(*i)

# Main program starts here
# In your implementation, you have to use the functions and the constants given above


def play_game(grid_, x = 0, y = 0):
    try:
        for i in grid_:
            print(*i)
        move,x,y = grid_update(get_move(), x, y)
        new_grid = make_grid(x,y)
        if move == QUIT:
            raise ValueError
        play_game(new_grid, x, y)
    except ValueError:
        exit()

play_game(initialize_grid(), 0, 0)