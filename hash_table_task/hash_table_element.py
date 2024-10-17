class HashTableElement:
    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    def __repr__(self):
        return "{" + f"{self.__key}: {self.__value}" + "}"
