class IntList:
    def __init__(self, size = 0, int_list = []):
        self.__size = size
        self.__int_list = int_list[:]

    def __str__(self):
        return str(self.__int_list)

    def add(self, number):
        if len(self.__int_list) < self.__size:
            self.__int_list.append(number)


    def __len__(self):
        return len(self.__int_list)

    def full(self):
        if len(self) == self.__size:
            return True
        else:
            return False

    def __add__(self, other):
        min_size = min(self.__size, other.__size)
        new_int_list = []
        for i in range(min_size):
            new_int_list.append(self.__int_list[i] + self.__int_list[i])
        return IntList(min_size, new_int_list)

def main():
    # Main program starts here
    list1 = IntList(5) 	# Constructs an IntList that can hold 5 integers
    list2 = IntList(12) 	# Constructs an IntList that can hold 12 integers

    for i in range(10):
        list1.add(i)
        list2.add(i)

    print(list1)
    print(list2) 

    print("Length of list1 is: {}".format(len(list1)))
    print("Length of list2 is: {}".format(len(list2)))

    if list1.full():
        print("list1 is full")
    if list2.full():
        print("list2 is full")
    
    list3 = list1 + list2
    print(list3)

    list4 = list2 + list1
    print(list4)

main()