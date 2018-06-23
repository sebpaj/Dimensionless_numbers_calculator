from tkinter import *


class Window(object):

    def __init__(self, root):

        self.root = root
        self.root.title("DN caluclator")

        l1 = Label(root, text="Density [kg/m3]")
        l1.grid(sticky="W", row=0, column=1)
        l2 = Label(root, text="Velocity [m/s]")
        l2.grid(sticky="W", row=1, column=1)
        l3 = Label(root, text="Characteristic length [m]")
        l3.grid(sticky="W", row=2, column=1)
        l4 = Label(root, text="Dynamic viscosity [kg/m3]")
        l4.grid(row=3, column=1)

        self.density = StringVar()
        self.e1 = Entry(root, textvariable=self.density, width=10)
        self.e1.grid(row=0, column=0)

        self.velocity = StringVar()
        self.e2 = Entry(root, textvariable=self.velocity, width=10)
        self.e2.grid(row=1, column=0)

        self.characteristic_length = StringVar()
        self.e3 = Entry(root, textvariable=self.characteristic_length, width=10)
        self.e3.grid(row=2, column=0)

        self.dynamic_viscosity = StringVar()
        self.e4 = Entry(root, textvariable=self.dynamic_viscosity, width=10)
        self.e4.grid(row=3, column=0)


root = Tk()
Window(root)
root.mainloop()