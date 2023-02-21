
# import tkinter as tk
#
# app = tk.Tk()
# app.geometry("400x200")
#
# entryExample = tk.Entry(app,
#                         width=5)
#
# entryExample.pack(side=tk.LEFT,
#                   padx=10)
#
# app.mainloop()


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



# dict1 = {'hello': [1,2,3]}
# print(dict1['hello'][2])


# ENUMERATE()
# list1 = ['hello', 'bye']
# print(list(enumerate(list1)))
#
# for x, y in enumerate(list1):
#     print(x)
#     print(y)
#
# index = 0
# for value in list:
#     print(index, list)
#     list += 1



# ARGS / KWARGS

# *args is so you can add as many arguments inside a function without having to proprely right it
# e.g
#
# info function info(args*) I can then call that function with info("Name", 3, 5) whereas normally I should
# have created the function as such: def info(student_name, age, IQ)

# def info(*args):
#     print(*args)
#
# info("Name", 3, 7)


# def test(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#
# test(Name="Bap", Age=6)
#
# def intro(**data):
#     print("\nData type of argument:",type(data))
#
#     for key, value in data.items():
#         print("{} is {}".format(key,value))
#
# intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
# intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
