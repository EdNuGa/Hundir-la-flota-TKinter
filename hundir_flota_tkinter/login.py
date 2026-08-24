from tkinter import ttk
import os
import tkinter as tk
import sqlite3
from tkinter import messagebox


from database import *
contador = 0

def login(nickname, password, defaultWindow,):
    global contador
    results = selectNickname(nickname) #Resultados de la query
    max_intentos = 3  # Número máximo de intentos permitidos

    if(len(results) == 0):
        messagebox.showerror(title=None, message="El usuario '" + nickname +"' no existe")
        
        return False
    
    for userInfo in results:
        if password == userInfo[1]:
            messagebox.showinfo(title=None, message="Bienvenido, "+ userInfo[0])
            contador = 0
            return True
        else:
            contador = contador + 1
            messagebox.showerror(title=None, message="Error en la conexión, quedan " + str(max_intentos - contador) + " intentos")
            if contador >= max_intentos:
                messagebox.showerror(title=None, message="Máximo de intentos alcanzado, cerrando aplicación")
                defaultWindow.destroy()
    return False




   