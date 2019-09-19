import string
#Functions

def has_punctuation(word):
    if word[-1] in string.punctuation:
        punc_char = word[-1]
        word = word[0:-1]
        return word, punc_char, True
    else:
        return word, word[-1], False

def scramble_word(word_len, word, punc_bool, punc_char):
    output_str = ""
    if word_len > 0:
        output_str += word[0]
    temp_len = word_len
    while(temp_len >= 3):
        if temp_len >= 4:
            output_str += word[word_len - (temp_len - 2)] + word[word_len - (temp_len - 1)]
        else:
            output_str += word[-2]
        temp_len -= 2
    if punc_bool:
            output_str += word[-1] + punc_char + " "
    elif word_len > 1:
            output_str += word[-1] + " "
    else: 
            output_str += " "
    return output_str

# Input and variables

file_input = input("Enter name of file: ")

# Main

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