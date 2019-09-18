# Variables
LEFT = "l"
RIGHT = "r"
QUIT = -1

pos = 0         # Position of the player
move_str = ""   # "r", "l" or quit

# Functions

def print_board(position):
    # Function that prints the board
    for grid in range(1, 11):
        if grid != position:
            print("x", end= "")
        else:
            print("o", end= "")
    print()

def move_pos(move, position):
    # Function that moves the position of the player
    if move == LEFT and position > 1:    # If the player is on the edge, don't change his position if he tries to move further
        position -= 1
    elif move == RIGHT and position < 10:
        position += 1
    elif move != LEFT and move != RIGHT:   # If input isn't "l" or "r", exit
        move = QUIT
    return move, position

def play(pos):
    #Function that loops the game
    move_str = input("Input your choice: ")
    move_str, pos = move_pos(move_str, pos) # Move the player
    print_board(pos)                        # Print the board
    if move_str == QUIT:
        exit()
    play(pos)        # Repeat if everything is right

# Main

while(not (1 <= pos <= 10)):    # Make sure the player inputs the right number
    pos = int(input("Input a position between 1 and 10: "))

print_board(pos)    # Initialize the board
print("l - for moving left\nr - for moving right\nAny other letter for quitting")

play(pos)   # The main play function, that repeats

