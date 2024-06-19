import tkinter as tk
from tkinter import messagebox

def show_height():
    height = entry.get()
    if height.isdigit():
        messagebox.showinfo("Result", f"Your height is {height}cm!")
    else:
        messagebox.showerror("Invalid input", "Please enter a valid height in cm.")

# Create the main window
root = tk.Tk()
root.title("Height caculator tool")

# Create and place the widgets
label = tk.Label(root, text="Input your height")
label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

button = tk.Button(root, text="Xem", command=show_height)
button.grid(row=0, column=2, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
