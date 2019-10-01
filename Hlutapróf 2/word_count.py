def get_input():
    ''' Function that returns the user input for a filename '''
    file_name = input("Enter filename: ")
    return file_name

def make_list(file_name):
    ''' Function that makes a list of all the words in the given text file '''
    word_list = []
    try:
        with open(file_name, "r") as words:  # Open, read, work with it, then close the file
            for line in words:  # for each line in the .txt
                line = line.strip().split()  # remove whitespace and newline
                for word in line:  # for each word in line
                    word_list.append(word)
        return word_list

    except FileNotFoundError:
        print("File {} not found!".format(file_name))
        return None

def count_words(word_list):
    ''' Function that counts words in a given list '''
    word_count = 0
    for word in word_list: # Iterate through each word and count it
        word_count += 1  
        if check_punctuation(word):  # Check if there is punctuation in the end of the string
            word_count += 1
    return word_count

def check_punctuation(word):
    ''' Function that checks if a string has a punctuation at the end of it '''
    punctuation_str = ",.!?"
    if word[-1] in punctuation_str: # If the last character is {,.!?}
        return True

        
    return False

def main():
    ''' Main function for this program '''
    file_name = get_input()
    word_list = make_list(file_name)
    if word_list != None:
        word_count = count_words(word_list)
        print(word_count)

main()