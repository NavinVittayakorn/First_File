import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    try:
        number1 = float(entry1.get())if entry1.get()else None
        number2 = float(entry2.get())if entry2.get()else None
        op = opration.get()

        if op =="+":
            result = number1+number2
        elif op =="-":
            result = number1-number2
        elif op =="*":
            result = number1*number2
        elif op =="/":
            if number2 !=0:
                result = number1/number2
            else:
                result - "Error (Div by zero)"
        elif op =="sqrt":
            if number1 is not None and number1>=0:
                result = math.sqrt(number1)
            else:
                result = "Error (negative root)"
        elif op =="root":
            if number1 is not None and number1!=0:
                result = number1**(1/number2)
            else:
                result = "Error"
        elif op =="pi":
            result = math.pi
        else:
            result = "unknown op"
        label_result.config(text=f"result: {result}")
    except Exception as e:
        label_result.config(text=f"result: {result}")
root = tk.Tk()
root.geometry("800x600")
root.title("Calculator GUI")

tk.Label(root, text="Welcome! to my First GUI Calculator", font=("Times new roman", 35)).pack(padx=30, pady=30)

tk.Label(root, text="First Number: ", font=("Times new roman",15)).pack()
textbock1 = tk.Text(root, height=2)
textbock1.pack()

tk.Label(root,text="Second Number (For opration needing 2 numbers): ", font=("Times new roman",15)).pack()
textbock2 = tk.Text(root, height=2)
textbock2.pack()

tk.Label(root,text="Operation(+, -, *, /, sqrt, root, pi)", font=("Times new roman",15)).pack()
opration = tk.Text(root, height=2)
opration.pack()

btn = tk.Button(root,text="Calculate",font=("Times new roman",15), command=calculate)
btn.pack()

label_result = tk.Label(root,text="Result: ", font=("Times new roman", 15))
label_result.pack()

root.mainloop()



