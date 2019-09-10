for number in range(10, 100): 
    number_fd = number//10     # First digit of the double digit number
    number_sd = number%10      # Second digit of the double digit number
    special_sum = (number_fd + number_sd)**2  #Sum of the first digit and the second digit, squared
    if(special_sum == number):  
        print(number)

for i in range (1, 100):  
    count = 0             # Keeps count of the divisors for each number, resets for each 
    # check if (1:i) are divisors
    for x in range(1,i+1):  
        if i%x == 0:      
            count += 1
    if count == 10:   # If the number has exactly 10 divisors, print it
        print(i)
