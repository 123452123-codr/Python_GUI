import tkinter as tk
from tkinter import *

window = Tk()
Label(window, text='Username:').grid(row=0)
Label(window, text='Password:').grid(row=1)
e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

mainloop()
