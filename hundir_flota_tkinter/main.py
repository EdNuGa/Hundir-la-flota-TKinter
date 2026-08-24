from tkinter import ttk
import os
import tkinter as tk
import sqlite3
from tkinter import messagebox
from login import login
from database import *
from frameController import *

###
### HORAS QUE LLEVO AQUÍ: MÁS DE LAS QUE ME GUSTARÍA
###

default = tk.Tk()
default.title("Login")
# Styles
style = ttk.Style()
style.configure('TButton', background='red')
style.configure('TButton', font=('roboto', 10), borderwidth='4')
style.configure('Label.TLabel', font=('Arial', 12))
style.map('TButton', foreground=[('active', '!disabled', 'Navy Blue')], background=[
          ('active', 'Navy Blue'), ('!disabled', 'black')], )

# Create Database
createDb()

default.geometry("1050x369")
default.resizable(False, False)
default.config(bg="blue")
default.config(relief="sunken")
default.config(bd=25)
# titleLabel = tk.Label(default, text="logeasion en la base de datos", font=("Arial", 14, "bold")).place(x=50, y=5)

# LEFT FRAME
leftFrame(default)

# MID FRAME
midFrame(default)

# RIGHT FRAME
rightFrame(default)

default.mainloop()


