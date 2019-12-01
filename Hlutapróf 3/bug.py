LENGTH = 20  # Length of the board

class Bug:
    ''' Class bug, the bug is initialize with a certain position
        it is possible to move() and turn() the bug on a board '''
    def __init__(self, pos=1):
        ''' Initialize the bug
            Note that in this function pos is always deducted by one, it is for the convenience of the user
            (user writes in base-1)'''
        # Make sure that the position is valid, if not change it to a valid position
        if pos < 1:
            self.pos = 0
        elif pos > LENGTH:
            self.pos = LENGTH - 1
        else:
            self.pos = pos - 1
        self.turn_right = True
        self.board = ("x"*LENGTH)  # Make the board "xx...xx"

    def __str__(self):
        ''' Print the board '''
        print_board = self.board[:self.pos] + "b" + self.board[(self.pos+1):]  # Slice the board and add the bug to it depending on it's position
        return print_board

    def move(self):
        ''' Method that moves the bug by one '''
        if 0 < self.pos < 19:  # Make sure it can not go out of bounds
            if self.turn_right:  # Check the boolean wheter it moves to the right or left
                self.pos += 1
            else:
                self.pos -= 1

    def turn(self):
        ''' Method that turns the bug '''
        if self.turn_right:  # If it is going right
            self.turn_right = False
        else:                # If it is going left
            self.turn_right = True

    def __gt__(self, another_bug):
        ''' Method overload for comparison of two bugs
            returns True or False depending of which bug has a higher position '''
        if self.pos > another_bug.pos:
            return True
        else:
            return False

    def __add__(self, another_bug):
        ''' Method overload for addition of two bugs position to make a new one '''
        pos_sum = self.pos + another_bug.pos + 2
        return Bug(pos_sum)  # Make an instance of the new bug
