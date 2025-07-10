class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def set_mines_count(self):
        mines_count = self.view.get_mines_count()

        try:
            self.model.set_mines_count(mines_count)

            try:
                self.view.display_mines_count(str(self.model.get_mines_count()))
            except ValueError:
                print("Переменная mines_count не является числом")
        except ValueError:
            print("Переменная mines_count не является числом")

    def set_field_size(self):
        field_size = self.view.get_field_size()
        self.model.set_field_size(field_size)
        self.view.display_field_size(str(self.model.get_field_size()))
