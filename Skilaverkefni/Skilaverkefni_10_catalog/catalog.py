class Item:
    def __init__(self, name="", category=""):
        ''' Initialize the class variables '''
        self.__name = name
        self.__category = category

    def __str__(self):
        ''' Print the name and category of the item '''
        return "Name: {}, Category: {}".format(self.__name, self.__category)

    def set_name(self, new_name):
        ''' Change the name of the item '''
        self.__name = new_name

    def set_category(self, new_category):
        ''' Change the category of the item '''
        self.__category = new_category

class Catalog:
    def __init__(self, name="", collection = []):
        ''' Initialize the name for the catalog '''
        self.__name = name
        self.__collection = collection  # List that saves the items in catalog

    def add(self, item):
        ''' Add an item to the catalog '''
        self.__collection.append(item)

    def remove(self, item):
        ''' Remove an item from the catalog '''
        self.__collection.remove(item)

    def set_name(self, name=""):
        ''' Change name of the catalog '''
        self.__name = name

    def find_item_by_name(self, name=""):
        ''' Find an item by their name and return the string version of that item '''
        for item in self.__collection:
            if name in str(item):  # If the name is in "Name: {NAME}, Category: {CATGORY}"
               return str(item)
        return None  # If the item is not in the catalog

    def clear(self):
        ''' clear the catalog '''
        self.__collection.clear()

    def __str__(self):
        ''' Print the name of catalog and it's items '''
        catalog_str = "Catalog {}:".format(self.__name)
        for item in self.__collection:
            catalog_str += ("\n\t" + str(item))  # Get the item string from the Item class
        return catalog_str
