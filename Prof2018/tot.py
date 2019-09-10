number = int(input("Please choose a number"))
print(number)
sequence = [number]
while number > 1:
    if number % 2 == 0:
        number = number//2
        sequence.append(number)
    else:
        number = number*3 + 1
        sequence.append(number)

for number in sequence:
    print(number,end=", ")


