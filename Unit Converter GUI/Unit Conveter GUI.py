import tkinter as tk

class unit_converter:
    # Distance
    KILOMETERS_PER_MILE = 1.60934
    MILES_PER_KILOMETER = 0.62137

    # Mass
    KILOGRAMS_PER_POUND = 0.45359
    POUNDS_PER_KILOGRAM = 2.20462

    # Temperature
    DIFFERENCE = 32 # distance between the Celsius and Fahrenheit scale
    CELSIUS_TO_FAHRENHEIT = 9/5
    FAHRENHEIT_TO_CELSIUS = 5/9

    '''Sets up window'''
    def __init__(self):
        # main window
        self.root = tk.Tk()
        self.root.title('Unit Converter')

        # main subdivisions
        self.top = tk.Frame(self.root)
        self.bottom = tk.Frame(self.root)
        # bottom subdivisions
        self.row1 = tk.Frame(self.bottom)
        self.row2 = tk.Frame(self.bottom)
        self.row3 = tk.Frame(self.bottom)
        # fields
        self.inputField = tk.Entry(self.top, width=5)
        self.arrow = tk.Label(self.top, text='——>')
        self.outputField = tk.Label(self.top, width=5)
        # buttons
        self.milesToKm = tk.Button(self.row1, text='Miles to Km', command=self.miles_to_km)
        self.kmToMiles = tk.Button(self.row1, text='Km to Miles', command=self.km_to_miles)
        self.lbsToKg = tk.Button(self.row2, text='Pounds to Kg', command=self.lbs_to_kg)
        self.kgToLbs = tk.Button(self.row2, text='Kg to Pounds', command=self.kg_to_lbs)
        self.fToC = tk.Button(self.row3, text='ºF to ºC', command=self.F_to_C)
        self.cToF = tk.Button(self.row3, text='ºC to ºF', command=self.C_to_F)

        # packing fields
        self.inputField.pack(side='left')
        self.arrow.pack(side='left')
        self.outputField.pack(side='left')
        # packing buttons
        self.milesToKm.pack(side='left')
        self.kmToMiles.pack(side='left')
        self.lbsToKg.pack(side='left')
        self.kgToLbs.pack(side='left')
        self.fToC.pack(side='left')
        self.cToF.pack(side='left')
        # packing rows
        self.row1.pack()
        self.row2.pack()
        self.row3.pack()
        # packing top level frames
        self.top.pack()
        self.bottom.pack()

        # main loop
        self.root.mainloop()

    '''Convert input'''
    def miles_to_km(self):
        miles = float(self.inputField.get())
        km = round(miles * self.KILOMETERS_PER_MILE, 2)
        km = str(km) + ' km'
        self.outputField.destroy()
        self.outputField = tk.Label(self.top, text=km)
        self.outputField.pack(side='left')
    
    def km_to_miles(self):
        km = float(self.inputField.get())
        miles = round(km * self.MILES_PER_KILOMETER, 2)
        miles = str(miles) + ' miles'
        self.outputField.destroy()
        self.outputField = tk.Label(self.top, text=miles)
        self.outputField.pack(side='left')
    
    def lbs_to_kg(self):
        lbs = float(self.inputField.get())
        kg = round(lbs * self.KILOGRAMS_PER_POUND, 2)
        kg = str(kg) + ' kg'
        self.outputField.destroy()
        self.outputField = tk.Label(self.top, text=kg)
        self.outputField.pack(side='left')

    def kg_to_lbs(self):
        kg = float(self.inputField.get())
        lbs = round(kg * self.POUNDS_PER_KILOGRAM, 2)
        lbs = str(lbs) + ' lbs'
        self.outputField.destroy()
        self.outputField = tk.Label(self.top, text=lbs)
        self.outputField.pack(side='left')

    def F_to_C(self):
        F = float(self.inputField.get())
        C = round(self.FAHRENHEIT_TO_CELSIUS * (F - 32), 2)
        C = str(C) + ' ºC'
        self.outputField.destroy()
        self.outputField = tk.Label(self.top, text=C)
        self.outputField.pack(side='left')

    def C_to_F(self):
        C = float(self.inputField.get())
        F = round((self.CELSIUS_TO_FAHRENHEIT * C) + 32, 2)
        F = str(F) + ' ºF'
        self.outputField.destroy()
        self.outputField = tk.Label(self.top, text=F)
        self.outputField.pack(side='left')

app = unit_converter()
