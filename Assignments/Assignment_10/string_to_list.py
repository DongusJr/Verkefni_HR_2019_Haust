def to_list(a_str):
    if "," in a_str:
        return a_str.split(",")
    else:
        return a_str.split()

# The main program starts here
the_string = input("Enter the string: ")
# call your function here
the_list = to_list(the_string)
print(the_list)