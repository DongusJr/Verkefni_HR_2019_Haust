def get_input():
    a_list = input("Input a list of integers separated with a comma: ").split(",")
    return {int(i) for i in a_list}

def print_options():
    print("1. Intersection\n2. Union\n3. Difference\n4. Quit")

def choice(user_choice):
    if user_choice == 1:
        intersection()
    elif user_choice == 2:
        union()
    elif user_choice == 3:
        difference()

def intersection():
    print(set_a & set_b)

def union():
    print(set_a | set_b)

def difference():
    print(set_a - set_b)


set_a = get_input()
set_b = get_input()
print("{}\n{}".format(set_a, set_b))
user_choice = 0
while user_choice != 4:
    print_options()
    user_choice = int(input("Set operation: "))
    choice(user_choice)