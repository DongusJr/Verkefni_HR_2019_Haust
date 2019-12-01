import random

class Dice:

    def __init__(self, sides=6, dice_roll=0):
        if sides > 0:
            self.sides = sides
            self.dice_roll = dice_roll
        else:
            self.sides = 6
            self.dice_roll = dice_roll

    def roll(self):
        self.dice_roll = random.randint(1,self.sides)


    def __add__(self, other_dice):
        dice_sum = self.dice_roll + other_dice.dice_roll
        return Dice(12, dice_sum)

    def __str__(self):
        return str(self.dice_roll)

def run_dice_experiment():
    dice1 = Dice(6)
    dice2 = Dice(6)
    for _ in range(0,10):
        dice1.roll()
        dice2.roll()
        sum_dice = dice1 + dice2
        print("dice1: {}, dice2: {}, sum dice: {}".format(str(dice1), str(dice2), str(sum_dice)))
        sum_dice.roll()
        print("sum dice: {}".format(str(sum_dice)))

# Main program starts here
seed_number = int(input("Enter a seed: "))
random.seed(seed_number)
run_dice_experiment()   
    