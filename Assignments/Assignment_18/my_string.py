class MyString:
    def __init__(self, user_str=""):
        self.user_str = user_str

    def __gt__(self, another_str):
        if len(self.user_str) > len(another_str.user_str):
            return True
        else:
            return False

    def __sub__(self, another_str):
        return abs(len(self.user_str) - len(another_str.user_str)) 

obj1 = MyString('this is a string')
obj2 = MyString('this is another one')
print(obj1 > obj2)
print(obj1-obj2)