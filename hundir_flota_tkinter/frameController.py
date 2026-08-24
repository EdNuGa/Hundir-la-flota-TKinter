from tkinter import ttk
import os
import tkinter as tk
import sqlite3
from hundirFlota import *
from UserUtils import *
from database import *
from tkinter import messagebox
from PIL import Image, ImageTk
from login import *
from tkinter import filedialog as quelcom

import shutil

user1IsLogged = False
user2IsLogged = False
sendButton = None
usernameGlobal = None

def startAndDeleteFrame(usernameGlobal, default):
    #Elimino default
    default.destroy()
    #empiezo el juego
    hundirFlota(usernameGlobal)

def leftFrame(default):

    frameP1 = tk.Frame(default, width=400, height=320)
    frameP1.config(relief="sunken")
    frameP1.config(bd=25)
    frameP1.pack(side=tk.LEFT)
    frameP1.config(bg="lightblue")
    nickNameP1Label = ttk.Label(frameP1, text="Nombre: ")
    nickNameP1Entry = ttk.Entry(frameP1)
    passwordP1Label = ttk.Label(frameP1, text="Contraseña: ")
    passwordP1Entry = ttk.Entry(frameP1)
    nickNameP1Label.place(x=0, y=50)
    nickNameP1Entry.place(x=0, y=70)
    passwordP1Label.place(x=0, y=100)
    passwordP1Entry.place(x=0, y=120)
    
    #Llamo a la funcion logged siempre y cuando la función login sea true
    #Funcion logged // Param1 - Frame // Param2 - nickname // Param3 - el numero de frame (1 en este caso) // Param4 - El frame inicial // Param5 - usertype (0 en este caso, se utiliza para el juego)
    loginButtonP1 = ttk.Button(frameP1, text="Iniciar Sesion", command=lambda: (logged(
        frameP1, nickNameP1Entry.get(), 1, default, 0) if login(nickNameP1Entry.get(), passwordP1Entry.get(), default) == True else None))
    loginButtonP1.place(x=250, y=250)

def midFrame(default):
    global usernameGlobal
    gamesPlayed = selectGamesPlayed(usernameGlobal)
    score = selectScore(usernameGlobal)

    if gamesPlayed == None:
        gamesPlayed = 0
    if score == None:
        score = 100

    frameMid = tk.Frame(default, width=200, height=320)
    frameMid.config(relief="groove")
    frameMid.config(bd=25)
    frameMid.pack(side=tk.LEFT)
    frameMid.config(bg="gray")
    resetButton = ttk.Button(frameMid, text="Crear usuario", command=createUser)

    global sendButton
    #Funcion startAndDeleteFrame se encarga de iniciar el juego y eliminar el frame anterior
    # // Param1 - Nombre de usuario // Param2 - el frame principal
    sendButton = ttk.Button(frameMid, text="Empezar partida", state="disabled", command=lambda:startAndDeleteFrame(usernameGlobal, default))
    sendButton.place(x=25, y=100)
    resetButton.place(x=32, y=150)

def rightFrame(default):
    frameP2 = tk.Frame(default, width=400, height=320)
    frameP2.config(relief="sunken")
    frameP2.config(bd=25)
    frameP2.pack(side=tk.LEFT)
    frameP2.config(bg="tomato")
    nickNameP2Label = ttk.Label(frameP2, text="Nombre: ")
    nickNameP2Entry = ttk.Entry(frameP2)
    passwordP2Label = ttk.Label(frameP2, text="Contraseña: ")
    passwordP2Entry = ttk.Entry(frameP2)
    nickNameP2Label.place(x=0, y=50)
    nickNameP2Entry.place(x=0, y=70)
    passwordP2Label.place(x=0, y=100)
    passwordP2Entry.place(x=0, y=120)


    #Llamo a la funcion logged siempre y cuando la función login sea true
    #Funcion logged // Param1 - Frame // Param2 - nickname // Param3 - el numero de frame (2 en este caso) // Param4 - El frame inicial // Param5 - usertype (1 en este caso, se utiliza para el juego)
    loginButtonP2 = ttk.Button(frameP2, text="Iniciar Sesion", command=lambda: (logged(
        frameP2, nickNameP2Entry.get(),2,default,1) if login(nickNameP2Entry.get(), passwordP2Entry.get(), default) == True else None))
    loginButtonP2.place(x=250, y=250)
    
def clean(frame):
    #Guardo todos los items del frame en una variable
    allFrameItems = frame.winfo_children()
    #Por cada item dentro del frame hago destroy()
    for item in allFrameItems:
        item.destroy()
    return True
    

