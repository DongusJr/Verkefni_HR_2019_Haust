import string

# Implement a function here
def unique_letter_list_maker(sentence):
    unique_letters = []
    for char in sentence:
        if char not in unique_letters and char not in string.punctuation and char not in string.whitespace:
            unique_letters.append(char)
    return unique_letters
# Main starts here
sentence = input("Input a sentence: ")
# Call the function here
unique_letters = unique_letter_list_maker(sentence)
print("Unique letters:", unique_letters)
print(string.whitespace, string.punctuation)