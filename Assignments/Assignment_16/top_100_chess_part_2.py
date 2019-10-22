
RANK = 0
COUNTRY = 1
ELO = 2
YEAR = 3


def open_file(file_name):
    try:
        return open(file_name, "r")
    except FileNotFoundError:
        return None

def make_player_dict(file_obj):
    players_dict = {}
    for line in file_obj:
        line = line.strip().split("; ")  # Split each element,
        player_ln, player_fn = line.pop(1).strip("").split(", ") # remove the players name from the list and save it as first name and last name 
        players_dict[(player_fn + " " + player_ln)] = line  # add to the dictionary the players along with their stats [Rank, country, elo, birth year]
    return players_dict

def make_dict_stat(players_dict, stat): # Stat either: rank, country, elo or year 
    stats_dict = {}  
    for player, stats in players_dict.items(): # iterate through players and their stats
        if stats[stat] in stats_dict: # If stat in dictionary then add the player to the list
            stats_dict[stats[stat]].append(player)
        else:                         # Else make a new list with this player
            stats_dict[stats[stat]] = [player]
    return stats_dict

def print_sorted(dict_stats, players_dict):
    for stat, players in sorted(dict_stats.items()):
        print("{} ({}) ({:.1f}):".format(stat, len(players), get_average_elo(players, players_dict)))  # len(players) = the amount of players from that certain country, also get the average elo from that country
        for player in players:
            print("{:>40}{:>10d}".format(player, int(players_dict[player][ELO]))) # print players and elo from a certain country

def  get_average_elo(player_list, players_dict):
    ''' A Function that returns average elo from a certain list of players '''
    elo_sum = 0
    for player in player_list:
        elo_sum += int(players_dict[player][ELO])  # Get elo sum
    return (elo_sum/len(player_list))  # Retrun total sum divided by total amount of players in list

def main():
    file_name = input("Enter filename: Players by country:\n")
    print("-------------------")
    file_obj = open_file(file_name)
    if file_obj:  # If it is not empty
        players_dict = make_player_dict(file_obj)
        country_dict = make_dict_stat(players_dict, COUNTRY)
        year_dict = make_dict_stat(players_dict, YEAR)
        print_sorted(country_dict, players_dict)
        print("Players by birth year:\n----------------------")
        print_sorted(year_dict, players_dict)

main()