def merge_lists(list1, list2):
    list3 = []
    add_to_list(list1, list3)
    add_to_list(list2, list3)
    return sorted(list3)

def add_to_list(list, list3):
    for item in list:
        if item not in list3:
            list3.append(item)

# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
