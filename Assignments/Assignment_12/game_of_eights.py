def check_eights(list):
    try:
        list = [int(i) for i in list]
    except:
        return "Error - please enter only integers."
    for i in range(len(list) -1):
        if int(list[i]) == int(list[i+1]) and int(list[i]) == 8:
            return True
    return False

    

element_list = input("Enter elements of list separated by commas: ").split(",")
print(check_eights(element_list))
