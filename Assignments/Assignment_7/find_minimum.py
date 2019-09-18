# find_min function definition goes here
def find_min(num_one, num_two):
    if num_one < num_two:
        return num_one
    else:
        return num_two

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
    
# Call the function here
minimum = find_min(first, second)
print("Minimum: ", minimum)