def resizeImage(imagePath, width, height):
    #Abro img
    original_image = Image.open(imagePath)
    #Redimensiono con los parametros
    resized_image = original_image.resize((width, height), Image.LANCZOS)
    #Retorno la imagen renderizada
    return ImageTk.PhotoImage(resized_image)

def showImage(name):
    userImg = ""
    imagesDirectory = os.path.join(os.path.dirname(__file__), 'images')
    
    imagePathFromDb = selectImage(name)
    if imagePathFromDb == None:
        userImg = os.path.join(imagesDirectory, "default_pfp.jpg")
        user_image = resizeImage(userImg, 200, 200)  # Redimensiona la imagen
    else:
        userImg = os.path.join(imagesDirectory, imagePathFromDb) #poraqui
        user_image = resizeImage(imagePathFromDb, 200, 200)  # Redimensiona la imagen
        #user_image = resizeImage(userImg, 200, 200)  # Redimensiona la imagen
    return user_image


def selectPfp(username, frame):
    file = quelcom.askopenfilename(initialdir="./", filetypes=(("Imágenes", "*.jpg"),))
    if file:
        destinationDir = "./images/"
        fileName = f"user_{username}_pfp.jpg"
        destinationPath = os.path.join(destinationDir, fileName)
        shutil.copy2(file, destinationPath)
        updateFilePath(destinationPath, username)
        reloadedImage = showImage(username)

        #Busco en el frame todos los elementos que sean instancia de ttk.label y que además sean una imagen, si lo encuentro lo elimino
        for widget in frame.winfo_children():
            if isinstance(widget, ttk.Label) and widget.cget("image"):
                widget.destroy()

        setUserPfp = ttk.Label(frame, image=reloadedImage)
        setUserPfp.photo = reloadedImage
        #Pongo la imagen en esta pos
        setUserPfp.place(x=147, y=20)
        

def remakeMidFrame():
    global sendButton, user1IsLogged, user2IsLogged
    if user1IsLogged and user2IsLogged:
        #Habilito el botón si ambos usuarios están logueados
        sendButton.config(state="normal")  
    else:
        #Deshabilito el botón si al menos uno de los usuarios no está logueado
        sendButton.config(state="disabled")  

def modifyUser(name):
    modUser(name)

def deleteUser(name, frame):
    result = messagebox.askquestion("Confirmar", "¿Estás seguro de que quieres eliminar la cuenta '" + name + "' ?")
    if result == 'yes':
        if deleteUserDb(name):
            messagebox.showinfo("Eliminado", "Usuario eliminado correctamente")
            frame.destroy()


def logged(frame, name, frameNum, globalFrame, usertype):
    global user1IsLogged, user2IsLogged, usernameGlobal
    if usertype == 0:
        usernameGlobal = name
        
    clean(frame)
        
    setNickNameLabel = ttk.Label(frame, text="Nombre: " + name)
    setNickNameLabel.place(x=0, y=20)
    gamesPlayed = selectGamesPlayed(name)
    score = selectScore(name)

    #Compruebo la base de datos que sea diferente a none
    if gamesPlayed[0] == None:
        gamesPlayed = 0
    if score[0] == None:
        score = "Ninguna"
        
    #Comprobaciones para que todo vaya fino
    if gamesPlayed != 0:
        gamesPlayed = gamesPlayed[0]
    if score != "Ninguna":
        score = score[0]

    setNickNameLabel = ttk.Label(frame, text="Veces Jugado: " +  str(gamesPlayed))
    setNickNameLabel.place(x=0, y=50)
    setNickNameLabel = ttk.Label(frame, text="Puntuación: " + str(score))
    setNickNameLabel.place(x=0, y=80)
    user_image = showImage(name)  
    setUserPfp = ttk.Label(frame, image=user_image)
    setUserPfp.photo = user_image  
    changePfpButton = ttk.Button(frame, text="Cambiar imagen", command=lambda: selectPfp(name, frame))
    changePfpButton.place(x=20, y=250)
    setUserPfp.place(x=147, y=20)
    modifyCredentials = ttk.Button(frame, text="Modificar", command=lambda: modifyUser(name))
    modifyCredentials.place(x=140, y=250)
    deleteUserButton = ttk.Button(frame, text="Eliminar Cuenta", command=lambda: deleteUser(name, globalFrame))
    deleteUserButton.place(x=243, y=250)

    if frameNum == 1:
        user1IsLogged = True
    elif frameNum == 2:
        user2IsLogged = True
    #Función para que el botón se quede habilitado
    remakeMidFrame()
    

