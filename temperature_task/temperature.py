import tkinter
import tkinter.ttk
from tkinter import ttk
from tkinter.messagebox import showerror


class Model:
    def __init__(self, temperature_scale):
        self.temperature_scale = temperature_scale


class View(tkinter.ttk.Frame):
    def __init__(self, temperature_scale, master=None):
        super().__init__(master)
        self.temperature_scale = temperature_scale

        frame_1 = tkinter.ttk.Frame(self)
        frame_2 = tkinter.ttk.Frame(self)
        frame_3 = tkinter.ttk.Frame(self)
        frame_4 = tkinter.ttk.Frame(self)
        frame_5 = tkinter.ttk.Frame(self)
        frame_6 = tkinter.ttk.Frame(self)
        frame_7 = tkinter.ttk.Frame(self)

        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        frame_4.pack()
        frame_5.pack()
        frame_6.pack()
        frame_7.pack()

        # создание двух переменных:
        # message - переменная, которой присвоится введенное значение температуры
        # result_message - переменная, которой присвоится результат перевода переменной message
        # self.message = tkinter.StringVar()
        self.result_message = tkinter.StringVar()
        self.message = tkinter.StringVar()

        # Создание переменных в которые записывается значения C, K или F для записи в них выбранных шкал
        # вводимой и выводимой температуры
        self.from_scale = tkinter.StringVar()
        self.to_scale = tkinter.StringVar()

        # добавка  виджета Entry и привязка к нему переменной message
        self.entry = ttk.Entry(frame_2, textvariable=self.message, font=("Arial", 11), foreground="blue")
        self.entry.pack(side="left", padx=20, pady=20)

        # добавка  "кнопки перевода температуры" и привязка к нему события:
        # при нажатии этой кнопки получаем значение result_message
        self.button = ttk.Button(frame_6, text="OK")
        self.button.pack()

        self.button.bind("<Button>",
                         lambda event: self.result_message.set("      " +
                                                               str(self.button_handler(self.message.get()))))

        # добавка виджета Label, в котором выводится полученное значение переменной result_message
        self.result_label = tkinter.ttk.Label(frame_4, text="      " + "0", width=20, font=("Arial", 11),
                                              foreground="blue")
        self.result_label.pack(side="left", padx=20, pady=20)

        self.button.bind("<Button>", lambda event: self.show_message(), add="+")

        # Надпись "FROM" над "кнопкой для выбора между C, K или F" для вводимой температуры
        self.from_label = tkinter.ttk.Label(frame_1, text="FROM", font=("Arial", 11), foreground="blue")
        self.from_label.pack(side="right")

        # Надпись "TO" над "кнопкой для выбора между C, K или F" для выводимой температуры
        self.to_label = tkinter.ttk.Label(frame_3, text="TO", font=("Arial", 11), foreground="blue")
        self.to_label.pack(side="right")

        # Комбобокс для выбора шкалы вводимой температуры
        self.from_scale_combobox = ttk.Combobox(frame_2, textvariable=self.from_scale, width=3, font=("Arial", 11),
                                                foreground="blue")
        self.from_scale_combobox["values"] = self.temperature_scale
        self.from_scale_combobox["foreground"] = "blue"
        self.from_scale_combobox["state"] = "readonly"
        self.from_scale_combobox.pack(side="left")

        # Комбобокс для выбора шкалы выодимой температуры
        self.to_scale_combobox = ttk.Combobox(frame_4, textvariable=self.to_scale, width=3, font=("Arial", 11),
                                              foreground="blue")
        self.to_scale_combobox["values"] = self.temperature_scale
        self.to_scale_combobox["state"] = "readonly"
        self.to_scale_combobox.pack(side="left", padx=20, pady=20)

        # Отступ над "кнопкой перевода температур"
        self.empty_space_upper_ok = ttk.Label(frame_5, text=" ")
        self.empty_space_upper_ok.pack()

        # Отступ после "кнопки перевода температур"
        self.empty_space_lower_ok = ttk.Label(frame_7, text=" ")
        self.empty_space_lower_ok.pack()

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def button_handler(self, message_temperature):
        try:
            float(message_temperature)
        except ValueError:
            result = showerror("Ошибка", "Введенное значение - не число")

            if result:
                return ""

        if str(self.from_scale.get()) == str(self.to_scale.get()):
            return str(message_temperature)

        if self.from_scale.get() == "F":
            if self.to_scale.get() == "C":
                return round(((float(message_temperature) - 32) * 5 / 9), 2)

            if self.to_scale.get() == "K":
                return round(((float(message_temperature) - 32) * 5 / 9 + 273.15), 2)

        if self.from_scale.get() == "K":
            if self.to_scale.get() == "C":
                return round((float(message_temperature) - 273.15), 2)

            if self.to_scale.get() == "F":
                return round(((float(message_temperature) - 273.15) * 9 / 5 + 32), 2)

        if self.from_scale.get() == "C":
            if self.to_scale.get() == "K":
                return round((float(message_temperature) + 273.15), 2)

            if self.to_scale.get() == "F":
                return round((float(message_temperature) * 9 / 5 + 32), 2)

    # привязка к кнопке "кнопка перевода температуры" отображения измененного значения result_message
    def show_message(self):
        self.result_label["text"] = self.result_message.get()


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self):
        self.model.temperature_scale = ("C", "K", "F")


class TemperatureConverter(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title("Перевод температуры")
        self.resizable(False, False)

        # create a model
        temperature_scale = ("C", "K", "F")
        model = Model(temperature_scale)

        # create a view and place it on the root window
        view = View(temperature_scale)

        view.pack()
        self.title("Перевод температуры")
        self.resizable(False, False)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = TemperatureConverter()
    app.mainloop()
