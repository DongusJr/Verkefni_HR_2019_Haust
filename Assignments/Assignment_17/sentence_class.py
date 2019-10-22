class Sentence():
    def __init__(self, sent_str=""):
        self.sent_list = sent_str.split(" ")

    def get_first_word(self):
        return self.sent_list[0]

    def get_all_words(self):
        return self.sent_list

    def replace(self, list_index, new_word):
        if 0 <= list_index <= len(self.sent_list):
            self.sent_list[list_index] = new_word
        else:
            pass
    

sent = Sentence('This is a test')
print(sent.get_first_word())
print(sent.get_all_words())
sent.replace(3, "must")
print(sent.get_all_words())
