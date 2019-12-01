import string

def open_file(file_name):
    try:
        return open(file_name, "r")
    except FileNotFoundError:
        print("File {} not found!".format(file_name))


def scramble_words(file_obj):
    scramble_sentence = ""
    for word in file_obj:
        word = word.strip("\n")
        has_punc = False
        if len(word) < 4:
            scramble_sentence += word + " "
        else:
            if word[-1] in string.punctuation:
                punct_char = word.pop()
                has_punc = True
            scramble_sentence += word[0]
            k = len(word) - 2
            while(k > 0):
                if k > 1:
                    scramble_sentence += word[len(word) - k - 1] + word[len(word) - k]
                if k == 1:
                    scramble_sentence = word[len(word)-k]
                k -= 2
            if has_punc:
                scramble_sentence += punct_char
            scramble_sentence += " "
    return scramble_sentence
            



def main():
    file_name = input("Enter name of file: ")
    file_obj = open_file(file_name)
    if file_obj:
        scramble_sentence = scramble_words(file_obj)
        print(scramble_sentence)

main()