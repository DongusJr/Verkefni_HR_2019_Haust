age = int(input("Enter your age: "))

if 0 <= age <= 34:
    print("Young")
elif 35 <= age <= 50:
    print("Mature")
elif 51 <= age <= 69:
    print("Middle-aged")
elif age >= 70:
    print("Old")
else:
    print("Invalid age")  