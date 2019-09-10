# Verkefni 1
a_str = input("Input a string: ")
print(a_str[0] + " " + a_str[-1])

# Verkefni 2
a_str = input("Input a string: ")

a_str = a_str[3:] + a_str[:3]

print(a_str)

# Verkefni 3
a_str = input("Input a string: ")
count = 0
for char in a_str:
    if "o" == char.lower():
        print(count)
    count += 1

#Önnur leið:
    
# for thing in enumerate(a_str):
#     if "o" in thing:
#         print(thing[0])

# Verkefni 4
a_str = input("Input a float: ")
print("{:12.2f}".format(float(a_str)))

# Verkefni 5
a_str = input("Input a string: ")
output_str = ""
for char in a_str:
    if char.isdigit():
        output_str += char
print(output_str)

# Verkefni 6
name = input("Input a name: ")

first_name, last_name = name.split(", ")

print(last_name[0].upper() + ". " + first_name.title())

# Verkefni 7
my_int = int(input('Give me an int >= 0: '))
if my_int == 0:
    bin_str = "0"
else:
    bin_str = ""
my_temp_int = my_int

while(my_temp_int != 0):
    bin_str += str(my_temp_int%2)
    my_temp_int //= 2
    
bin_str = bin_str[::-1]

print("The binary of", my_int, "is", bin_str)