from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror


def convert_celsius_to_fahrenheit(celsius_temperature):
    return f"{(float(celsius_temperature) * 9 / 5 + 32):.2f}"


def convert_celsius_to_kelvin(celsius_temperature):
    return f"{(float(celsius_temperature) + 273.15):.2f}"


def convert_kelvin_to_fahrenheit(kelvin_temperature):
    return f"{((float(kelvin_temperature) - 273.15) * 9 / 5 + 32):.2f}"


def convert_kelvin_to_celsius(kelvin_temperature):
    return f"{(float(kelvin_temperature) - 273.15):.2f}"


def convert_fahrenheit_to_celsius(fahrenheit_temperature):
    return f"{((float(fahrenheit_temperature) - 32) * 5 / 9):.2f}"


def convert_fahrenheit_to_kelvin(fahrenheit_temperature):
    return f"{((float(fahrenheit_temperature) - 32) * 5 / 9 + 273.15):.2f}"


# функция для кнопки "FROM"
def button_handler(message):
    try:
        float(message)
    except ValueError:
        result = showerror("Ошибка значения", "Введенное значение - не число")
        if result:
            return
    else:
        if str(from_message.get()) == str(to_message.get()):
            return str(message)
        elif from_message.get() == "F":
            if to_message.get() == "C":
                return convert_fahrenheit_to_celsius(message)
            elif to_message.get() == "K":
                return convert_fahrenheit_to_kelvin(message)
        elif from_message.get() == "K":
            if to_message.get() == "C":
                return convert_kelvin_to_celsius(message)
            elif to_message.get() == "F":
                return convert_kelvin_to_fahrenheit(message)
        elif from_message.get() == "C":
            if to_message.get() == "K":
                return convert_celsius_to_kelvin(message)
            elif to_message.get() == "F":
                return convert_celsius_to_fahrenheit(message)


# создаем окно
root = Tk()

# 6 горизонтальных рамок, расположенных сверху вниз
frame_1 = Frame(root)
frame_2 = Frame(root)
frame_3 = Frame(root)
frame_4 = Frame(root)
frame_5 = Frame(root)
frame_6 = Frame(root)

frame_1.pack()
frame_2.pack()
frame_3.pack()
frame_4.pack()
frame_5.pack()
frame_6.pack()

# заголовок окна
root.title("Перевод температуры")
# размеры окна
root.geometry("800x600")
# разрешаем окну растягиваться по горизонтали и вертикали
root.resizable(True, True)
root.minsize(300, 200)
root.maxsize(1200, 800)

# создание двух переменных:
# message - переменная, которой присвоится введенное значение температуры
# result_message - переменная, которой присвоится результат перевода переменной message
message = StringVar()
result_message = StringVar()

# добавка  виджета Entry и привязка к нему переменной message
entry = ttk.Entry(frame_2, textvariable=message)
entry.pack(side="left", fill=X, padx=20, pady=20)

# добавка  "кнопки перевода температуры" и привязка к нему события:
# при нажатии этой кнопки получаем значение result_message
button = ttk.Button(frame_6, text="Ok")
button.pack()

button.bind("<Button>", lambda event: result_message.set(button_handler(message.get())))

# добавка виджета Label, в котором выводится полученное значение переменной result_message
result_label = Label(frame_4, text="0", width=23)
result_label.pack(side=LEFT)


# привязка к кнопке "кнопка перевода температуры" отображения измененного значения result_message
def show_message():
    result_label["text"] = result_message.get()


button.bind("<Button>", lambda event: show_message(), add="+")

# Надпись "FROM" над "кнопкой для выбора между C, K или F" для вводимой температуры
from_label = Label(frame_1, text="FROM")
from_label.pack(side=RIGHT)

# Надпись "TO" над "кнопкой для выбора между C, K или F" для выводимой температуры
to_label = Label(frame_3, text="TO")
to_label.pack(side=RIGHT)

# Создание переменных в которые записывается значения C, K или F для записи в них выбранных размерностей
# вводимой и выводимой температуры
from_message = StringVar()
to_message = StringVar()

# Создание кнопки для выбора размерности вводимой температуры
# Значение переменной from_message используется: 1) для изменения надписи на этой кнопке;
# 2) для выбора правильной функции перевода температуры
from_submit_button = ttk.Button(frame_2, text="CHOOSE")
from_submit_button.bind("<Button>", lambda event: from_message.set(str(next(from_iterator))))


# Изменение надписи на кнопке from_submit_button
def from_submit_button_handler():
    from_submit_button["text"] = from_message.get()


from_submit_button.bind("<Button>", lambda event: from_submit_button_handler(), add="+")
from_submit_button.pack(side=LEFT)

# Создание кнопки для выбора размерности выводимой температуры
# Значение переменной to_message используется: 1) для изменения надписи на этой кнопке;
# 2) для выбора правильной функции перевода температуры
to_submit_button = ttk.Button(frame_4, text="CHOOSE")
to_submit_button.bind("<Button>", lambda event: to_message.set(str(next(to_iterator))))


# Изменение надписи на кнопке to_submit_button
def to_submit_button_handler():
    to_submit_button["text"] = to_message.get()


to_submit_button.bind("<Button>", lambda event: to_submit_button_handler(), add="+")
to_submit_button.pack(side=LEFT)


# Отступ над "кнопкой перевода температур"
to_label = Label(frame_5, text=" ")
to_label.pack()


def circular():
    while True:
        for temperature in ["C", "K", "F"]:
            yield str(temperature)


from_iterator = circular()
to_iterator = circular()

root.mainloop()
