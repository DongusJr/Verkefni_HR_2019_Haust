n = int(input("Enter the length of the sequence: "))

num_1 = 1
num_2 = 2
num_3 = 3

for i in range(1, n+1):
    if 1 <= i <= 3:
        print(i, end=", ")
    else:
        new_num = num_1+num_2+num_3
        num_1 = num_2
        num_2 = num_3
        num_3 = new_num
        print(num_3, end=", ")

