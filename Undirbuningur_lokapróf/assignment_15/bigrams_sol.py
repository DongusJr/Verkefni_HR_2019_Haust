from operator import itemgetter
import string

def open_file(file_name):
    return open(file_name, "r")

def make_word_list(file_obj):
    word_list = []
    for line in file_obj:
        line_strip = line.strip().split()
        for word in line_strip:
            word = word.strip(string.punctuation)
            word_list.append(word.lower())
    return word_list

def count_bigrams(word_list):
    bigram_dict = {}
    for i in range(len(word_list) - 1):
        bigram_tuple = (word_list[i], word_list[i+1])
        if bigram_tuple in bigram_dict:
            bigram_dict[bigram_tuple] += 1
        else:
            bigram_dict[bigram_tuple] = 1
    return bigram_dict
        

def main():
    file_name = input("Enter name of file: ")
    file_obj = open_file(file_name)
    word_list = make_word_list(file_obj)
    bigram_dict = count_bigrams(word_list)
    a_list = sorted(bigram_dict.items(), key=itemgetter(1), reverse=True)
    print(a_list[:10])
main()

