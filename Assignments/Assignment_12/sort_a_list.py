# sort_list() function goes here
def sort_list(a_list):
    return a_list.sort()


# get_list() function goes here
def get_list():
    a_list = []
    try:
        while(True):
            a_list.append(int(input()))
    except:
        return a_list
        
# Do not modify this part
def main():
    a_list = get_list()
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    
main()