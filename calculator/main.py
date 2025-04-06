import tkinter as tk
from tkinter import messagebox

# Functions for operations
def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            label_result.config(text="Error! Cannot Divide by Zero.")
        else:
            result = num1 / num2
            label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Function to clear inputs and result
def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    label_result.config(text="Result: ")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Input fields
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Buttons for operations
tk.Button(root, text="Add", command=add).grid(row=2, column=0, padx=10, pady=5)
tk.Button(root, text="Subtract", command=subtract).grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Multiply", command=multiply).grid(row=3, column=0, padx=10, pady=5)
tk.Button(root, text="Divide", command=divide).grid(row=3, column=1, padx=10, pady=5)

# Clear button
tk.Button(root, text="Clear", command=clear).grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Result label
label_result = tk.Label(root, text="Result: ")
label_result.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()