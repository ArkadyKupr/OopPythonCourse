import tkinter
from tkinter import *
from tkinter import ttk
import random
from PIL import Image, ImageTk
import datetime
from tkinter.messagebox import showinfo


class Model:
    def __init__(self):
        self.mines_count = 0
        self.field_size = 0

    def set_field_size(self, field_size):
        try:
            int(field_size)
        except ValueError:
            self.field_size = 9
        else:
            self.field_size = field_size

    def get_field_size(self):
        return self.field_size

    def set_mines_count(self, mines_count):
        try:
            int(mines_count)
        except ValueError:
            self.mines_count = 10
        else:
            if int(self.get_field_size()) * int(self.get_field_size()) <= int(mines_count):
                self.mines_count = mines_count
            else:
                self.mines_count = 10

    def get_mines_count(self):
        return self.mines_count


class ViewSecondaryHighScores(tkinter.ttk.Frame):
    def __init__(self, master=None, parent=None):
        super().__init__(master)
        frame_1 = tkinter.ttk.Frame(self)
        self.frame_2 = tkinter.ttk.Frame(self)

        frame_1.pack()
        self.frame_2.pack()

        self.parent = parent

        self.show_record_table()

        self.master.title("High Scores")
        self.master.resizable(False, False)
        self.pack()

        self.focus_set()

    def show_record_table(self):
        with open("output.txt", "r", encoding="utf-8") as file:
            lines = [line.rstrip() for line in file]

        k = 0

        for i in range(3):
            for j in range(3):
                if k < len(lines):
                    self.name_and_time_record_button = ttk.Button(self.frame_2, text=f"{k + 1}. {lines[k]}", width=30)
                    self.name_and_time_record_button.grid(row=j, column=i)

                    k += 1
                else:
                    self.name_and_time_record_button = ttk.Button(self.frame_2, text=f" ", width=30)
                    self.name_and_time_record_button.grid(row=j, column=i)


class ViewSecondaryAbout(tkinter.ttk.Frame):
    def __init__(self, master=None, parent=None):
        super().__init__(master)
        frame = tkinter.ttk.Frame(self)
        frame.pack()

        self.parent = parent
        self.label = ttk.Label(frame, text="Это игра \"Minesweeper\" была создана в рамках курса \"ООП Python\"")
        self.label.pack()

        self.master.title("About")
        self.master.resizable(True, True)
        self.master.minsize(300, 200)
        self.master.maxsize(1200, 800)
        self.pack()

        self.focus_set()


