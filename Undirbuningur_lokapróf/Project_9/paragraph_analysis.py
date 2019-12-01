import string
from operator import itemgetter

def open_file(file_name):
    try:
        return open(file_name, "r", encoding="utf-8")
    except FileNotFoundError:
        print("Filename {} not found!".format(file_name))
        return None

def make_word_list(file_obj):
    word_list = []
    par_list = []
    for line in file_obj:
        if line == "\n":
            word_list.append(par_list)
            par_list = []
        else:
            par_list += [word.strip(string.punctuation).lower() for word in line.strip().split(" ")]
    word_list.append(par_list)
    for i in range(len(word_list)):
        word_list[i].remove("")
    return word_list
        

def make_paragraph_index(word_list):
    paragraph_index = {}
    for i, paragraph in enumerate(word_list):
        for word in paragraph:
            if word in paragraph_index:
                paragraph_index[word].add(i+1)
            else:
                paragraph_index[word] = {i+1}
    return paragraph_index

def make_count_dict(word_list):
    count_dict = {}
    for paragraph in word_list:
        for word in paragraph:
            if word in count_dict:
                count_dict[word] += 1
            else:
                count_dict[word] = 1
    return count_dict

def print_highest_counts(count_dict, n):
        print("\nThe highest {} counts".format(n))
        for word, count in sorted(sorted(count_dict.items()), key=itemgetter(1), reverse=True)[:n]:
            print("{}: {}".format(word, count))


def print_results(paragraph_index, count_dict):
    print("\nThe paragraph index:")
    for word, indexes in sorted(paragraph_index.items()):
        sort_index = sorted(indexes)
        print(word, end=" ")
        for item in sort_index:
            if item != sort_index[-1]:
                print(item, end=", ")
            else:
                print(item)

    print_highest_counts(count_dict, 10)
    print_highest_counts(count_dict, 20)



def main():
    file_name = input("Enter filename: ")
    file_obj = open_file(file_name)
    if file_obj:
        word_list = make_word_list(file_obj)
        file_obj.close()
        paragraph_index = make_paragraph_index(word_list)
        count_dict = make_count_dict(word_list)
        print_results(paragraph_index, count_dict)

main()