import os
import sqlite3
import tkinter as tk
from tkinter import font
from tkinter import messagebox
from plantillaPartida import *
from database import *

contador = 0
botPos = {}
score = 0
nickname = ""
newGamePlayed = 0

def boom(x, y, boton):
    global nickname
    global score
    global contador
    global victoria
    if tablero[x][y] == 0:
        #Deshabilitar el botón después de ser presionado.
        boton.config(bg="#9db7e2")
        boton.config(state=tk.DISABLED)
        contador = contador +1
        #Actualizar el label de información con la posición del botón presionado.
        infoLabel.config(text="Botón " + botPos[boton] + " presionado.\n¡Agua!")
    elif tablero[x][y] == 2:
        boton.config(bg="red3")
        boton.config(state=tk.DISABLED)
        contador = contador +1
        victoria = victoria -1
        #Actualizar la etiqueta con la posición del botón presionado.
        infoLabel.config(text="Botón " + botPos[boton] + " presionado.\n¡Impacto!")
        if victoria == 0:
            if contador < score:
                updateInfoGame(nickname, newGamePlayed, contador)
            messagebox.showinfo("¡Victoria!", "Has ganado en " + str(contador) + " intentos")
            root.destroy()
            
    
def createInterface(oldNickname):
    global nickname
    global score
    global newGamePlayed
    global root
    nickname = oldNickname
    nscore = selectScore(nickname)
    if nscore is None or nscore[0] is None:
        score = 100  # Asignar un valor predeterminado si nscore o nscore[0] es None
    else:
        score = int(nscore[0])
    
    nnewGamePlayed = selectGamesPlayed(nickname)
    if nnewGamePlayed is None or nnewGamePlayed[0] is None:
        newGamePlayed = 1  # Asignar un valor predeterminado si nnewGamePlayed o nnewGamePlayed[0] es None
    else:
        newGamePlayed = int(nnewGamePlayed[0]) + 1
    
    updateInfoGame(nickname, newGamePlayed, score)
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Hundir la flota")
    bold_font = font.Font(weight="bold")

    #Frame pantalla informativa.
    #Muestra información al jugador.
    global infoLabel
    infoLabel = tk.Label(root, text="Pantalla informativa", bg="lightgrey", pady="10", padx ="130")
    infoLabel.pack()
    #Frame tablero.
    boardFrame = tk.LabelFrame(root, bg="#9db7e2")
    boardFrame.pack()
    #Labels para mostrar las letras de cada columna en el tablero.
    colLabelE = tk.Label(boardFrame, text=" ", font=bold_font, bg="#9db7e2")
    colLabelE.grid(row=1,column=1)
    colLabelA = tk.Label(boardFrame, text="A", font=bold_font, bg="#9db7e2")
    colLabelA.grid(row=1,column=2)
    colLabelB = tk.Label(boardFrame, text="B", font=bold_font, bg="#9db7e2")
    colLabelB.grid(row=1,column=3)
    colLabelC = tk.Label(boardFrame, text="C", font=bold_font, bg="#9db7e2")
    colLabelC.grid(row=1,column=4)
    colLabelD = tk.Label(boardFrame, text="D", font=bold_font, bg="#9db7e2")
    colLabelD.grid(row=1,column=5)
    colLabelE = tk.Label(boardFrame, text="E", font=bold_font, bg="#9db7e2")
    colLabelE.grid(row=1,column=6)
    colLabelF = tk.Label(boardFrame, text="F", font=bold_font, bg="#9db7e2")
    colLabelF.grid(row=1,column=7)
    colLabelG = tk.Label(boardFrame, text="G", font=bold_font, bg="#9db7e2")
    colLabelG.grid(row=1,column=8)
    colLabelH = tk.Label(boardFrame, text="H", font=bold_font, bg="#9db7e2")
    colLabelH.grid(row=1,column=9)
    colLabelI = tk.Label(boardFrame, text="I", font=bold_font, bg="#9db7e2")
    colLabelI.grid(row=1,column=10)
    #Labels para mostrar el número de cada fila
    filLabel1 = tk.Label(boardFrame, text="1", font=bold_font, bg="#9db7e2")
    filLabel1.grid(row=2,column=1)
    filLabel2 = tk.Label(boardFrame, text="2", font=bold_font, bg="#9db7e2")
    filLabel2.grid(row=3,column=1)
    filLabel3 = tk.Label(boardFrame, text="3", font=bold_font, bg="#9db7e2")
    filLabel3.grid(row=4,column=1)
    filLabel4 = tk.Label(boardFrame, text="4", font=bold_font, bg="#9db7e2")
    filLabel4.grid(row=5,column=1)
    filLabel5 = tk.Label(boardFrame, text="5", font=bold_font, bg="#9db7e2")
    filLabel5.grid(row=6,column=1)
    filLabel6 = tk.Label(boardFrame, text="6", font=bold_font, bg="#9db7e2")
    filLabel6.grid(row=7,column=1)
    filLabel7 = tk.Label(boardFrame, text="7", font=bold_font, bg="#9db7e2")
    filLabel7.grid(row=8,column=1)
    filLabel8 = tk.Label(boardFrame, text="8", font=bold_font, bg="#9db7e2")
    filLabel8.grid(row=9,column=1)
    filLabel9 = tk.Label(boardFrame, text="9", font=bold_font, bg="#9db7e2")
    filLabel9.grid(row=10,column=1)
    #Filas.
    for i in range(2, 11):
        posCol = [0,0,'A','B','C','D','E','F','G','H','I']
        #Columnas.
        for j in range(2, 11):
            button = tk.Button(boardFrame, bg="white", pady="5", padx="15")
            button.grid(row=i, column=j)
            # Asociar la función lambda al evento clic del botón, si se le añade directamente no funciona.
            button.configure(command=lambda x=i, y=j, btn=button: boom(x, y, btn))
            botPos[button] = posCol[i] + str(j)
    
    root.mainloop()
