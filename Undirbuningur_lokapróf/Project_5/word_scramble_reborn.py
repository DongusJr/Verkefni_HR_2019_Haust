import string

def open_file(file_name):
    try:
        return open(file_name, "r")
    except FileNotFoundError:
        print("File {} not found!".format(file_name))
        return None

def scramble_sentence(file_obj):
    scramble_sentence = ""
    for line in file_obj:
        has_punct = False
        word = line.strip()
        if len(word) < 4:
            scramble_sentence += word + " "
        else:
            word, punctuation = check_punctuation(word)
            if punctuation:
                has_punct = True
            
            scramble_sentence += word[0]
            k = 1
            while(k < len(word)-1):
                if k == len(word)-2:
                    scramble_sentence += word[k]
                else:
                    scramble_sentence += word[k+1] + word[k]
                k += 2
            scramble_sentence += word[-1]
            if has_punct:
                scramble_sentence += punctuation
            scramble_sentence += " "
    return scramble_sentence

def check_punctuation(word):
    if word[-1] in string.punctuation:
        punctuation = word[-1]
        word = word[:-1]
        return word, punctuation
    return word, None

def main():
    file_name = input("Enter name of file: ")
    file_obj = open_file(file_name)
    if file_obj:
        sentence = scramble_sentence(file_obj)
        print(sentence)


main()