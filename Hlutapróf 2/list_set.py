def get_lists():
    ''' Function that makes a list of ints from the users input '''
    # Here we take the user_input and split it between each spacechar and parse it to int
    list_1 = [int(i) for i in input("Enter elements of a list separated by space: ").split()]
    list_2 = [int(i) for i in input("Enter elements of a list separated by space: ").split()]
    return list_1, list_2

def make_sets(list_1, list_2):
    ''' Function that converts lists into sets '''
    set_1, set_2 = [], []
    for item in list_1:
        if item not in set_1:  # If certain value is not in set then it is unique
            set_1.append(item)
    
    for item in list_2:
        if item not in set_2:
            set_2.append(item)
    
    return sorted(set_1), sorted(set_2)  # return it sorted

def make_intersection(set_1, set_2):
    ''' Function that makes an intersection from two sets '''
    # We get the upper and lower bound for the range in the "for" loop so that it goes through all numbers in both sets
    lower_bound = min(set_1[0], set_2[0])  # Lowest value of each set
    upper_bound = max(set_1[-1], set_2[-1])  # Highest value of each set
    intersection = []
    for i in range(lower_bound, upper_bound + 1):
        if i in set_1 and i in set_2:  # If a number is in both sets then append to intersection
            intersection.append(i)
    return intersection

def make_union(set_1, set_2):
    ''' Function that makes an union from two sets '''
    # Same function as make_intersection except "or" in the if statement
    lower_bound = min(set_1[0], set_2[0])
    upper_bound = max(set_1[-1], set_2[-1])
    union = []
    for i in range(lower_bound, upper_bound + 1):
        if i in set_1 or i in set_2:  # if number is in either set
            union.append(i)
    return union

def print_results(set_1, set_2, intersection, union):
    ''' Function that prints the sets '''
    print("Set 1: {}".format(set_1))
    print("Set 2: {}".format(set_2))
    print("Intersection: {}".format(intersection))
    print("Union: {}".format(union))

def main():
    ''' Main function for this program '''
    list_1, list_2 = get_lists()
    set_1, set_2 = make_sets(list_1, list_2)
    intersection = make_intersection(set_1, set_2)
    union = make_union(set_1, set_2)
    print_results(set_1, set_2, intersection, union)

main()