import tkinter
import tkinter.ttk
from tkinter import ttk
from tkinter.messagebox import showerror
from temperature_task.celsius_temperature import CelsiusTemperature
from temperature_task.fahrenheit_temperature import FahrenheitTemperature
from temperature_task.kelvin_temperature import KelvinTemperature


class View(tkinter.ttk.Frame):
    def __init__(self, temperature_scales, master=None):
        super().__init__(master)
        self.__temperature_scales = temperature_scales

        frame_for_from_temperature_lable = tkinter.ttk.Frame(self)
        frame_for_converting_temperature = tkinter.ttk.Frame(self)
        frame_for_to_temperature_lable = tkinter.ttk.Frame(self)
        frame_for_converted_temperature = tkinter.ttk.Frame(self)
        frame_for_empty_space = tkinter.ttk.Frame(self)
        frame_for_button_ok = tkinter.ttk.Frame(self)
        frame_for_lower_empty_space = tkinter.ttk.Frame(self)

        frame_for_from_temperature_lable.pack()
        frame_for_converting_temperature.pack()
        frame_for_to_temperature_lable.pack()
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
        self.__from_scale.set(self.__temperature_scales[0])
        self.__to_scale.set(self.__temperature_scales[0])

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
        self.__result_label = tkinter.ttk.Label(frame_for_converted_temperature, text="      " + "0",
                                                width=20, font=("Arial", 11))
        self.__result_label.pack(side="left", padx=20, pady=20)

        self.__button.bind("<Button>", lambda event: self.show_message(), add="+")

        # Надпись "FROM" над "кнопкой для выбора между C, K или F" для вводимой температуры
        self.__from_label = tkinter.ttk.Label(frame_for_from_temperature_lable, text="FROM temperature", font=("Arial", 11))
        self.__from_label.pack(side="right")

        # Надпись "TO" над "кнопкой для выбора между C, K или F" для выводимой температуры
        self.__to_label = tkinter.ttk.Label(frame_for_to_temperature_lable, text="TO temperature", font=("Arial", 11))
        self.__to_label.pack(side="right")

        # Комбобокс для выбора шкалы вводимой температуры
        self.__from_scale_combobox = ttk.Combobox(frame_for_converting_temperature, textvariable=self.__from_scale,
                                                  width=3, font=("Arial", 11))
        self.__from_scale_combobox["values"] = self.__temperature_scales
        self.__from_scale_combobox["state"] = "readonly"
        self.__from_scale_combobox.pack(side="left")

        # Комбобокс для выбора шкалы выводимой температуры
        self.__to_scale_combobox = ttk.Combobox(frame_for_converted_temperature, textvariable=self.__to_scale,
                                                width=3, font=("Arial", 11))
        self.__to_scale_combobox["values"] = self.__temperature_scales
        self.__to_scale_combobox["state"] = "readonly"
        self.__to_scale_combobox.pack(side="left", padx=20, pady=20)

        # Отступ над "кнопкой перевода температур"
        self.__empty_space_upper_ok = ttk.Label(frame_for_empty_space, text=" ")
        self.__empty_space_upper_ok.pack()

        # Отступ после "кнопки перевода температур"
        self.__empty_space_lower_ok = ttk.Label(frame_for_lower_empty_space, text=" ")
        self.__empty_space_lower_ok.pack()

        # set the controller
        self.__controller = None

    def set_controller(self, controller):
        self.__controller = controller

    def button_handler(self, message_temperature):
        try:
            float(message_temperature)
        except ValueError:
            result = showerror("Ошибка", "Введенное значение - не число")

            if result:
                return ""

        converted_temperature = 0

        if str(self.__from_scale.get()) == "C":
            converted_temperature = (
                float(CelsiusTemperature(message_temperature).convert_temperature_to_celsius_scale()))

        if str(self.__from_scale.get()) == "F":
            converted_temperature = (
                float(FahrenheitTemperature(message_temperature).convert_temperature_to_celsius_scale()))

        if str(self.__from_scale.get()) == "K":
            converted_temperature = float(KelvinTemperature(message_temperature).convert_temperature_to_celsius_scale())

        if str(self.__to_scale.get()) == "C":
            return CelsiusTemperature(converted_temperature).convert_temperature_from_celsius_scale()

        if str(self.__to_scale.get()) == "F":
            return FahrenheitTemperature(converted_temperature).convert_temperature_from_celsius_scale()

        if str(self.__to_scale.get()) == "K":
            return KelvinTemperature(converted_temperature).convert_temperature_from_celsius_scale()

    # привязка к кнопке "кнопка перевода температуры" отображения измененного значения result_message
    def show_message(self):
        self.__result_label["text"] = self.__result_message.get()

    def prompt_for_temperature_value(self):
        return self.__message.get()

    def prompt_for_from_scale(self):
        return self.__from_scale.get()

    def prompt_for_to_scale(self):
        return self.__to_scale.get()
