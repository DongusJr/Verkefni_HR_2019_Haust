import string
from operator import itemgetter

def open_file(file_name):
    ''' Function that opens a file requested by the user, returns the file object '''
    try:
        return open(file_name, "r", encoding="utf-8")
    except FileNotFoundError:
        print("Filename {} not found!".format(file_name))
        return None

def make_word_list(file_obj):
    ''' Function that takes each line of the text file given and adds each word into a list '''
    word_list = []
    for line in file_obj:
        line = line.strip().split()  # Clear out whitespaces and newlines
        if line == []:  # If there is a new paragraph
            word_list += ["\n"] # Save this to for the paragraph index
        else:
            word_list += [word.strip(string.punctuation).lower() for word in line]  # Remove any punctuation at the start or end of the word
    return word_list

def get_sorted_paragraph_index(word_list):
    ''' Function that takes in the word list and returns a dictionary that tells you what paragraph each word was in '''
    paragraph_index_dict = {}
    paragraph_number = 1  # Start at paragraph number 1
    for word in word_list:
        if word == "\n":  # New paragraph
            paragraph_number += 1
            continue
        if word in paragraph_index_dict:
            paragraph_index_dict[word].add(paragraph_number) # This is a set so it wont double count any paragraph
        else:
            paragraph_index_dict[word] = {paragraph_number}  # If we haven't found this word already then add it and save paragraph in a set
    return paragraph_index_dict



def print_paragraph_index(paragraph_index_dict):
    ''' Function that prints out the paragraph index for each word in word list '''
    print("\nThe paragraph index:")
    for word, paragraphs in sorted(paragraph_index_dict.items()):  #  word, paragraph in [("...", number), ("...", number),...], sorted alphabeticaly
        print(word, end=" ")
        first_number = True  # Boolean to check if we need to print ", "
        for number in sorted(paragraphs):  # Sort the numbers
            if not first_number:  # If it is not the first number then print ", "
                print(", ", end="")
            print(number, end="")
            first_number = False
        print()

def get_highest_count(word_list):
    ''' Function that get's the highest count of certain words in word list '''
    highest_count_dict = {}
    for word in word_list:
        if word == "\n":  # Don't need to count a new paragraph
            continue
        if word in highest_count_dict:  # Add to count if it is already in the dictionary
            highest_count_dict[word] += 1
        else:                           # Initialize the count if it is not in the dictionary
            highest_count_dict[word] = 1
    return sorted(highest_count_dict.items())  # Sorted so it will print also in alphabetical order [("a", number), ("b", number), ...]

def print_highest_count(highest_count_dict, n):
    ''' Function that prints the higest numbers from a dictionary of word count, n represents how many words you want to print'''
    print("\nThe highest {} counts: ".format(n))
    # sort the higest_count_dir at index 1 to get the higest count, highest n numbers
    for word, count in sorted(highest_count_dict, key=itemgetter(1), reverse=True)[:n]:
        print("{}: {}".format(word, count))

def main():
    ''' Main function of this program '''
    file_name = input("Enter filename: ")
    file_obj = open_file(file_name)
    if file_obj:  # If it read the file
        word_list = make_word_list(file_obj)
        paragraph_index_dict = get_sorted_paragraph_index(word_list)
        highest_count_dict = get_highest_count(word_list)
        print_paragraph_index(paragraph_index_dict)
        print_highest_count(highest_count_dict, 10)  # Print top 10
        print_highest_count(highest_count_dict, 20)  # Print top 20

main()