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
f_top = Frame(root)
f_center = Frame(root)
f_bottom = Frame(root)
f_ground = Frame(root)
f_ground_1 = Frame(root)

f_top.pack()
f_center.pack()
f_bottom.pack()
f_ground.pack()
f_ground_1.pack()

# заголовок окна
root.title("Перевод температуры")
# размеры окна
root.geometry("800x600")
# разрешаем окну растягиваться по горизонтали и вертикали
root.resizable(True, True)
root.minsize(300, 200)
root.maxsize(1200, 800)

# добавка переменной виджета
message = StringVar()

result_message = StringVar()

message.get()

entry = ttk.Entry(f_top, textvariable=message)
entry.pack(side="left", fill=X, padx=20, pady=20)

text = message.get()

button = ttk.Button(f_center, text="Ok", command=entry.get())
button.pack(side=LEFT)

button.bind("<Button>", lambda event: result_message.set(button_handler(message.get())))

# Было: button.bind("<Button>", lambda event: message.set(button_handler(message.get())))

result_label = Label(f_top, text="0")
result_label.pack(side=RIGHT)


def show_message():
    result_label["text"] = from_message.get() + " " + result_message.get() + " " + to_message.get()


button.bind("<Button>", lambda event: show_message(), add="+")


# Блок "FROM"
from_temperatures = ["C", "K", "F"]
from_temperatures_var = StringVar(value=from_temperatures)

from_lbox = Listbox(f_bottom, width=15, height=8, listvariable=from_temperatures_var)
from_lbox.pack(side=LEFT)


# выбор значения температуры из "FROM"
def get_selected_from_value():
    # переменная для индекса выбранного значения
    index = from_lbox.curselection()
    from_message.set(index)
    print(index[0])
    return index[0]


# Надпись над кнопкою для перевода "FROM"
from_label = Label(f_ground, text="FROM              ")
from_label.pack(side=LEFT)


# Блок "TO"
to_temperatures = ["C", "K", "F"]
to_temperatures_var = StringVar(value=to_temperatures)

to_lbox = Listbox(f_bottom, width=15, height=8, listvariable=to_temperatures_var)
to_lbox.pack(side=LEFT)


# выбор значения температуры из "TO"
def get_selected_to_value():
    # переменная для индекса выбранного значения
    index = to_lbox.curselection()
    to_message.set(index)
    print(index[0])
    return index[0]


to_label = Label(f_ground, text="      TO")
to_label.pack(side=LEFT)

from_message = StringVar(value=from_temperatures[0])
to_message = StringVar(value=to_temperatures[0])


# Изменение надписи на кнопке from_submit_button
def from_submit_button_handler():
    from_submit_button["text"] = from_message.get()


# Кнопка from_submit_button для подключения к "FROM"
from_submit_button = ttk.Button(f_ground_1, text="C")
from_submit_button.bind("<Button>", lambda event: from_message.set(str(next(iterator))))
from_submit_button.bind("<Button>", lambda event: from_submit_button_handler(), add="+")
from_submit_button.pack(side=LEFT)


# Изменение надписи на кнопке to_submit_button
def to_submit_button_handler():
    to_submit_button["text"] = to_message.get()


# Кнопка to_submit_button для подключения к "TO"
to_submit_button = ttk.Button(f_ground_1, text="C")
to_submit_button.bind("<Button>", lambda event: to_message.set(to_temperatures[get_selected_to_value()]))
to_submit_button.bind("<Button>", lambda event: to_submit_button_handler(), add="+")
to_submit_button.pack(side=LEFT)


def fto():
    for temperature in ["C", "K", "F"]:
        yield temperature


def ffrom():
    for temperature in ["C", "K", "F"]:
        yield str(temperature)

iterator = ffrom()
# отображение температуры
root.mainloop()
