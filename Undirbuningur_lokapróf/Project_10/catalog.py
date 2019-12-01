class Catalog:
    def __init__(self, name = "", collection = None):
        self.__name = name
        self.__collection = []
    
    def __str__(self):
        out_str = "Catalog {}:".format(self.__name)
        for item in self.__collection:
            out_str += "\n\t{}".format(str(item))
        return out_str

    def add(self, item):
        self.__collection.append(item)

    def remove(self, item):
        self.__collection.remove(item)

    def set_name(self, name):
        self.__name = name
        
    def find_item_by_name(self, user_item):
        for item in self.__collection:
            if user_item in str(item):
                return str(item)
        return None

    def clear(self):
        self.__collection.clear()

class Item:
    def __init__(self, name = "", category = ""):
        self.__name = name
        self.__category = category

    def __str__(self):
        return "Name: {}, Category: {}".format(self.__name, self.__category)

    def set_name(self, name):
        self.__name = name

    def set_category(self, category):
        self.__category = category

