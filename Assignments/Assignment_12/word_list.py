import string

def open_file(file_input):
    try:
        file_obj = open(file_input, "r")
        return file_obj
    except FileNotFoundError:
        print("File {} does not exist".format(file_input))
        return None

def get_word_list(file_obj):
    word_list = []
    for line in file_obj:
        line = line.strip().split()
        for word in line:
            word = check_punctuation(word)
            if word not in word_list:
                word_list.append(word)
    return sorted(word_list)

def check_punctuation(word):
    new_str = ""
    for letter in word:
        if letter not in string.punctuation or letter is "-":
            new_str += letter
    return new_str

file_input = input("Enter filename: ")
file_obj = open_file(file_input)
word_list = get_word_list(file_obj)
print(word_list)
