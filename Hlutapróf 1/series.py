#Get the variables for the while loop
first = int(input("First: "))
step = int(input("Step: "))
sum = 0

while(sum < 100):  #Run until the sum exceeds 100
    print(first, end = " ")  #end = " ", makes it print space inbetween the numbers
    sum += first  #Add to the sum
    first += step
    
print("\n" + "Sum of series: " + str(sum))