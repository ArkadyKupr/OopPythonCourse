class Model:
    def __init__(self):
        self.__mines_count = 0
        self.__field_size = 0

    def set_field_size(self, field_size):
        try:
            int(field_size)
        except ValueError:
            self.__field_size = 10
        else:
            self.__field_size = field_size

    def get_field_size(self):
        return self.__field_size

    def set_mines_count(self, mines_count):
        try:
            int(mines_count)
        except ValueError:
            self.__mines_count = 9
        else:
            if int(self.get_field_size()) * int(self.get_field_size()) <= int(mines_count):
                self.__mines_count = mines_count
            else:
                self.__mines_count = 9

    def get_mines_count(self):
        return self.__mines_count
