class WholeNumber:
    def __init__(self, num=0):
        try:
            if num >= 0 and type(num) == int:
                self.__num = num
            else:
                self.__num = None
        except:
            self.__num = None

    def __str__(self):
        return str(self.__num)

    def __add__(self, other):
        if (self.__num != None) and (other.__num != None):
            return WholeNumber(self.__num + other.__num)
        return None

    def __mul__(self, other):
        if (self.__num != None) and (other.__num != None):
            return WholeNumber(self.__num * other.__num)
        return None

    def __sub__(self, other):
        if (self.__num != None) and (other.__num != None):
            return WholeNumber(self.__num - other.__num)
        return None

    