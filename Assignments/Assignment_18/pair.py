class Pair:
    def __init__(self, v1=0, v2=0):
        self.v1 = v1
        self.v2 = v2

    def __str__(self):
        return "Value 1: {}, Value 2: {}".format(self.v1, self.v2)

    def __add__(self, input_value):
        new_v1 = self.v1 + input_value.v1
        new_v2 = self.v2 + input_value.v2
        return Pair(new_v1, new_v2)


a = Pair(20,30)
print(a)    
b = Pair(40,50)
c = a + b
print(c)