import random

TEAM_SIZE = 5
GAME_LENGTH = 48

class Team:
    def __init__(self, name):
        self.__name = name
        self.__team = []
        self.__points = 0
        for i in range(TEAM_SIZE):
            player = BasketballPlayer(i+1) # i+1 is the number for the player
            self.__team.append(player)

    def play_offence(self):
        random_index = random.randint(0, TEAM_SIZE-1)
        self.__points += self.__team[random_index].shoot_ball()

    def get_player_with_highest_score(self):
        highest_player = self.__team[0]
        for player in self.__team:
            if player > highest_player:
                highest_player = player
        return highest_player

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points

    def __str__(self):
        the_str = ''
        for player in self.__team:
            the_str += str(player)
        return the_str


class BasketballPlayer:
    # You need to implment this class
    def __init__(self, number, points=0):
        self.number = number
        self.points = points

    def __str__(self):
        return "Number: {} Points: {}\n".format(self.number, self.points)

    def shoot_ball(self):
        hit_or_miss = random.randint(0,1)
        if hit_or_miss == 1:
            self.points += 2
            return 2
        else:
            return 0
    
    def __gt__(self, other):
        if self.points > other.points:
            return True
        return False
    

def print_winner(team_a, team_b):
    if team_a.get_points() > team_b.get_points():
        print("{} won!".format(team_a.get_name()))
    elif team_b.get_points() > team_a.get_points():
        print("{} won!".format(team_b.get_name()))
    else:
        print("Tie!")


def print_scores(team_a, team_b):
    ''' You need to implent this function.  Print out:
        how many points each team scored
        the scoring of each player in each team
        the highest scoring player in each team  
    '''
    print("\n{} scored {} points!".format(team_a.get_name(), team_a.get_points()))
    print("{} scored {} points!\n".format(team_b.get_name(), team_b.get_points()))

    print("{} scoring:".format(team_a.get_name()))
    print(str(team_a))

    print("{} scoring:".format(team_b.get_name()))
    print(str(team_b))

    print("{} highest scoring player:".format(team_a.get_name()))
    print(team_a.get_player_with_highest_score())

    print("{} highest scoring player:".format(team_b.get_name()))
    print(team_b.get_player_with_highest_score())

def play(team_a, team_b):
    for _ in range(GAME_LENGTH):
        team_a.play_offence()    
        team_b.play_offence()
        
def random_seed():
    seed = int(input("Random seed: "))
    random.seed(seed)

def main():
    # You are not allowed to change this main function
    random_seed()
    chicago_bulls = Team("Chicago Bulls")
    la_lakers = Team("LA Lakers")

    play(chicago_bulls, la_lakers)
    print_winner(chicago_bulls, la_lakers)
    print_scores(chicago_bulls, la_lakers)

main()