class ArrayList:
    def __init__(self):
        self.__items = [None] * 10
        self.__size = 0

    def __len__(self):
        return self.__size

    def __getitem__(self, item):
        #
        return self.__items[item]

    def __setitem__(self, key, value):
        #
        self.__items[key] = value

    def pop(self, index):
       if index < self.__size - 1:
           for i in range(index, self.__size):
               self.__items[i] = self.__items[i + 1]

       self.__items[self.__size - 1] = None
       self.__size -= 1

    def append(self, element):
        if self.__size >= len(self.__items):
            self.__increase_capacity()

        self.__items[self.__size] = element
        self.__size += 1

    def increase_capacity(self):
        # увеличиваем длину массива в 2 раза
        self.__items = self.__items + [None] * len(self.__items)
