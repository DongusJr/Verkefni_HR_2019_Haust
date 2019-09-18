import string

# Input and variables
file_input = input("Enter name of file: ")
output_str = ""
# Main
try:
    txt_file = open(file_input, "r")  # Open text file as read
    for line in txt_file:
        punc_bool = False  # Boolean that holds on if a line has a punctuation
        line = line.strip()  # Remove the \n from each line
        if line[-1] in string.punctuation:  #Check if the word has punctuation
            punc_char = line[-1]
            line = line[0: -1]
            punc_bool = True

        word_len = len(line)
        if word_len > 0:
            output_str += line[0]  # Add the first letter
        temp_len = word_len    # I use this variable for calculation of the scramble
        while(temp_len >= 3):  # While if temp_len is 2, then only the first and last letters are left
            if temp_len >=4:   # Check if you have two letters inbetween the first and last letter that you can scramble
                output_str += line[word_len - (temp_len - 2)] + line[word_len - (temp_len - 1)]
            else:              # Else there is only one letter to "scramble", add it
                output_str += line[-2]
            temp_len -= 2
        if punc_bool:          # If there is punctuation in the word, add it
            output_str += line[-1] + punc_char + " "
        elif word_len > 1:     # Else if add the last letter
            output_str += line[-1] + " "
        else:                  # If the word is only 1 letter long, only add an space    
            output_str += " "
    print(output_str)
    txt_file.close()  # Close the text file

except FileNotFoundError:   # If the file is not found
    print("File {} not found!".format(file_input))