import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


import tkinter as tk
import numpy as np
from decimal import getcontext

getcontext().prec = 30

class Calculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Pixel")

        # Labels
        self.num1_label = tk.Label(self, text=">>:")
        self.num1_label.grid(row=0, column=0)

        self.num2_label = tk.Label(self, text=">>:")
        self.num2_label.grid(row=1, column=0)

        self.result_label = tk.Label(self, text=":")
        self.result_label.grid(row=2, column=0)

        self.result_value = tk.Label(self, fg="red")
        self.result_value.grid(row=2, column=1)

        # Entries
        self.num1_entry = tk.Entry(self)
        self.num1_entry.grid(row=0, column=1, columnspan=1)

        self.num2_entry = tk.Entry(self)
        self.num2_entry.grid(row=1, column=1, columnspan=1)

        self.cos_entry = tk.Entry(self)
        self.cos_entry.grid(row=0, column=4, columnspan=1)

        self.sin_entry = tk.Entry(self)
        self.sin_entry.grid(row=1, column=4, columnspan=1)

        self.tan_entry = tk.Entry(self)
        self.tan_entry.grid(row=2, column=4, columnspan=1)

        self.sqrt_entry = tk.Entry(self)
        self.sqrt_entry.grid(row=3, column=4, columnspan=1)

        self.exp_entry = tk.Entry(self)
        self.exp_entry.grid(row=4, column=4, columnspan=1)

        # Buttons
        self.add_button = tk.Button(self, text="+", font=(" bold ", 12), fg="green", command=self.add)
        self.add_button.grid(row=3, column=0, padx=2, pady=5, ipadx=2, ipady=2, columnspan=1)

        self.subtract_button = tk.Button(self, text="-", font=(" bold ", 12), fg="green", command=self.subtract)
        self.subtract_button.grid(row=4, column=0, padx=2, pady=5, ipadx=2, ipady=2, columnspan=1)

        self.multiply_button = tk.Button(self, text="*", font=(" bold ", 12), fg="green", command=self.multiply)
        self.multiply_button.grid(row=5, column=0, padx=2, pady=5, ipadx=2, ipady=2, columnspan=1)

        self.divide_button = tk.Button(self, text="/", font=(" bold ", 12), fg="green", command=self.divide)
        self.divide_button.grid(row=6, column=0, padx=2, pady=5, ipadx=2, ipady=2, columnspan=1)

        self.cos_button = tk.Button(self, text="cos", fg="green", command=self.cos)
        self.cos_button.grid(row=0, column=3, sticky="w", padx=5, pady=10, ipadx=0, ipady=0, columnspan=1)

        self.sin_button = tk.Button(self, text="sin", fg="green", command=self.sin)
        self.sin_button.grid(row=1, column=3, sticky="w", padx=5, pady=10, ipadx=0, ipady=0, columnspan=1)

        self.tan_button = tk.Button(self, text="tan", fg="green", command=self.tan)
        self.tan_button.grid(row=2, column=3, sticky="w", padx=5, pady=10, ipadx=0, ipady=0, columnspan=1)

        self.sqrt_button = tk.Button(self, text=" √ ", fg="green", command=self.sqrt)
        self.sqrt_button.grid(row=3, column=3, sticky="w", padx=5, pady=10, ipadx=0, ipady=0, columnspan=1)

        self.exp_button = tk.Button(self, text="e^?", fg="green", command=self.exp)
        self.exp_button.grid(row=4, column=3, sticky="w", padx=5, pady=10, ipadx=0, ipady=0, columnspan=1)



        # Center the widget on the screen
        self.grid(padx=10, pady=10)
        self.master.update()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))


    def add(self):
        add_input1 = self.num1_entry.get()
        add_input2 = self.num2_entry.get()
        if add_input1 == '':
            self.result_value.configure(text='Please enter a value for >>')
            return
        if add_input2 == '':
            self.result_value.configure(text='Please enter a value for >>')
            return
        num1 = float(add_input1)
        num2 = float(add_input2)
        result = np.add(num1, num2)
        self.result_value.configure(text=str(result))

    def subtract(self):
        subtract_input1 = self.num1_entry.get()
        subtract_input2 = self.num2_entry.get()
        if subtract_input1 == '':
            self.result_value.configure(text='Please enter a value for >>')
            return
        if subtract_input2 == '':
            self.result_value.configure(text='Please enter a value for >>')
            return
        num1 = float(subtract_input1)
        num2 = float(subtract_input2)
        result = np.subtract(num1, num2)
        self.result_value.configure(text=str(result))

    def multiply(self):
        multiply_input1 = self.num1_entry.get()
        multiply_input2 = self.num2_entry.get()
        if multiply_input1 == '':
            self.result_value.configure(text='Please enter a value for >>')
            return
        if multiply_input2 == '':
            self.result_value.configure(text='Please enter a value for >>')
            return
        num1 = float(multiply_input1)
        num2 = float(multiply_input2)
        result = np.multiply(num1, num2)
        self.result_value.configure(text=str(result))

    def divide(self):
        divide_input1 = self.num1_entry.get()
        divide_input2 = self.num2_entry.get()
        if divide_input1 == '':
            self.result_value.configure(text='Please enter a value for >>')
            return
        if divide_input2 == '':
            self.result_value.configure(text='Please enter a value for >>')
            return
        num1 = float(divide_input1)
        num2 = float(divide_input2)

        result = np.divide(num1, num2)
        self.result_value.configure(text=str(result))

    def cos(self):
        cos_input = self.cos_entry.get()
        if cos_input == '':
            self.result_value.configure(text='Please enter a value for cos')
            return
        cos = float(cos_input)
        cos1 = np.deg2rad(cos)
        cos2 = np.cos(cos1)
        result = round(cos2, 5)
        self.result_value.configure(text=str(result))

    def sin(self):
        sin_input = self.sin_entry.get()
        if sin_input == '':
            self.result_value.configure(text='Please enter a value for sin')
            return
        sin = float(sin_input)
        sin1 = np.deg2rad(sin)
        sin2 = np.sin(sin1)  # Use np.sin instead of np.cos
        result = round(sin2, 5)
        self.result_value.configure(text=str(result))

    def tan(self):
        tan_input = self.tan_entry.get()
        if tan_input == '':
            self.result_value.configure(text='Please enter a value for tan')
            return
        tan = float(tan_input)
        tan1 = np.deg2rad(tan)
        tan2 = np.tan(tan1)
        result = round(tan2, 5)
        self.result_value.configure(text=str(result))

    def sqrt(self):
        sqrt_input = self.sqrt_entry.get()
        if sqrt_input == '':
            self.result_value.configure(text='Please enter a value for √')
            return
        sqrt = float(sqrt_input)
        result = round(sqrt ** 0.5, 5)
        self.result_value.configure(text=str(result))

    def exp(self):
        exp_input = self.exp_entry.get()
        if exp_input == '':
            self.result_value.configure(text='Please enter a value for ?')
            return
        exp = float(exp_input)
        result = round(np.exp(exp), 5)
        self.result_value.configure(text=str(result))


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
