import tkinter
import tkinter.ttk
from tkinter import ttk
from tkinter.messagebox import showerror


class ViewAndController(tkinter.ttk.Frame):
    def __init__(self, temperatures, master=None):
        super().__init__(master)
        self.__temperatures = temperatures

        self.configure(width=200, height=100)
        self.pack()

        frame_for_from_temperature_label = tkinter.ttk.Frame(self)
        frame_for_converting_temperature = tkinter.ttk.Frame(self)
        frame_for_to_temperature_label = tkinter.ttk.Frame(self)
        frame_for_converted_temperature = tkinter.ttk.Frame(self)
        frame_for_empty_space = tkinter.ttk.Frame(self)
        frame_for_button_ok = tkinter.ttk.Frame(self)
        frame_for_lower_empty_space = tkinter.ttk.Frame(self)

        frame_for_from_temperature_label.pack()
        frame_for_converting_temperature.pack()
        frame_for_to_temperature_label.pack()
        frame_for_converted_temperature.pack()
        frame_for_empty_space.pack()
        frame_for_button_ok.pack()
        frame_for_lower_empty_space.pack()

        # создание двух переменных:
        # message - переменная, которой присвоится введенное значение температуры
        # result_message - переменная, которой присвоится результат перевода переменной message
        # self.message = tkinter.StringVar()
        self.__result_message = tkinter.StringVar()
        self.__message = tkinter.StringVar()

        # Создание переменных в которые записывается значения C, K или F для записи в них выбранных шкал
        # вводимой и выводимой температуры
        self.__from_scale = tkinter.StringVar()
        self.__to_scale = tkinter.StringVar()

        # Установка в комбобокс изначально шкалы
        self.__from_scale.set(self.__temperatures[0].get_temperature_abbreviation())
        self.__to_scale.set(self.__temperatures[0].get_temperature_abbreviation())

        # добавка  виджета Entry и привязка к нему переменной message
        self.__entry = ttk.Entry(frame_for_converting_temperature, textvariable=self.__message, font=("Arial", 11))
        self.__entry.pack(side="left", padx=20, pady=20)

        # добавка  "кнопки перевода температуры" и привязка к нему события:
        # при нажатии этой кнопки получаем значение result_message
        self.__button = ttk.Button(frame_for_button_ok, text="OK")
        self.__button.pack()

        self.__button.bind("<Button>",
                           lambda event: self.__result_message.set("      " +
                                                                   str(self.button_handler(self.__message.get()))))

        # добавка виджета Label, в котором выводится полученное значение переменной result_message
        self.__result_label = tkinter.ttk.Label(frame_for_converted_temperature, text=" ",
                                                width=20, font=("Arial", 11))
        self.__result_label.pack(side="left", padx=20, pady=20)

        self.__button.bind("<Button>", lambda event: self.show_message(), add="+")

        # Надпись "FROM" над "кнопкой для выбора между C, K или F" для вводимой температуры
        self.__from_label = tkinter.ttk.Label(frame_for_from_temperature_label,
                                              text="FROM temperature", font=("Arial", 11))
        self.__from_label.pack(side="right")

        # Надпись "TO" над "кнопкой для выбора между C, K или F" для выводимой температуры
        self.__to_label = tkinter.ttk.Label(frame_for_to_temperature_label, text="TO temperature", font=("Arial", 11))
        self.__to_label.pack(side="right")

        # Комбобокс для выбора шкалы вводимой температуры
        self.__from_scale_combobox = ttk.Combobox(frame_for_converting_temperature, textvariable=self.__from_scale,
                                                  width=3, font=("Arial", 11))
        self.__from_scale_combobox["values"] = self.__temperatures
        self.__from_scale_combobox["state"] = "readonly"
        self.__from_scale_combobox.pack(side="left")

        # Комбобокс для выбора шкалы выводимой температуры
        self.__to_scale_combobox = ttk.Combobox(frame_for_converted_temperature, textvariable=self.__to_scale,
                                                width=3, font=("Arial", 11))
        self.__to_scale_combobox["values"] = self.__temperatures
        self.__to_scale_combobox["state"] = "readonly"
        self.__to_scale_combobox.pack(side="left", padx=20, pady=20)

        # Отступ над "кнопкой перевода температур"
        self.__empty_space_upper_ok = ttk.Label(frame_for_empty_space, text=" ")
        self.__empty_space_upper_ok.pack()

        # Отступ после "кнопки перевода температур"
        self.__empty_space_lower_ok = ttk.Label(frame_for_lower_empty_space, text=" ")
        self.__empty_space_lower_ok.pack()

    def button_handler(self, message_temperature):
        try:
            float(message_temperature)
        except ValueError:
            result = showerror("Error", "The entered value is not a number")

            if result:
                return ""

        converted_temperature = 0

        for obj in self.__temperatures:
            if obj.get_temperature_abbreviation() == self.__from_scale_combobox.get():
                converted_temperature = obj.convert_to_celsius(message_temperature)

        for obj in self.__temperatures:
            if obj.get_temperature_abbreviation() == self.__to_scale_combobox.get():
                return obj.convert_from_celsius(converted_temperature)

    # привязка к кнопке "кнопка перевода температуры" отображения измененного значения result_message
    def show_message(self):
        self.__result_label["text"] = self.__result_message.get()
