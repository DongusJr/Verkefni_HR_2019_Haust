# The function definition goes here
def in_range(num):
    if(1 < num < 555):
        return True
    return False
num = int(input("Enter a number: "))

# You call the function here
range_bool = in_range(num)
if range_bool:
    print("{} is in range.".format(num))
else:
    print("{} is outside the range!".format(num))