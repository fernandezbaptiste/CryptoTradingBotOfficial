# class Parent:
#     def __init__(self, value):
#         self.value = value
#
#     def display(self):
#         print("Parent class:", self.value)
#
# class Child(Parent):
#     def __init__(self, value):
#         super().__init__(value)
#
#     def display(self):
#         # super().display()
#         print("Child class:", self.value)
#
# c = Child("Hello")
# c.display()

import tkinter as tk
app = tk.Tk()
app.geometry("400x200")
entryExample = tk.Entry(app,
                        width=5)
entryExample.pack(side=tk.LEFT,
                  padx=10)
app.mainloop()

# Import the required library
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# Create an instance of tkinter frame
win=Tk()
# Set the geometry
win.geometry("700x350")
# Add a Scrollbar(horizontal)
h=Scrollbar(win, orient='horizontal')
h.pack(side=BOTTOM, fill='x')
# Add a text widget
text=Text(win, font=("Calibri, 16"), wrap=NONE, xscrollcommand=h.set)
text.pack()
# Add some text in the text widget
for i in range(5):
   text.insert(END, "Welcome to Tutorialspoint...")
# Attach the scrollbar with the text widget
h.config(command=text.xview)
win.mainloop()
