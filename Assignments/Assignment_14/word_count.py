import string

def get_word_list(file_steam):
    sline = []
    for line in file_steam:
        sline += line.strip().split()
    return [item.strip(string.punctuation).lower() for item in sline]
        
def word_list_to_counts(word_list):
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

def dict_to_tuple(word_count_dict):
    return sorted(word_count_dict.items())

def main():
    filename = input("Name of file: ")
    # Get a file stream
    fstream = open(filename)
    # Get a list of words from the stream
    word_list = get_word_list(fstream) 
    fstream.close()
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuple(word_count_dict)
    print(sorted(word_count_tuples))
    
main()