def even_sum(lst):
    lst = [int(i) for i in lst]
    return sum([i for i in lst if i%2 == 0])

def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))
