class StringSet:
    def __init__(self, input_str):
        self.__words = []
        for word in input_str.strip().split():  # For each word in user input sentence
            if word not in self.__words:  # check if the word is unique
                self.__words.append(word)

    def __str__(self):
        return_str = ""
        for word in self.__words:
            return_str += word + " "
        return return_str.strip()

    def __add__(self, other):
        ''' Union of the two sets '''
        union_set_str = ""
        for word in self.__words:
            if word not in union_set_str:  # Check if it is unique
                union_set_str += word + " "

        for word in other.__words:
            if word not in union_set_str:  # Check if it is unique
                union_set_str += word + " "
        return StringSet(union_set_str)

    def size(self):
        ''' returns the size of the set '''
        return len(self.__words)

    def at(self, index_num):
        ''' returns the value at a certain index '''
        return self.__words[index_num]

    def find(self, word):
        ''' returns a boolean value depending on wheter a certain word is in the set '''
        try:
            if self.__words.index(word):
                return True
        except:
            return False


def main():
    str1 = 'chocolate ice cream and chocolate candy ice bars are my favorite'
    set1 = StringSet(str1)
    str2 = 'I like to eat broccoli and fish and ice cream and brussel fish sprouts'
    set2 = StringSet(str2)
    print("Set1:", set1)
    print("Set2:", set2)
    print("Set1 size:", set1.size())
    print("Set2 size:", set2.size())
    the_union = set1 + set2
    print("Union:", the_union)
    print("Union size:", the_union.size())

    query = StringSet('chocolate cream fish good rubbish')
    print("Query:", query)
    count = 0
    for i in range(query.size()):
        if the_union.find(query.at(i)) != False:
            count += 1
    
    print("Query size:", query.size())
    print("Found in union:", count)

    set1 = StringSet('word1 word2 word3 word2 word1 word4')
    set2 = StringSet('word2 word5 word4 word6 word7 word3')
    set3 = set1 + set2
    print(set3)

    set1 = StringSet('word1 word2 word3 word2')

    print(set1)
main()
    