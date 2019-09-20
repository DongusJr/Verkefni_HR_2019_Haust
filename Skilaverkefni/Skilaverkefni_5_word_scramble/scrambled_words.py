import string
#Functions

def has_punctuation(word):
    ''' This Function checks if a word has punctuation at the end of the word
    Input: a word
    Return: the word without punctuation, punctuation variable and a boolean '''
    if word[-1] in string.punctuation:
        punc_char = word[-1]  # Save the punctuation for later
        word = word[0:-1]     # Get the word without the punctuation
        return word, punc_char, True
    else:
        return word, word[-1], False

def scramble_word(word_len, word, punc_bool, punc_char):
    ''' This function scrambles all the word except for the first and last letter
    Input: lenght of the word, the word, whether it has punctuation, and the punctuation
    Return: only the output string '''
    output_str = ""
    if word_len > 0: # i.e if "-" is the sentence then has_punctuation function will remove it, so we need to make an exception for that
        output_str += word[0]  #First letter

    temp_len = word_len  # Control variable for the while
    while(temp_len >= 3):  # While there are more than 1 letter besides the first and last letter
        if temp_len >= 4: # If there are two letters to scramble
            output_str += word[word_len - (temp_len - 2)] + word[word_len - (temp_len - 1)] # Second to second last letter
        else:  # If there is only one left
            output_str += word[-2]
        temp_len -= 2

    if punc_bool:
            output_str += word[-1] + punc_char + " "  # Add the last letter and punctuation
    elif word_len > 1:
            output_str += word[-1] + " "  # Add the last letter
    else: 
            output_str += " " # Add nothing if it's a 1 letter word
    return output_str

# Main

file_input = input("Enter name of file: ")

try:
    txt_file = open(file_input, "r")  # Open text file as read

    for line in txt_file:
        punc_bool = False  # Boolean that holds on if a line has a punctuation
        line = line.strip()  # Remove the \n from each line
        line, punc_char, punc_bool = has_punctuation(line)
        word_len = len(line)
        output_str = scramble_word(word_len, line, punc_bool, punc_char)
        print(output_str, end="")
        
    print()
    txt_file.close()  # Close the text file

except FileNotFoundError:   # If the file is not found  
    print("File {} not found!".format(file_input))