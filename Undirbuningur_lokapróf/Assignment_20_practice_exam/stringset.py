class StringSet:
    def __init__(self, input_str):
        self.str_set = []
        for word in input_str.split(" "):
            if word not in self.str_set:
                self.str_set.append(word)

    def __str__(self):
        out_str = ""
        for word in self.str_set:
            out_str += word + " "
        return out_str.strip()

    def size(self):
        return len(self.str_set)

    def __add__(self, other):
        new_set = []
        for word in self.str_set:
            new_set.append(word)
        for word in other.str_set:
            if word not in new_set:
                new_set.append(word)
        return StringSet(str(new_set))

    def at(self, index_num):
        ''' returns the value at a certain index '''
        return self.str_set[index_num]

    def find(self, word):
        ''' returns a boolean value depending on wheter a certain word is in the set '''
        try:
            if self.str_set.index(word):
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
        if the_union.find(query.at(i)):
            count += 1
    
    print("Query size:", query.size())
    print("Found in union:", count)

main()