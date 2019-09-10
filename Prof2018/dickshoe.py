top_num = int(input("Upper number for the range: ")) # Do not change this line
perfect_numbers = []
for i in range(1, top_num):
    print("i: " + str(i))
    temp_sum = 0
    for x in range(1, i):
        if(i%x) == 0:
            temp_sum += x
    if temp_sum == i:
        perfect_numbers.append(i)

print(perfect_numbers)