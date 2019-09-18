# is_prime function definition goes here
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
num = int(input("Input an integer greater than 1: "))

# Call the function here and print out the appropriate message
prime_bool = is_prime(num)
if prime_bool:
    print("{} is a prime".format(num))
else:
    print("{} is not a prime".format(num))