class View(tkinter.ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.frame_1 = tkinter.ttk.Frame(self)
        frame_2 = tkinter.ttk.Frame(self)
        self.frame_3 = tkinter.ttk.Frame(self)
        frame_4 = tkinter.ttk.Frame(self)

        self.frame_1.pack()
        frame_2.pack()
        self.frame_3.pack()
        frame_4.pack()

        self.mines_count = tkinter.StringVar()
        self.field_size = tkinter.StringVar()

        # добавка label, связанного с количеством мин
        self.mines_count_label = ttk.Label(self.frame_1, text="Количество мин:", width=16)
        self.mines_count_label.pack(side="left", padx=10, pady=20)

        # добавка  виджета Entry и привязка к нему переменной - mines_count
        self.mines_count_entry = ttk.Entry(self.frame_1, textvariable=self.mines_count, width=10)
        self.mines_count_entry.pack(side="left", padx=10, pady=20)

        # поддержка таблицы рекордов
        self.gamer_name = tkinter.StringVar()

        self.gamer_name_entry = ttk.Entry(self.frame_1, textvariable=self.gamer_name)
        self.gamer_name_entry.pack(side="right", padx=10, pady=20)

        self.gamer_name_label = ttk.Label(self.frame_1, text=" Пользователь:", width=15)
        self.gamer_name_label.pack(side="right", padx=10, pady=20)

        # добавка  виджета Entry и привязка к нему переменной - size
        self.field_size_entry = ttk.Entry(self.frame_1, textvariable=self.field_size, width=10)
        self.field_size_entry.pack(side="right", padx=10, pady=20)

        # добавка label, связанного с шириной поля
        self.size_label = ttk.Label(self.frame_1, text="Ширина поля:", width=15)
        self.size_label.pack(side="right", padx=20, pady=20)

        # добавка  кнопки "About"
        self.about_button = ttk.Button(frame_2, text="About", command=self.show_window_about)
        self.about_button.pack(side="right", padx=20, pady=20)

        # добавка  кнопки "Exit"
        self.exit_button = ttk.Button(frame_2, text="Exit", command=self.destroy)
        self.exit_button.pack(side="right", padx=20, pady=20)

        # добавка  кнопки "High Scores"
        self.high_scores_button = ttk.Button(frame_2, text="High Scores", command=self.show_window_high_scores)
        self.high_scores_button.pack(side="right", padx=20, pady=20)

        # добавка "кнопки создания поля и расстановки мин" и привязка к нему события
        self.new_game_button = ttk.Button(frame_2, text="New Game")
        self.new_game_button.pack(side="right", padx=20, pady=20)

        self.new_game_button.bind("<Button>", lambda event: self.delete_field())
        self.new_game_button.bind("<Button>", lambda event: self.check_mines_count_and_field_size(), add="+")
        self.new_game_button.bind("<Button>", lambda event: self.create_field(), add="+")

        # блок кода для подсчета времени, потраченного на окончание игры с выигрышом
        self.start_seconds = tkinter.IntVar()
        self.new_game_button.bind("<Button>", lambda event: self.start_seconds.set(self.time_count()), add="+")

        self.end_seconds = tkinter.IntVar()
        self.game_time = tkinter.StringVar()

        # переменная, в которую записываетя True при первом нажатии любой кнопки в поле
        self.first_press_on_any_button = tkinter.BooleanVar()
        self.first_press_on_any_button.set(True)

        # создание переменной количества открытых клеточек поля для выведения сообщения о выигрыше
        self.opened_buttons_quantity = tkinter.IntVar()

        # создание переменных, ответственных за вторичное изменение размера поля:
        # self.game_already_launched - переменная, показывающая, что до этого момента как минимум одна игра была сыграна
        # self.previous_game_field_size - переменная, в которую записывается значение размера поля
        # предыдущей сыгранной игры
        self.game_already_launched = tkinter.BooleanVar()
        self.game_already_launched.set(False)

        self.previous_game_field_size = tkinter.StringVar()

        # Создание кнопок в поле
        self.buttons = [[None for _ in range(1)] for _ in range(1)]

        # установка контроллера
        self.controller = None

        self.mines_matrix = []

    # проверка, что переменные: размеры поля - field_size, и количество мин - mines_count, были int
    def check_mines_count_and_field_size(self):
        try:
            int(self.mines_count.get())
        except ValueError:
            self.mines_count.set("10")

        try:
            int(self.field_size.get())
        except ValueError:
            self.field_size.set("9")

        # проверка, что размеры поля - field_size, соответствовали mines_count
        if int(self.field_size.get()) * int(self.field_size.get()) < int(self.mines_count.get()):
            self.field_size.set("9")
            self.mines_count.set("10")

    def set_controller(self, controller):
        self.controller = controller

    def save_button_clicked(self):
        if self.controller:
            self.controller.set_mines_count()

    def prompt_for_mines_count(self):
        return self.mines_count.get()

    def display_mines_count(self, mines_count):
        self.mines_count.set(str(mines_count))

    def prompt_for_field_size(self):
        return self.field_size.get()

    def display_field_size(self, field_size):
        self.field_size.set(str(field_size))

    # функция для подсчета времени, потраченного на заканчивание игры с выигрышом
    def time_count(self):
        then = datetime.datetime(2025, 2, 5, 19, 27, 0)
        start = datetime.datetime.now()
        delta = start - then
        return int(delta.total_seconds())

    # функция для создания матрицы мин. Срабатывает при первом нажатии на кнопку в поле grid
    def create_mines_matrix(self, row, col):
        matrix_size = int(self.field_size.get())
        mines_count = int(self.mines_count.get())

        current_mines_quantity = 0

        self.mines_matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

        last_index = int(matrix_size) - 1

        while current_mines_quantity < mines_count:
            i = random.randint(0, last_index)
            j = random.randint(0, last_index)

            if self.mines_matrix[i][j] != 1:
                self.mines_matrix[i][j] = 1

                current_mines_quantity += 1

        return self.mines_matrix

    # функция для создания матрицы количества соседних мин
    def create_neighbour_mines_quantity_matrix(self):
        matrix_size = len(self.mines_matrix)

        neighbour_mines_quantity_matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

        for i in range(matrix_size):
            for j in range(matrix_size):
                if i == 0 and j == 0:
                    neighbour_mines_quantity_matrix[0][0] = self.mines_matrix[0][1] + self.mines_matrix[1][1] + \
                                                                self.mines_matrix[1][0]
                elif i == 0 and j == matrix_size - 1:
                    neighbour_mines_quantity_matrix[0][matrix_size - 1] = (self.mines_matrix[0][matrix_size - 2] +
                                                                           self.mines_matrix[1][matrix_size - 2] +
                                                                           self.mines_matrix[1][matrix_size - 1])
                elif i == matrix_size - 1 and j == 0:
                    neighbour_mines_quantity_matrix[matrix_size - 1][0] = (self.mines_matrix[matrix_size - 2][0] +
                                                                           self.mines_matrix[matrix_size - 2][1] +
                                                                           self.mines_matrix[matrix_size - 1][0])
                elif i == matrix_size - 1 and j == matrix_size - 1:
                    neighbour_mines_quantity_matrix[matrix_size - 1][matrix_size - 1] = (
                                self.mines_matrix[matrix_size - 2][matrix_size - 1] +
                                self.mines_matrix[matrix_size - 2][matrix_size - 2] +
                                self.mines_matrix[matrix_size - 1][matrix_size - 2])
                elif j == 0:
                    neighbour_mines_quantity_matrix[i][0] = (self.mines_matrix[i - 1][0] +
                                                             self.mines_matrix[i - 1][1] + self.mines_matrix[i + 1][0] +
                                                             self.mines_matrix[i + 1][1] + self.mines_matrix[i][1])
                elif i == 0:
                    neighbour_mines_quantity_matrix[0][j] = (self.mines_matrix[0][j + 1] + self.mines_matrix[0][j - 1] +
                                                             self.mines_matrix[1][j + 1] + self.mines_matrix[1][j - 1] +
                                                             self.mines_matrix[1][j])
                elif j == matrix_size - 1:
                    neighbour_mines_quantity_matrix[i][matrix_size - 1] = (self.mines_matrix[i - 1][matrix_size - 1] +
                                                                           self.mines_matrix[i - 1][matrix_size - 2] +
                                                                           self.mines_matrix[i + 1][matrix_size - 1] +
                                                                           self.mines_matrix[i + 1][matrix_size - 2] +
                                                                           self.mines_matrix[i][matrix_size - 2])
                elif i == matrix_size - 1:
                    neighbour_mines_quantity_matrix[matrix_size - 1][j] = (self.mines_matrix[matrix_size - 1][j + 1] +
                                                                           self.mines_matrix[matrix_size - 1][j - 1] +
                                                                           self.mines_matrix[matrix_size - 2][j + 1] +
                                                                           self.mines_matrix[matrix_size - 2][j - 1] +
                                                                           self.mines_matrix[matrix_size - 2][j])
                else:
                    neighbour_mines_quantity_matrix[i][j] = (self.mines_matrix[i][j + 1] + self.mines_matrix[i][j - 1] +
                                                             self.mines_matrix[i - 1][j + 1] + self.mines_matrix[i - 1][
                                                                     j - 1] +
                                                             self.mines_matrix[i - 1][j] + self.mines_matrix[i + 1][j + 1] +
                                                             self.mines_matrix[i + 1][j - 1] + self.mines_matrix[i + 1][j])

        return neighbour_mines_quantity_matrix

    # функция создания поля, которая вызывается при нажании кнопки "New Game"
    def create_field(self):
        # запись в  переменную self.previous_game_field_size значения размера поля текущей игры
        self.previous_game_field_size.set(self.field_size.get())

        field_size = int(self.field_size.get())

        # создание 3 матриц для tkinter переменных, в которые будут записаны значения из матриц:
        # 1) значения из матрицы мин,
        # 2) значения из матрицы количества соседних мин,
        # 3) значения из матрицы посещенных кнопок (чтобы не превышать дозволенного числа вызовов рекурсивной функции)
        mines_values_matrix = [[None for _ in range(field_size)] for _ in range(field_size)]
        neighbour_mines_quantity_values_matrix = [[None for _ in range(field_size)] for _ in range(field_size)]
        visited_buttons_values_matrix = [[None for _ in range(field_size)] for _ in range(field_size)]

        self.first_press_on_any_button.set(True)

        for row in range(field_size):
            for col in range(field_size):
                mines_values_matrix[row][col] = tkinter.StringVar()
                neighbour_mines_quantity_values_matrix[row][col] = tkinter.StringVar()
                visited_buttons_values_matrix[row][col] = tkinter.BooleanVar()

        # открытие картинки мины и флага
        mine = Image.open(r".\mine.png")
        resized_mine = mine.resize((15, 15))
        mine_picture = ImageTk.PhotoImage(resized_mine)

        flag = Image.open(r".\flag.png")
        resized_flag = flag.resize((15, 15))
        flag_picture = ImageTk.PhotoImage(resized_flag)

        # создание матрицы кнопок в поле
        self.buttons = [[None for _ in range(field_size)] for _ in range(field_size)]

        for row in range(field_size):
            for col in range(field_size):
                self.buttons[row][col] = ttk.Button(self.frame_3,
                                               text=" ",
                                               width=3,
                                               command=lambda row=row, col=col: show_content(row, col))

                self.buttons[row][col].grid(row=row, column=col, sticky=NSEW)

        def show_content(row, col):
            if self.first_press_on_any_button.get() is True:
                self.first_press_on_any_button.set(False)

                self.buttons[row][col].bind("<Button>", create_matrixes(row, col))
                self.buttons[row][col].bind("<Button>", show_field_on_first_press_of_button(row, col))
            else:
                if int(mines_values_matrix[row][col].get()) == 1:
                    showinfo("Сообщение", "Вы проиграли!")
                    self.game_already_launched.set(True)

                    # отображение всех мин и оставшихся флагов
                    show_all_mines_and_rest_flags()

                if int(mines_values_matrix[row][col].get()) == 0 and not visited_buttons_values_matrix[row][
                        col].get():
                    self.buttons[row][col].bind("<Button>", show_field_on_first_press_of_button(row, col))

        # увеличение количества посещенных клеток при посещении новой клетки
        def increase_visited_buttons_quantity(buttons_quantity):
            return buttons_quantity + 1

        # проверка количества посещенных клеток, чтобы поймать момент выигрыша
        def check_visited_buttons_quantity():
            self.opened_buttons_quantity.set(0)

            for i in range(field_size):
                for j in range(field_size):
                    if visited_buttons_values_matrix[i][j].get():
                        self.opened_buttons_quantity.set(
                                increase_visited_buttons_quantity(self.opened_buttons_quantity.get()))

            # выведение сообщения о выигрыше
            if self.opened_buttons_quantity.get() == field_size * field_size - int(self.mines_count.get()):
                showinfo("Сообщение", "Вы выиграли!")

                self.game_already_launched.set(True)

                # отображение всех мин и оставшихся флагов
                show_all_mines_and_rest_flags()

                # подсчет времени окончания игры для последующей записи в таблицу рекордов
                self.end_seconds.set(self.time_count())
                self.game_time.set(str(self.end_seconds.get() - self.start_seconds.get()))

                # запись имени и времени игры в таблицу рекордов
                self.write_gamer_record(self.gamer_name.get(), self.game_time.get())
                self.read_gamer_name()

            return self.opened_buttons_quantity.get()

        # отображение количества мин в соседних клетках в квадрате 3х3
        def show_quantity_of_neighbour_mines(row, col):
            self.buttons[row][col].configure(text=neighbour_mines_quantity_values_matrix[row][col].get())
            self.buttons[row][col].unbind("<Button>")

            visited_buttons_values_matrix[row][col].set(True)

        # отображение количества мин в соседних клетках в квадрате размером 3х3
        # функция применяется, если в клетке нет мины
        def show_zero(row, col):
            if int(neighbour_mines_quantity_values_matrix[row][col].get()) == 0:
                if not visited_buttons_values_matrix[row][col].get():
                    self.buttons[row][col]["image"] = flag_picture
                    return show_field_on_first_press_of_button(row, col)
            else:
                show_quantity_of_neighbour_mines(row, col)

        # раскрытие поля при первом нажатии кнопки
        def show_field_on_first_press_of_button(row, col):
            field_size = int(self.field_size.get())

            if int(neighbour_mines_quantity_values_matrix[row][col].get()) == 0:
                visited_buttons_values_matrix[row][col].set(True)

                self.buttons[row][col]["image"] = flag_picture

                if row == field_size - 1 and col == field_size - 1:
                    show_zero(row, col - 1)
                    show_zero(row - 1, col - 1)
                    show_zero(row - 1, col)
                elif row == field_size - 1 and col == 0:
                    show_zero(row, 1)
                    show_zero(row - 1, 0)
                    show_zero(row - 1, col + 1)
                elif row == 0 and col == 0:
                    show_zero(0, col + 1)
                    show_zero(row + 1, col)
                    show_zero(row + 1, col + 1)
                elif row == 0 and col == field_size - 1:
                    show_zero(row, col - 1)
                    show_zero(row + 1, col)
                    show_zero(row + 1, col - 1)
                elif row == 0:
                    show_zero(row, col - 1)
                    show_zero(row, col + 1)
                    show_zero(row + 1, col)
                    show_zero(row + 1, col - 1)
                    show_zero(row + 1, col + 1)
                elif col == 0:
                    show_zero(row, col + 1)
                    show_zero(row - 1, col)
                    show_zero(row - 1, col + 1)
                    show_zero(row + 1, col)
                    show_zero(row + 1, col + 1)
                elif row == field_size - 1:
                    show_zero(row, col + 1)
                    show_zero(row, col - 1)
                    show_zero(row - 1, col)
                    show_zero(row - 1, col + 1)
                    show_zero(row - 1, col - 1)
                elif col == field_size - 1:
                    show_zero(row, col - 1)
                    show_zero(row - 1, col)
                    show_zero(row - 1, col - 1)
                    show_zero(row + 1, col)
                    show_zero(row + 1, col - 1)
                else:
                    show_zero(row + 1, col + 1)
                    show_zero(row + 1, col - 1)
                    show_zero(row + 1, col)
                    show_zero(row, col + 1)
                    show_zero(row, col - 1)
                    show_zero(row - 1, col)
                    show_zero(row - 1, col + 1)
                    show_zero(row - 1, col - 1)
            else:
                show_quantity_of_neighbour_mines(row, col)

        # раскрытие игрового поля
        def show_all_mines_and_rest_flags():
            for row in range(field_size):
                for col in range(field_size):
                    if int(mines_values_matrix[row][col].get()) == 1:
                        self.buttons[row][col]["image"] = mine_picture

                    if not visited_buttons_values_matrix[row][col].get() and int(
                            mines_values_matrix[row][col].get()) == 0:
                        self.buttons[row][col]["image"] = flag_picture

                    self.buttons[row][col].unbind("<Button>")

        # создание матриц: матрицы мин и матрицы количества мин в соседних клетках в квадрате 3х3
        def create_matrixes(row, col):
            mines_matrix = self.create_mines_matrix(row, col)
            neighbour_mines_quantity_matrix = self.create_neighbour_mines_quantity_matrix()

            # вывод матрицы mines_matrix для проверки, что выигрыш работает
            print("Сгенерированная матрица расположения мин:")
            print(mines_matrix)

            for row in range(int(self.field_size.get())):
                for column in range(int(self.field_size.get())):
                    mines_values_matrix[row][column].set(self.mines_matrix[row][column])
                    neighbour_mines_quantity_values_matrix[row][column].set(
                            neighbour_mines_quantity_matrix[row][column])

    # запись записи о выигрыше: имени и времени в секундах, в файл
    def write_gamer_record(self, gamer_name, game_time):
        with open("output.txt", "a", encoding="utf-8") as file:
            file.write(gamer_name + " " + game_time)

        with open("output.txt", "r", encoding="utf-8") as file, open("copy.txt", "w",
                                                                     encoding="utf-8") as copy_file:
            copy_file.write(file.read())

        self.read_gamer_name()

    # чтение из файла, сортировка записей о выигрыше, перезапись отсортированных записей в файл
    def read_gamer_name(self):
        with open("copy.txt", "r", encoding="utf-8") as copy_file, open("output.txt", "w",
                                                                        encoding="utf-8") as file:
            lines = [line.rstrip() for line in copy_file]

            counts = []

            for i in range(0, len(lines)):
                index = lines[i].rfind(" ")
                if index != -1:
                    count = lines[i][index::]
                    counts.append(int(count))

            self.bubble_sort(counts, lines)

            for i in range(len(lines)):
                file.write(lines[i] + "\r")

    # сортировка записей из файла с записями рекордов
    def bubble_sort(self, counts, lines):
        for i in range(len(counts) - 1):
            is_exchanged = False

            for j in range(len(counts) - 1 - i):
                if counts[j] > counts[j + 1]:
                    lines[j], lines[j + 1] = lines[j + 1], lines[j]
                    counts[j], counts[j + 1] = counts[j + 1], counts[j]
                    is_exchanged = True

            if not is_exchanged:
                return

    # удаление игрового поля при перезапуске игры при нажатии кнопки "New Game"
    def delete_field(self):
        if self.game_already_launched.get() is True:
            field_size = int(self.previous_game_field_size.get())

            for row in range(field_size):
                for col in range(field_size):
                    self.buttons[row][col].destroy()

    def show_window_high_scores(self):
        # Выводим вторичное окно, не забыв указать в параметре parent
        ViewSecondaryHighScores(master=tkinter.Toplevel(), parent=self)

    def show_window_about(self):
        # Выводим вторичное окно, не забыв указать в параметре parent
        ViewSecondaryAbout(master=tkinter.Toplevel(), parent=self)


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def set_mines_count(self):
        mines_count = self.view.prompt_for_mines_count()

        try:
            self.model.set_mines_count(mines_count)
            try:
                self.view.display_mines_count(str(self.model.get_mines_count()))
            except ValueError:
                print("Переменная mines_count не является числом")
        except ValueError:
            print("Переменная mines_count не является числом")

    def set_field_size(self):
        field_size = self.view.prompt_for_field_size()
        self.model.set_field_size(field_size)
        self.view.display_field_size(str(self.model.get_field_size()))


class Minesweeper(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title("Minesweper")
        self.geometry("800x600")
        self.resizable(True, True)
        self.minsize(300, 200)
        self.maxsize(1200, 800)

        # создание model
        model = Model()

        # создание view_and_controller
        view = View()
        view.pack()

        # создание контроллера
        controller = Controller(model, view)
        controller.set_field_size()
        controller.set_mines_count()
        view.set_controller(controller)


if __name__ == "__main__":
    app = Minesweeper()
    app.mainloop()
