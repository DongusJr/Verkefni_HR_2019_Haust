def palindrome(in_str:
    only_letter_str = ""
    for letter in in_str:
        if letter.isalpha():
            only_letter_str += letter.lower()
    if only_letter_str == only_letter_str[::-1]:
        return True
    return False

in_str = input("Enter a string: ")

# call the function and print out the appropriate message
palindrome_bool = palindrome(in_str)
if palindrome_bool:
    print("\"{}\" is a palindrome.".format(in_str))
else:
    print("\"{}\" is not a palindrome.".format(in_str))