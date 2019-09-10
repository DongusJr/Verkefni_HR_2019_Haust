num_stars = int(input("Number of stars: "))

for i in range(1, (num_stars + 1)):  #  i,x span from 1 to num_stars
    for x in range(1, (num_stars + 1)):
        if(i >= x):               # Each iteration of the "i" loop makes a new line, 
            print("*", end = "")  # The if statement in the "x" loop makes sure that right amount of stars are place in a right line
    print("\n")                   # i.e. first line has one star, second has two and so on, in other words i>=x