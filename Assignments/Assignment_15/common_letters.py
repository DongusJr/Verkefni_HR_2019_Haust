def make_set_list(name):
    same_ch = []
    for chr in name[0]:
        if chr in name[1] and chr not in same_ch:
            same_ch.append(chr)
    return sorted(same_ch)

def make_set_set(name):
    first_name = set(name[0])
    second_name = set(name[1])
    return first_name & second_name

def main():
    name = input("Enter name: ").lower().split()
    set_list = make_set_list(name)
    set_set = make_set_set(name)
    print(set_list)
    print(sorted(set_set))


main()