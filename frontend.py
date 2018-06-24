from tkinter import *


class Window(object):

    def __init__(self, root):

        self.root = root
        self.root.title("DN caluclator")

        l1 = Label(root, text="Density [kg/m3]")
        l1.grid(sticky="W", row=1, column=1)
        l2 = Label(root, text="Velocity [m/s]")
        l2.grid(sticky="W", row=2, column=1)
        l3 = Label(root, text="Characteristic length [m]")
        l3.grid(sticky="W", row=3, column=1)
        l4 = Label(root, text="Dynamic viscosity [kg/m3]")
        l4.grid(sticky="W",row=4, column=1)
        l5 = Label(root, text="Sound's velocity [m/s]")
        l5.grid(sticky="W", row=5, column=1)
        l6 = Label(root, text="Kinematic viscosity [m2/s]")
        l6.grid(sticky="W", row=6, column=1)
        l7 = Label(root, text="Thermal diffusivity [m2/s]")
        l7.grid(sticky="W", row=7, column=1)
        l8 = Label(root, text="Convenctive heat transfer coefficient [W/m2K]")
        l8.grid(sticky="W", row=8, column=1)
        l9 = Label(root, text="Thermal conductivity [W/mK]")
        l9.grid(sticky="W", row=9, column=1)
        l10 = Label(root, text="Gravity [m2/s]")
        l10.grid(sticky="W", row=10, column=1)
        l11 = Label(root, text="Thermal expansion coefficient [1/K]")
        l11.grid(sticky="W", row=11, column=1)
        l12 = Label(root, text="Surface temperature [K]")
        l12.grid(sticky="W", row=12, column=1)
        l13 = Label(root, text="Fluid temperature [K]")
        l13.grid(sticky="W", row=13, column=1)
        l14 = Label(root, text="Time [s]")
        l14.grid(sticky="W", row=14, column=1)
        l15 = Label(root, text="Calculate", width=30, font=("Courier", 18))
        l15.grid(row=0, column=2)
        l16 = Label(root, text="Result",width=20, font=("Courier", 12))
        l16.grid(row=10, column=2)

        self.density = StringVar()
        self.e1 = Entry(root, textvariable=self.density, width=10)
        self.e1.grid(row=1, column=0, pady=2)

        self.velocity = StringVar()
        self.e2 = Entry(root, textvariable=self.velocity, width=10)
        self.e2.grid(row=2, column=0, pady=2)

        self.characteristic_length = StringVar()
        self.e3 = Entry(root, textvariable=self.characteristic_length, width=10)
        self.e3.grid(row=3, column=0, pady=2)

        self.dynamic_viscosity = StringVar()
        self.e4 = Entry(root, textvariable=self.dynamic_viscosity, width=10)
        self.e4.grid(row=4, column=0, pady=2)

        self.sound_velocity = StringVar()
        self.e5 = Entry(root, textvariable=self.sound_velocity, width=10)
        self.e5.grid(row=5, column=0, pady=2)

        self.kinematic_viscosity = StringVar()
        self.e6 = Entry(root, textvariable=self.kinematic_viscosity, width=10)
        self.e6.grid(row=6, column=0, pady=2)

        self.thermal_diffusivity = StringVar()
        self.e7 = Entry(root, textvariable=self.thermal_diffusivity, width=10)
        self.e7.grid(row=7, column=0, pady=2)

        self.convective_coefficient = StringVar()
        self.e8 = Entry(root, textvariable=self.convective_coefficient, width=10)
        self.e8.grid(row=8, column=0, pady=2)

        self.thermal_conductivity = StringVar()
        self.e9 = Entry(root, textvariable=self.thermal_conductivity, width=10)
        self.e9.grid(row=9, column=0, pady=2)

        self.gravity = StringVar()
        self.e10 = Entry(root, textvariable=self.gravity, width=10)
        self.e10.grid(row=10, column=0, pady=2)

        self.thermal_expansion = StringVar()
        self.e11 = Entry(root, textvariable=self.thermal_expansion, width=10)
        self.e11.grid(row=11, column=0, pady=2)

        self.surface_temperature = StringVar()
        self.e12 = Entry(root, textvariable=self.surface_temperature, width=10)
        self.e12.grid(row=12, column=0, pady=2)

        self.fluid_temperature = StringVar()
        self.e13 = Entry(root, textvariable=self.fluid_temperature, width=10)
        self.e13.grid(row=13, column=0, pady=2)

        self.time = StringVar()
        self.e14 = Entry(root, textvariable=self.time, width=10)
        self.e14.grid(row=14, column=0, pady=2)

        self.list1 = Listbox(root, height= 1, width=40)
        self.list1.grid(row=11,column=2, pady=2)

        b1 = Button(root, text="Re", width=10)
        b1.grid(sticky="W", row=2,column=2, padx=50)

        b2 = Button(root, text="Ma", width=10)
        b2.grid(row=2, column=2)

        b3 = Button(root, text="Pr", width=10)
        b3.grid(sticky="E", row=2, column=2, padx=50)

        b4 = Button(root, text="Nu", width=10)
        b4.grid(sticky="W", row=4,column=2, padx=50)

        b5 = Button(root, text="Ra", width=10)
        b5.grid(row=4, column=2)

        b6 = Button(root, text="Pe", width=10)
        b6.grid(sticky="E", row=4, column=2, padx=50)

        b7 = Button(root, text="Gr", width=10)
        b7.grid(sticky="W", row=6,column=2, padx=50)

        b8 = Button(root, text="Fo", width=10)
        b8.grid(row=6, column=2)

        b9 = Button(root, text="Bi", width=10)
        b9.grid(sticky="E", row=6, column=2, padx=50)

        b10 = Button(root, text="St", width=10)
        b10.grid(row=8, column=2)


root = Tk()
Window(root)
root.mainloop()