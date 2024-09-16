import tkinter as tk
from tkinter import ttk
import math

# --- Calculator Functions ---
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + number)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        expression = display.get()
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def add_operator(operator):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + operator)

def square_root():
    try:
        number = float(display.get())
        result = math.sqrt(number)
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def power():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + "**")

def factorial():
    try:
        number = int(display.get())
        result = math.factorial(number)
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def sin():
    try:
        number = float(display.get())
        result = math.sin(math.radians(number))  # Convert to radians
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def cos():
    try:
        number = float(display.get())
        result = math.cos(math.radians(number))  # Convert to radians
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def tan():
    try:
        number = float(display.get())
        result = math.tan(math.radians(number))  # Convert to radians
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def log():
    try:
        number = float(display.get())
        result = math.log10(number)
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# --- Create the Calculator Window ---
root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg="#222")  # Dark gray background

# --- Display Screen ---
display = tk.Entry(root, width=30, borderwidth=5, bg="#444", fg="#eee", font=("Arial", 14))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# --- Number Buttons ---
button_7 = tk.Button(root, text="7", width=5, command=lambda: button_click("7"), bg="#333", fg="#eee", font=("Arial", 12))
button_7.grid(row=1, column=0, padx=5, pady=5)
button_8 = tk.Button(root, text="8", width=5, command=lambda: button_click("8"), bg="#333", fg="#eee", font=("Arial", 12))
button_8.grid(row=1, column=1, padx=5, pady=5)
button_9 = tk.Button(root, text="9", width=5, command=lambda: button_click("9"), bg="#333", fg="#eee", font=("Arial", 12))
button_9.grid(row=1, column=2, padx=5, pady=5)
button_4 = tk.Button(root, text="4", width=5, command=lambda: button_click("4"), bg="#333", fg="#eee", font=("Arial", 12))
button_4.grid(row=2, column=0, padx=5, pady=5)
button_5 = tk.Button(root, text="5", width=5, command=lambda: button_click("5"), bg="#333", fg="#eee", font=("Arial", 12))
button_5.grid(row=2, column=1, padx=5, pady=5)
button_6 = tk.Button(root, text="6", width=5, command=lambda: button_click("6"), bg="#333", fg="#eee", font=("Arial", 12))
button_6.grid(row=2, column=2, padx=5, pady=5)
button_1 = tk.Button(root, text="1", width=5, command=lambda: button_click("1"), bg="#333", fg="#eee", font=("Arial", 12))
button_1.grid(row=3, column=0, padx=5, pady=5)
button_2 = tk.Button(root, text="2", width=5, command=lambda: button_click("2"), bg="#333", fg="#eee", font=("Arial", 12))
button_2.grid(row=3, column=1, padx=5, pady=5)
button_3 = tk.Button(root, text="3", width=5, command=lambda: button_click("3"), bg="#333", fg="#eee", font=("Arial", 12))
button_3.grid(row=3, column=2, padx=5, pady=5)
button_0 = tk.Button(root, text="0", width=5, command=lambda: button_click("0"), bg="#333", fg="#eee", font=("Arial", 12))
button_0.grid(row=4, column=0, padx=5, pady=5)
button_dot = tk.Button(root, text=".", width=5, command=lambda: button_click("."), bg="#333", fg="#eee", font=("Arial", 12))
button_dot.grid(row=4, column=1, padx=5, pady=5)

# --- Operator Buttons ---
button_add = tk.Button(root, text="+", width=5, command=lambda: add_operator("+"), bg="#FFA500", fg="#eee", font=("Arial", 12))
button_add.grid(row=1, column=3, padx=5, pady=5)
button_subtract = tk.Button(root, text="-", width=5, command=lambda: add_operator("-"), bg="#FFA500", fg="#eee", font=("Arial", 12))
button_subtract.grid(row=2, column=3, padx=5, pady=5)
button_multiply = tk.Button(root, text="*", width=5, command=lambda: add_operator("*"), bg="#FFA500", fg="#eee", font=("Arial", 12))
button_multiply.grid(row=3, column=3, padx=5, pady=5)
button_divide = tk.Button(root, text="/", width=5, command=lambda: add_operator("/"), bg="#FFA500", fg="#eee", font=("Arial", 12))
button_divide.grid(row=4, column=3, padx=5, pady=5)

# --- Function Buttons ---
button_clear = tk.Button(root, text="C", width=5, command=clear_display, bg="#007BFF", fg="#eee", font=("Arial", 12))
button_clear.grid(row=4, column=2, padx=5, pady=5)
button_equal = tk.Button(root, text="=", width=5, command=calculate, bg="#007BFF", fg="#eee", font=("Arial", 12))
button_equal.grid(row=5, column=3, padx=5, pady=5)
button_sqrt = tk.Button(root, text="√", width=5, command=square_root, bg="#007BFF", fg="#eee", font=("Arial", 12))
button_sqrt.grid(row=5, column=0, padx=5, pady=5)
button_power = tk.Button(root, text="^", width=5, command=power, bg="#007BFF", fg="#eee", font=("Arial", 12))
button_power.grid(row=5, column=1, padx=5, pady=5)
button_factorial = tk.Button(root, text="!", width=5, command=factorial, bg="#007BFF", fg="#eee", font=("Arial", 12))
button_factorial.grid(row=5, column=2, padx=5, pady=5)
button_sin = tk.Button(root, text="sin", width=5, command=sin, bg="#007BFF", fg="#eee", font=("Arial", 12))
button_sin.grid(row=6, column=0, padx=5, pady=5)
button_cos = tk.Button(root, text="cos", width=5, command=cos, bg="#007BFF", fg="#eee", font=("Arial", 12))
button_cos.grid(row=6, column=1, padx=5, pady=5)
button_tan = tk.Button(root, text="tan", width=5, command=tan, bg="#007BFF", fg="#eee", font=("Arial", 12))
button_tan.grid(row=6, column=2, padx=5, pady=5)
button_log = tk.Button(root, text="log", width=5, command=log, bg="#007BFF", fg="#eee", font=("Arial", 12))
button_log.grid(row=6, column=3, padx=5, pady=5)

root.mainloop()
