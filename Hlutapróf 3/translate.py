import string
QUIT = "q"

def open_file(file_name):
    ''' Function that opens the textfile given by user '''
    try:
        return open(file_name, "r")
    except FileNotFoundError:  # Incase of faulty input
        return None

def make_abbrev_dict(file_obj):
    ''' Function that makes a dictionary for the abbreviations
        Keys are the abbreviations and values are their translations '''
    abbrev_dict = {}
    for line in file_obj:
        abbrev, translation = line.strip().split(":")  # Remove white space and get the key and value
        abbrev_dict[abbrev] = translation
    return abbrev_dict

def change_sentence(user_sentence, abbrev_dict, punct_bool = False):
    ''' Function that translates the sentence of abbreviations
        and returns a string of the new sentence '''
    if user_sentence[-1] in string.punctuation:  # If the word has a punctuation
        punct = user_sentence[-1]
        user_sentence = user_sentence[:-1]  # Slice it without the punc
        punct_bool = True  # Save it
    new_sentence = ""
    for word in user_sentence.split(" "):
        if word in abbrev_dict:  # If the word is in the dictionary then we add the translation to the string along with a space
            new_sentence += abbrev_dict[word] + " "
        else:  # Else we keep the word unchanged with a space
            new_sentence += word + " "
    if punct_bool:  # If the sentece had punctuation, add it
        new_sentence = new_sentence.strip() + punct  # strip to remove the whitespace of the last word for the punct
    return new_sentence
    
def main():
    ''' Main function of this program '''
    file_name = input("Enter name of mapping file: ")
    file_obj = open_file(file_name)
    if file_obj:  # If it is not None
        abbrev_dict = make_abbrev_dict(file_obj)

        user_sentence = input("Enter a message: ")  
        while user_sentence != QUIT:  # Loop that consists of getting user input and translating the input
            new_sentence = change_sentence(user_sentence, abbrev_dict)
            print(new_sentence)
            user_sentence = input("Enter a message: ")  # Loop controlled, q to Quit

main()