CON = 0
ELO = 1
BDAY = 2

def open_file(file_name):
    try:
        return open(file_name, "r")
    except:
        print("file {} was not found.".format(file_name))
        return None

def make_player_dict(file_obj):
    player_dict = {}
    for line in file_obj:
        line = line.strip().split("; ")[1:]
        last_name, first_name = line.pop(0).split(", ")
        name = first_name + " " + last_name
        player_dict[name] = tuple(line)
    return player_dict

def count_attribute(player_dict, atr):
    atr_count = {}
    for player, atrs in player_dict.items():
        if atrs[atr] in atr_count:
            atr_count[atrs[atr]].append(player)
        else:
            atr_count[atrs[atr]] = [player]
    print(atr_count)
    return atr_count

def print_table(player_dict, bday_count):
    print("Players by birth year:\n----------------------")
    for bday, players in sorted(bday_count.items()):
        average_elo = 0
        for player in players:
            average_elo += float(player_dict[player][ELO])
        average_elo /= len(players)
        print("{} ({}) ({:.1f}):".format(bday, len(players), average_elo))
        for player in players:
            print("{:>40}{:>10d}".format(player, int(player_dict[player][ELO])))


def main():
    file_name = input("Enter the name of the file: ")
    file_obj = open_file(file_name)
    if file_obj:
        player_dict = make_player_dict(file_obj)
        bday_count = count_attribute(player_dict, BDAY)
        print_table(player_dict, bday_count)


main()