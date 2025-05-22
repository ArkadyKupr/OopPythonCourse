from model.model import Model
from view_and_controller.view_and_controller import ViewAndController
import tkinter.ttk


if __name__ == "__main__":
    root = tkinter.Tk()

    model = Model()
    view_and_controller = ViewAndController(model.get_temperatures(), master=root)

    root.title("Temperature conversion")

    root.mainloop()
