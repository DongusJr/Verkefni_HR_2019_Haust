from bug import Bug

print("Bug 1:")
bug1 = Bug(10)  # creates an instance of a bug whose initial position is at 10
print(bug1)

for i in range(1,3):
    bug1.move()
    print(bug1)

bug1.turn()

for i in range(1,5):
    bug1.move()
    print(bug1)

print("Bug 2:")
bug2 = Bug(5)   # creates an instance of a bug whose initial position is at 5
bug2.turn()
bug2.move()
print(bug2)

if bug1 > bug2:
    print("Bug1 has travelled further than bug2")

print("Bug 3:")
# creates an instance of a bug whose initial position is the sum of the position of bug1 and bug2
bug3 = bug1 + bug2  
print(bug3)
bug3.move()
bug3.move()
print(bug3)
if bug3 > bug1:
    print("Bug3 has travelled further than bug1")

print("________TEST2_________")

print("Bug 1:")
bug1 = Bug(18)  # creates an instance of a bug whose initial position is at 18
print(bug1)

for i in range(1,5):
    bug1.move()
    print(bug1)


print("________TEST3_________")

bug1 = Bug(25)
print(bug1)

bug2 = Bug(-5)
bug2.turn()
bug2.move()
print(bug2)

print("________TEST4_________")

bug1 = Bug(10)
bug2 = Bug(5)
bug3 = bug1 + bug2
print(bug3)


bug1 = Bug(7)
bug2 = Bug(3)
print(bug1 > bug2)
