# Your function definition goes here
def count_case(input_str):
    upper_count = 0
    lower_count = 0
    for letter in input_str:
        if letter.islower():
            lower_count += 1
        elif letter.isupper():
            upper_count += 1
        else:
            continue
    return upper_count, lower_count
    
user_input = input("Enter a string: ")

# Call the function here
upper, lower = count_case(user_input)
print("Upper case count: ", upper)
print("Lower case count: ", lower)
