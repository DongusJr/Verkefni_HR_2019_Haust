from operator import itemgetter
import string

def open_file(file_name):
    try:
        return open(file_name, "r")
    except FileNotFoundError:
        return None

def make_word_list(file_obj):
    word_list = []
    for line in file_obj:
        line = line.strip().split(" ")
        for word in line:
            word_list.append(word.strip(string.punctuation).lower())
    return word_list

def make_bigram_dict(word_list):
    bigram_dict = {}
    for i in range(len(word_list) - 1):
        bigram = (word_list[i], word_list[i+1])
        if bigram in bigram_dict:
            bigram_dict[bigram] += 1
        else:
            bigram_dict[bigram] = 1
    return bigram_dict

def print_dict(bigram_dict):
    top_list = sorted(bigram_dict.items(), key=itemgetter(1), reverse=True)
    print(top_list[:10])

def main():
    file_name = input("Enter filename: ")
    file_obj = open_file(file_name)
    if file_obj:
        word_list = make_word_list(file_obj)
        bigram_dict = make_bigram_dict(word_list)
        print_dict(bigram_dict)

main()