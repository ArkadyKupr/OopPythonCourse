import tkinter
from tkinter import ttk
from tkinter import *
import random
from PIL import Image, ImageTk
import datetime
from tkinter.messagebox import showinfo
from minesweeper_task.view.about import About
from minesweeper_task.view.records import Records

MIN_FIELD_SIZE = 10
MAX_FIELD_SIZE = 30

MIN_MINES_COUNT = 9


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

        # Переменная, в которую записывается введенное значение количество мин
        self.initial_mines_count = tkinter.StringVar()

        # добавка label, связанного с количеством мин
        self.mines_count_label = ttk.Label(self.frame_1, text="Count of mines:", width=16)
        self.mines_count_label.pack(side="left", padx=10, pady=20)

        # добавка  виджета Entry и привязка к нему переменной - mines_count
        self.mines_count_entry = ttk.Entry(self.frame_1, textvariable=self.mines_count, width=10)
        self.mines_count_entry.pack(side="left", padx=10, pady=20)

        # поддержка таблицы рекордов
        self.gamer_name = tkinter.StringVar()

        # переменная для комбобокса
        self.__menu_option = tkinter.StringVar()
        self.__menu_option.set("Menu")

        self.__page_options = ["New Game", "About", "Records", "Exit"]

        self.__menu_combobox = ttk.Combobox(self.frame_1, textvariable=self.__menu_option, values=self.__page_options, width=15)
        self.__menu_combobox.pack(side="right", padx=20, pady=20)
        self.__menu_combobox.bind("<<ComboboxSelected>>", self.show_selected_page)
        self.__menu_combobox["state"] = "readonly"





        self.gamer_name_entry = ttk.Entry(self.frame_1, textvariable=self.gamer_name)
        self.gamer_name_entry.pack(side="right", padx=10, pady=20)

        self.gamer_name_label = ttk.Label(self.frame_1, text=" User:", width=10)
        self.gamer_name_label.pack(side="right", padx=10, pady=20)

        # добавка  виджета Entry и привязка к нему переменной - size
        self.field_size_entry = ttk.Entry(self.frame_1, textvariable=self.field_size, width=10)
        self.field_size_entry.pack(side="right", padx=10, pady=20)

        # добавка label, связанного с шириной поля
        self.size_label = ttk.Label(self.frame_1, text="Field width:", width=15)
        self.size_label.pack(side="right", padx=20, pady=20)

        # добавка  кнопки "About"
        self.about_button = ttk.Button(frame_2, text="About", command=self.show_window_about)
        self.about_button.pack(side="right", padx=20, pady=20)

        # добавка  кнопки "Exit"
        self.exit_button = ttk.Button(frame_2, text="Exit", command=self.destroy)
        self.exit_button.pack(side="right", padx=20, pady=20)

        # добавка  кнопки "Records"
        self.records_button = ttk.Button(frame_2, text="Records", command=self.show_window_records)
        self.records_button.pack(side="right", padx=20, pady=20)

        # добавка "кнопки создания поля и расстановки мин" и привязка к нему события
        self.new_game_button = ttk.Button(frame_2, text="New Game")
        self.new_game_button.pack(side="right", padx=20, pady=20)

        self.new_game_button.bind("<Button-3>", lambda event: self.delete_field())
        self.new_game_button.bind("<Button-3>", lambda event: self.check_mines_count_and_field_size(), add="+")
        self.new_game_button.bind("<Button-3>", lambda event: self.create_field(), add="+")

        # блок кода для подсчета времени, потраченного на окончание игры с выигрышом
        self.start_seconds = tkinter.IntVar()
        self.new_game_button.bind("<Button-3>", lambda event: self.start_seconds.set(self.time_count()), add="+")

        self.end_seconds = tkinter.IntVar()
        self.game_time = tkinter.StringVar()

        # переменная, в которую записываетя True при первом нажатии любой кнопки в поле
        self.first_press_on_any_button = tkinter.BooleanVar()
        self.first_press_on_any_button.set(False)

        # создание переменной количества открытых клеточек поля для выведения сообщения о выигрыше
        self.opened_cells_quantity = tkinter.IntVar()

        # создание переменных, ответственных за вторичное изменение размера поля:
        # self.game_already_launched - переменная, показывающая, что до этого момента как минимум одна игра была сыграна
        # self.previous_game_field_size - переменная, в которую записывается значение размера поля
        # предыдущей сыгранной игры
        self.game_already_launched = tkinter.BooleanVar()
        self.game_already_launched.set(False)

        self.previous_game_field_size = tkinter.StringVar()

        # Создание кнопок в поле
        self.__buttons = [[None for _ in range(1)] for _ in range(1)]

        # установка контроллера
        self.controller = None

        self.__mines_matrix = []

        self.__stack = []

    # Функция, запускающаяся при выборе опции комбобокса (self.__menu_combobox)
    def show_selected_page(self, event):
        if self.__menu_option.get() == "About":
            About(master=tkinter.Toplevel(), parent=self)
            self.__menu_option.set("Menu")

        if self.__menu_option.get() == "Records":
            Records(master=tkinter.Toplevel(), parent=self)
            self.__menu_option.set("Menu")

        if self.__menu_option.get() == "Exit":
            self.destroy()
            self.__menu_option.set("Menu")

        if self.__menu_option.get() == "New Game":
            self.delete_field()
            self.check_mines_count_and_field_size()
            self.create_field()
            self.__menu_option.set("Menu")

    # проверка, что переменные: размеры поля - field_size, и количество мин - mines_count, были int
    def check_mines_count_and_field_size(self):
        try:
            int(self.mines_count.get())
        except ValueError:
            self.mines_count.set(str(MIN_MINES_COUNT))

        try:
            int(self.field_size.get())
        except ValueError:
            self.field_size.set(str(MIN_FIELD_SIZE))

        if int(self.field_size.get()) in range(MIN_FIELD_SIZE, MAX_FIELD_SIZE + 1):
            # проверка, что размеры поля - field_size, соответствовали mines_count
            if int(self.field_size.get()) * int(self.field_size.get()) <= int(self.mines_count.get()):
                self.mines_count.set(str(int(self.field_size.get()) * int(self.field_size.get()) - 1))
        else:
            self.mines_count.set(str(MIN_MINES_COUNT))
            self.field_size.set(str(MIN_FIELD_SIZE))

    def set_controller(self, controller):
        self.controller = controller

    def save_button_clicked(self):
        if self.controller:
            self.controller.set_mines_count()

    def get_mines_count(self):
        return self.mines_count.get()

    def display_mines_count(self, mines_count):
        self.mines_count.set(str(mines_count))

    def get_field_size(self):
        return self.field_size.get()

    def display_field_size(self, field_size):
        self.field_size.set(str(field_size))

    # функция для подсчета времени, потраченного на заканчивание игры с выигрышом
    def time_count(self):
        then = datetime.datetime(2025, 2, 5, 19, 27, 0)
        start = datetime.datetime.now()
        delta = start - then
        return int(delta.total_seconds())

    # функция создания поля, которая вызывается при нажании кнопки "New Game"
    def create_field(self):
        # запись в  переменную self.previous_game_field_size значения размера поля текущей игры
        self.previous_game_field_size.set(self.field_size.get())

        field_size = int(self.field_size.get())

        # создание 3-х матриц для tkinter переменных, в которые будут записаны значения из матриц:
        # 1) значения из матрицы мин,
        # 2) значения из матрицы количества соседних клеток,
        # 3) значения из матрицы клеток, помеченных флажками,
        # 4) значения из матрицы клеток, помеченных вопросительными знаками,
        # 5) значения из марицы открытых клеток (чтобы не превышать дозволенного числа вызовов рекурсивной функции)
        mines_values_matrix = [[None for _ in range(field_size)] for _ in range(field_size)]
        neighbour_mines_quantity_values_matrix = [[None for _ in range(field_size)] for _ in range(field_size)]

        flagged_cells_values_matrix = [[None for _ in range(field_size)] for _ in range(field_size)]
        questioned_cells_values_matrix = [[None for _ in range(field_size)] for _ in range(field_size)]
        opened_cells_values_matrix = [[None for _ in range(field_size)] for _ in range(field_size)]

        self.first_press_on_any_button.set(True)

        for row in range(field_size):
            for col in range(field_size):
                mines_values_matrix[row][col] = tkinter.StringVar()
                neighbour_mines_quantity_values_matrix[row][col] = tkinter.StringVar()

                # flagged_cell - помечена флагом. Нажимая левой кнопкой, помечаем знаком вопроса, т.е. questioned_cell
                # questioned_cell - помечена знаком вопроса. Нажимая левой кнопкой, переходим к состоянию opened_cell
                flagged_cells_values_matrix[row][col] = tkinter.BooleanVar()
                flagged_cells_values_matrix[row][col].set(False)

                questioned_cells_values_matrix[row][col] = tkinter.BooleanVar()
                questioned_cells_values_matrix[row][col].set(False)
                print(flagged_cells_values_matrix[row][col].get(), end=" ")

                opened_cells_values_matrix[row][col] = tkinter.BooleanVar()
                opened_cells_values_matrix[row][col].set(False)
                print(opened_cells_values_matrix[row][col].get(), end=" ")

        # открытие картинки мины, пустой клетки и флага
        mine = Image.open(r".\view\mine.png")
        resized_mine = mine.resize((15, 15))
        mine_picture = ImageTk.PhotoImage(resized_mine)

        crossed_mine = Image.open(r".\view\crossed_mine.png")
        resized_crossed_mine = crossed_mine.resize((15, 15))
        crossed_mine_picture = ImageTk.PhotoImage(resized_crossed_mine)

        flag = Image.open(r".\view\flag.png")
        resized_flag = flag.resize((15, 15))
        flag_picture = ImageTk.PhotoImage(resized_flag)

        question_mark = Image.open(r".\view\question_mark.png")
        resized_question_mark = question_mark.resize((15, 15))
        question_mark_picture = ImageTk.PhotoImage(resized_question_mark)

        # создание матрицы кнопок в поле
        self.__buttons = [[None for _ in range(field_size)] for _ in range(field_size)]

        for row in range(field_size):
            for col in range(field_size):
                self.__buttons[row][col] = ttk.Button(self.frame_3,
                                                      text=" ",
                                                      width=3,
                                                      command=lambda row=row, col=col: show_content(row, col))

                self.__buttons[row][col].grid(row=row, column=col, sticky=NSEW)

        def show_content(row, col):
            if self.first_press_on_any_button.get():
                self.first_press_on_any_button.set(False)
                self.__buttons[row][col].bind("<Button-1>", lambda event: create_mines_matrix(row, col))

                self.__buttons[row][col].bind("<Button-1>", lambda event: create_matrices(), add="+")

                self.__buttons[row][col].bind("<Button-1>", lambda event: show_field_on_first_press_of_button(row, col),
                                              add="+")

                opened_cells_values_matrix[row][col].set(True)
            else:
                self.__buttons[row][col].unbind("<Button-1>")

                if not opened_cells_values_matrix[row][col].get():
                    if not flagged_cells_values_matrix[row][col].get() and not questioned_cells_values_matrix[row][
                        col].get():
                        self.__buttons[row][col].bind("<Button-3>", lambda event: show_flag_or_question(row, col),
                                                      add="+")
                    # без условия "not flagged_cells_values_matrix[row][col].get()
                    # and not questioned_cells_values_matrix[row][col].get()" возникает проблемы с чередованием:
                    # флажок, вопрос, пустая клетка. При оставлении флажка или знака вопроса, нажатии другой клетки и
                    # возврате к оставленным флажке и клетке - нарушается последовательность чередования
                    # "флажок, вопрос, пустая клетка". Будто запускается вторая, точно такая же функция и эти функции
                    # получают одновременный доступ к матрицам flagged_cells_values_matrix и
                    # questioned_cells_values_matrix.
                    self.__buttons[row][col].bind("<Button-1>", lambda event:
                    show_field_on_first_press_of_button(row, col), add="+")

        # проверка количества посещенных клеток, чтобы поймать момент выигрыша
        def check_visited_buttons_quantity():
            self.opened_cells_quantity.set(0)

            # увеличение количества посещенных клеток при посещении новой клетки
            for i in range(field_size):
                for j in range(field_size):
                    if opened_cells_values_matrix[i][j].get():
                        self.opened_cells_quantity.set(self.opened_cells_quantity.get() + 1)

            # выведение сообщения о выигрыше
            if self.opened_cells_quantity.get() == field_size * field_size - int(self.initial_mines_count.get()):
                # отображение всех мин и оставшихся флагов
                for row in range(field_size):
                    for col in range(field_size):
                        if int(mines_values_matrix[row][col].get()) == 1:
                            self.__buttons[row][col]["image"] = flag_picture

                        if not opened_cells_values_matrix[row][col].get() and int(
                                mines_values_matrix[row][col].get()) == 0:
                            self.__buttons[row][col]["text"] = "Blue"

                        self.__buttons[row][col].config(state="disabled")

                showinfo("Message", "You win!")

                self.game_already_launched.set(True)

                # установка минимального количества мин после завершения работы,
                # так как, устанавливая флаги, мы уменьшаем количество мин,
                # и это количество может переходить в новую игру
                self.mines_count.set(str(MIN_MINES_COUNT))

                # подсчет времени окончания игры для последующей записи в таблицу рекордов
                self.end_seconds.set(self.time_count())
                self.game_time.set(str(self.end_seconds.get() - self.start_seconds.get()))

                # запись имени и времени игры в таблицу рекордов
                self.write_gamer_record(self.gamer_name.get(), self.game_time.get())
                self.read_gamers_records()

        # отображение количества мин в соседних клетках в квадрате 3х3
        def show_quantity_of_neighbour_mines(row, col):
            self.__buttons[row][col].configure(text=neighbour_mines_quantity_values_matrix[row][col].get())
            opened_cells_values_matrix[row][col].set(True)

            check_visited_buttons_quantity()

        # отображение количества мин в соседних клетках в квадрате размером 3х3
        # функция применяется, если в клетке нет мины
        """def show_zero(row, col):
            if int(neighbour_mines_quantity_values_matrix[row][col].get()) == 0:
                if not opened_cells_values_matrix[row][col].get():
                    self.__buttons[row][col].config(state="disabled")

                    return show_field_on_first_press_of_button(row, col)

                check_visited_buttons_quantity()
            else:
                show_quantity_of_neighbour_mines(row, col)

        # раскрытие поля при первом нажатии кнопки
        def show_field_on_first_press_of_button(row, col):
            check_visited_buttons_quantity()
            #field_size = int(self.field_size.get())

            if flagged_cells_values_matrix[row][col].get():
                return

            if questioned_cells_values_matrix[row][col].get():
                return

            if int(mines_values_matrix[row][col].get()) == 1:
                showinfo("Message", "You lost!")
                self.game_already_launched.set(True)

                # отображение всех мин и оставшихся флагов
                # раскрытие игрового поля
                for row in range(field_size):
                    for col in range(field_size):
                        if (int(mines_values_matrix[row][col].get()) == 1 and
                                not questioned_cells_values_matrix[row][col].get()):
                            self.__buttons[row][col]["image"] = mine_picture

                        if (not opened_cells_values_matrix[row][col].get() and int(
                                mines_values_matrix[row][col].get()) == 0 and
                                not questioned_cells_values_matrix[row][col].get()):
                            if not flagged_cells_values_matrix[row][col].get():
                                self.__buttons[row][col].config(state="disabled")
                            else:
                                self.__buttons[row][col]["image"] = crossed_mine_picture

                        self.__buttons[row][col].config(state="disabled")

                        self.mines_count.set(str(MIN_MINES_COUNT))

            if int(neighbour_mines_quantity_values_matrix[row][col].get()) == 0:
                check_visited_buttons_quantity()

                self.__buttons[row][col].config(state="disabled")

                opened_cells_values_matrix[row][col].set(True)

                if col < field_size - 1:
                    show_zero(row, col + 1)

                if col > 0:
                    show_zero(row, col - 1)

                if row > 0 and col < field_size - 1:
                    show_zero(row - 1, col + 1)

                if row > 0 and col > 0:
                    show_zero(row - 1, col - 1)

                if row > 0:
                    show_zero(row - 1, col)

                if row < field_size - 1 and col < field_size - 1:
                    show_zero(row + 1, col + 1)

                if row < field_size - 1 and col > 0:
                    show_zero(row + 1, col - 1)

                if row < field_size - 1:
                    show_zero(row + 1, col)
            else:
                show_quantity_of_neighbour_mines(row, col)"""

        # Без рекурсии
        # отображение количества мин в соседних клетках в квадрате размером 3х3
        # функция применяется, если в клетке нет мины
        def show_zero(row, col):
            if int(neighbour_mines_quantity_values_matrix[row][col].get()) == 0:
                if not opened_cells_values_matrix[row][col].get():
                    self.__buttons[row][col].config(state="disabled")

                    self.__stack.append([row, col])

                    opened_cells_values_matrix[row][col].set(True)

                check_visited_buttons_quantity()
            else:
                show_quantity_of_neighbour_mines(row, col)

        # раскрытие поля при первом нажатии кнопки
        def show_field_on_first_press_of_button(row, col):
            check_visited_buttons_quantity()
            # field_size = int(self.field_size.get())

            if flagged_cells_values_matrix[row][col].get():
                return

            if questioned_cells_values_matrix[row][col].get():
                return

            if int(mines_values_matrix[row][col].get()) == 1:
                showinfo("Message", "You lost!")
                self.game_already_launched.set(True)

                # отображение всех мин и оставшихся флагов
                # раскрытие игрового поля
                for row in range(field_size):
                    for col in range(field_size):
                        if (int(mines_values_matrix[row][col].get()) == 1 and
                                not questioned_cells_values_matrix[row][col].get()):
                            self.__buttons[row][col]["image"] = mine_picture

                        if (not opened_cells_values_matrix[row][col].get() and int(
                                mines_values_matrix[row][col].get()) == 0 and
                                not questioned_cells_values_matrix[row][col].get()):
                            if not flagged_cells_values_matrix[row][col].get():
                                self.__buttons[row][col].config(state="disabled")
                            else:
                                self.__buttons[row][col]["image"] = crossed_mine_picture

                        self.__buttons[row][col].config(state="disabled")

                        self.mines_count.set(str(MIN_MINES_COUNT))

            if int(neighbour_mines_quantity_values_matrix[row][col].get()) == 0:
                check_visited_buttons_quantity()

                self.__buttons[row][col].config(state="disabled")

                opened_cells_values_matrix[row][col].set(True)

                if col < field_size - 1:
                    show_zero(row, col + 1)

                if col > 0:
                    show_zero(row, col - 1)

                if row > 0 and col < field_size - 1:
                    show_zero(row - 1, col + 1)

                if row > 0 and col > 0:
                    show_zero(row - 1, col - 1)

                if row > 0:
                    show_zero(row - 1, col)

                if row < field_size - 1 and col < field_size - 1:
                    show_zero(row + 1, col + 1)

                if row < field_size - 1 and col > 0:
                    show_zero(row + 1, col - 1)

                if row < field_size - 1:
                    show_zero(row + 1, col)

                while len(self.__stack) > 0:
                    element = self.__stack.pop()

                    i = element[0]
                    j = element[1]

                    if j < field_size - 1:
                        show_zero(i, j + 1)

                    if j > 0:
                        show_zero(i, j - 1)

                    if i > 0 and j < field_size - 1:
                        show_zero(i - 1, j + 1)

                    if i > 0 and j > 0:
                        show_zero(i - 1, j - 1)

                    if i > 0:
                        show_zero(i - 1, j)

                    if i < field_size - 1 and j < field_size - 1:
                        show_zero(i + 1, j + 1)

                    if i < field_size - 1 and j > 0:
                        show_zero(i + 1, j - 1)

                    if i < field_size - 1:
                        show_zero(i + 1, j)
            else:
                show_quantity_of_neighbour_mines(row, col)

        # Реализация логики правой кнопки мыши
        def show_flag_or_question(row, col):
            check_visited_buttons_quantity()

            if not opened_cells_values_matrix[row][col].get():
                if (not flagged_cells_values_matrix[row][col].get() and
                        not questioned_cells_values_matrix[row][col].get()):
                    flagged_cells_values_matrix[row][col].set(True)

                    self.__buttons[row][col]["image"] = flag_picture

                    # Уменьшение количества мин, отображаемых в виджете self.mines_count_entry
                    self.mines_count.set(int(self.mines_count.get()) - 1)

                    check_visited_buttons_quantity()
                    return

                if flagged_cells_values_matrix[row][col].get():
                    flagged_cells_values_matrix[row][col].set(False)
                    questioned_cells_values_matrix[row][col].set(True)

                    self.__buttons[row][col]["image"] = question_mark_picture
                    # Увеличение количества мин, отображаемых в виджете self.mines_count_entry
                    self.mines_count.set(int(self.mines_count.get()) + 1)
                    return

                if questioned_cells_values_matrix[row][col].get():
                    questioned_cells_values_matrix[row][col].set(False)

                    self.__buttons[row][col].config(image="")
                    return

        # создание матриц: матрицы мин и матрицы количества мин в соседних клетках в квадрате 3х3
        def create_matrices():
            print(self.__mines_matrix)

            mines_matrix = self.__mines_matrix
            neighbour_mines_quantity_matrix = self.create_neighbour_mines_quantity_matrix()

            for row in range(int(self.field_size.get())):
                for column in range(int(self.field_size.get())):
                    mines_values_matrix[row][column].set(self.__mines_matrix[row][column])
                    neighbour_mines_quantity_values_matrix[row][column].set(
                        neighbour_mines_quantity_matrix[row][column])

        # создание матрицы мин, в которой в клетке нажатия с координатой [col,row] в окружении 3х3 нет мин
        def create_mines_matrix(col, row):
            matrix_size = int(self.field_size.get())
            mines_count = int(self.mines_count.get())

            current_mines_quantity = 0

            self.__mines_matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

            last_index = int(matrix_size) - 1

            while current_mines_quantity < mines_count:
                i = random.randint(0, last_index)
                j = random.randint(0, last_index)

                # запрет, чтобы в матрице 3х3 вокруг координаты [col, row] была поставлена мина (1)
                if not (col - 1 <= i <= col + 1 and row - 1 <= j <= row + 1):
                    if self.__mines_matrix[i][j] != 1:
                        self.__mines_matrix[i][j] = 1

                        current_mines_quantity += 1

            self.initial_mines_count.set(self.mines_count.get())

            self.__buttons[row][col].unbind("<Button-1>")

            return self.__mines_matrix

    # функция для создания матрицы количества соседних мин
    def create_neighbour_mines_quantity_matrix(self):
        matrix_size = len(self.__mines_matrix)

        neighbour_mines_quantity_matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

        for i in range(matrix_size):
            for j in range(matrix_size):
                neighbour_mines_quantity_matrix[i][j] = 0

                if j < matrix_size - 1:
                    neighbour_mines_quantity_matrix[i][j] += self.__mines_matrix[i][j + 1]

                if j > 0:
                    neighbour_mines_quantity_matrix[i][j] += self.__mines_matrix[i][j - 1]

                if i > 0 and j < matrix_size - 1:
                    neighbour_mines_quantity_matrix[i][j] += self.__mines_matrix[i - 1][j + 1]

                if i > 0 and j > 0:
                    neighbour_mines_quantity_matrix[i][j] += self.__mines_matrix[i - 1][j - 1]

                if i > 0:
                    neighbour_mines_quantity_matrix[i][j] += self.__mines_matrix[i - 1][j]

                if i < matrix_size - 1 and j < matrix_size - 1:
                    neighbour_mines_quantity_matrix[i][j] += self.__mines_matrix[i + 1][j + 1]

                if i < matrix_size - 1 and j > 0:
                    neighbour_mines_quantity_matrix[i][j] += self.__mines_matrix[i + 1][j - 1]

                if i < matrix_size - 1:
                    neighbour_mines_quantity_matrix[i][j] += self.__mines_matrix[i + 1][j]

        return neighbour_mines_quantity_matrix

    # запись записи о выигрыше: имени и времени в секундах, в файл
    def write_gamer_record(self, gamer_name, game_time):
        with open("output.txt", "a", encoding="utf-8") as file:
            file.write(gamer_name + " " + game_time)

        with open("output.txt", "r", encoding="utf-8") as file, open("copy.txt", "w",
                                                                     encoding="utf-8") as copy_file:
            copy_file.write(file.read())

        self.read_gamers_records()

    # чтение из файла, сортировка записей о выигрыше, перезапись отсортированных записей в файл
    def read_gamers_records(self):
        with open("copy.txt", "r", encoding="utf-8") as copy_file, open("output.txt", "w",
                                                                        encoding="utf-8") as file:
            lines = [line.rstrip() for line in copy_file]

            gamers_records = []

            for i in range(0, len(lines)):
                index = lines[i].rfind(" ")

                if index != -1:
                    count = lines[i][index::]
                    gamers_records.append((lines[i], int(count)))

            gamers_records.sort(key=lambda gamers_records: gamers_records[1], reverse=False)

            for i in range(len(lines)):
                file.write(gamers_records[i][0] + "\r")

    # удаление игрового поля при перезапуске игры при нажатии кнопки "New Game"
    def delete_field(self):
        if self.game_already_launched.get() is True:
            field_size = int(self.previous_game_field_size.get())

            for row in range(field_size):
                for col in range(field_size):
                    self.__buttons[row][col].destroy()

    def show_window_records(self):
        # Выводим вторичное окно, не забыв указать в параметре parent
        Records(master=tkinter.Toplevel(), parent=self)

    def show_window_about(self):
        # Выводим вторичное окно, не забыв указать в параметре parent
        About(master=tkinter.Toplevel(), parent=self)

# https://itnotesblog.ru/note/pattern-mvc-na-primere-capera
