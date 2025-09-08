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
root.title("Calculator GUI")

tk.Label(root, text="First Number: ").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root,text="Second Number (for opreation needing 2 numbers): ")
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root,text="Operation(+, -, *, /, sqrt, root, pi)").pack()
opration = tk.Entry(root)
opration.pack()

btn = tk.Button(root,text="Calculate", command=calculate)
btn.pack()

label_result = tk.Label(root,text="Result: ")
label_result.pack()

root.mainloop()
