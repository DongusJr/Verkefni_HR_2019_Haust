RANK = 0
COUNTRY = 1
ELO = 2
BYEAR = 3


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

def make_dict_countries(players_dict):
    countries_dict = {}
    for player, stats in players_dict.items(): # Player: [stats]
        if stats[COUNTRY] in countries_dict:  # If there is a player already from this country in this dict, add the new player
            countries_dict[stats[COUNTRY]].append(player)
        else:                                 # Else add the country assigned with this player
            countries_dict[stats[COUNTRY]] = [player]
    return countries_dict

def print_sorted(dict_countries, players_dict):
    for country, players in sorted(dict_countries.items()):
        print("{} ({}) ({:.1f}):".format(country, len(players), get_average_elo(players, players_dict)))  # len(players) = the amount of players from that certain country, also get the average elo from that country
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
        country_dict = make_dict_countries(players_dict)
        print_sorted(country_dict, players_dict)

main()