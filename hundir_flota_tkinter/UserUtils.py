from tkinter import ttk
import tkinter as tk
from database import *
from login import *
from tkinter import filedialog as quelcom

def checkEditUser(name, password):
    #Method es la manera de decirle si edito el nombre(0) o la contraseña (1)
    allUser = selectNickname(name)

    userDbName = allUser[0][0]
    userDbPassword = allUser[0][1]
    if userDbPassword == password:
        messagebox.showinfo("Funcionó! ","Te has verificado correctamente")
        return True
    else:
        messagebox.showinfo("Error", "Contraseña incorrecta")
        return False


def confirmUserIdentity(oldName, newName, newPassword, method):

    identity = tk.Tk()
    identity.title("Confirmar Identidad")
    identity.resizable(False, False)
    
    userLabel = tk.Label(identity, bg="#9db7e2")
    userLabel.pack()
    confLabel = tk.Label(userLabel, text="", bg="#9db7e2")
    confLabel.grid(row=1,column=0)
    buttonBox = tk.LabelFrame(identity, )
    buttonBox.pack()
    infoLabel = tk.Label(identity, text="")
    infoLabel.pack()
    nickName = tk.Label(userLabel, text="Introduce la contraseña de " + oldName , bg="#9db7e2")
    nickName.grid(row=0, column=0)
    labelPlayerPasswrd = tk.Label(confLabel, text="Contraseña: " , bg="#9db7e2")
    labelPlayerPasswrd.grid(row=1, column=0)
    passwrdEnt = tk.Entry(confLabel, show="*")
    passwrdEnt.grid(row=1, column=1)

    #Method 0 cambiar usuario, method 1 cambiar contraseña
    if method == 0:
        confirmIdentity = tk.Button(buttonBox, text="Continuar", bg="#ffa31a", command=lambda: saveName(oldName, newName) if checkEditUser(oldName, passwrdEnt.get()) else None)
        confirmIdentity.grid(row=0, column= 0)
    if method == 1:
        confirmIdentity = tk.Button(buttonBox, text="Continuar", bg="#ffa31a", command=lambda: savePassword(oldName, newPassword) if checkEditUser(oldName, passwrdEnt.get()) else None)
        confirmIdentity.grid(row=0, column= 0)


def saveName(oldUsername, newName):
    if updateUserName(oldUsername, newName):
        messagebox.showinfo("Funcionó!", "El usuario '" + oldUsername + "' se ha renombrado a '" + newName + "'\nReinicia la aplicación para que los cambios tengan efecto")
    else:
        messagebox.showerror("Error", "Reinicia la aplicación e intentalo de nuevo")

def savePassword(username, newPassword):
    if updateUserPassword(username, newPassword):
        messagebox.showinfo("Funcionó!", "Se ha cambiado la contraseña del usario '" + username + "'\nReinicia la aplicación para que los cambios tengan efecto")
    else:
        messagebox.showerror("Error", "Reinicia la aplicación e intentalo de nuevo")
    

def modUser(username):
    
    #allUser // 0 = nickname, 1 = password 2 = imagepath, 3 = gamesPlayed, 4 = score 
    allUser = selectNickname(username)

    editUser = tk.Tk()
    editUser.title("Editar Jugador")   
    editUser.geometry("300x300")
    editUser.resizable(False, False)
    
    title1 = ttk.Label(editUser, text="Datos del Usuario")
    title1.place(x=110, y=0)

    usernameLabel = ttk.Label(editUser, text="Nombre: " + allUser[0][0])
    usernameLabel.place(x=0, y=20)

    titleEditUser = ttk.Label(editUser, text="Modificar nombre de usuario")
    titleEditUser.place(x=75, y=50)

    newUsernameLabel = ttk.Label(editUser, text="Nombre: ")
    newUsernameLabel.place(x=0, y=80)

    newNicknameEntry = ttk.Entry(editUser)
    newNicknameEntry.place(x=125, y=80)

    saveNewNickname = tk.Button(editUser, text="Guardar Nombre", bg="#ffa31a", command=lambda: confirmUserIdentity(username, newNicknameEntry.get(), None, 0))
    saveNewNickname.place(x=100, y=110)

    titleEditPassword = ttk.Label(editUser, text="Modificar contraseña")
    titleEditPassword.place(x=110, y=140)

    newPasswordLabel0 = ttk.Label(editUser, text="Contraseña: ")
    newPasswordLabel0.place(x=0, y=170)

    newPaswordEntry0 = ttk.Entry(editUser)
    newPaswordEntry0.place(x=125, y=170)

    newPasswordLabel1 = ttk.Label(editUser, text="Repite la Contraseña: ")
    newPasswordLabel1.place(x=0, y=200)

    newPaswordEntry1 = ttk.Entry(editUser)
    newPaswordEntry1.place(x=125, y=200)

    saveNewPassword = tk.Button(editUser, text="Guardar Contraseña", bg="#ffa31a", command=lambda: 
    confirmUserIdentity(username, None, newPaswordEntry0.get(), 1) 
    if newPaswordEntry0.get() == newPaswordEntry1.get() else messagebox.showerror(
        title="Error", message="Las contraseñas no coinciden"
    ))
    saveNewPassword.place(x=90, y=230)




def createUser():
    newUser = tk.Tk()
    newUser.title("Ficha de jugador")   
    newUser.geometry("200x100")
    newUser.resizable(False, False)
    
    userLabel = tk.Label(newUser, bg="#9db7e2")
    userLabel.grid(row=0, column=0)
    buttonBox = tk.LabelFrame(newUser, )
    buttonBox.grid(row=1, column=0)
    infoLabel = tk.Label(newUser, text="")
    infoLabel.grid(row=2, column=0)
    nickName = tk.Label(userLabel, text="Nombre: " , bg="#9db7e2", font=(16))
    nickName.grid(row=0, column=0)
    nickEnt = tk.Entry(userLabel, )
    nickEnt.grid(row=0, column=1)
    playerPasswrd = tk.Label(userLabel, text="Contraseña: " , bg="#9db7e2",font=(16))
    playerPasswrd.grid(row=1, column=0)
    passwrdEnt = tk.Entry(userLabel, show="*")
    passwrdEnt.grid(row=1, column=1)
    
    savePlayer = tk.Button(buttonBox, text="Guardar jugador", bg="#ffa31a", command=lambda: insertUser(nickEnt, passwrdEnt, infoLabel))
    savePlayer.grid(row=0, column= 0)
    exitCreate = tk.Button(buttonBox, text="Cancelar", bg="#ffa31a", command=lambda: exitUser(newUser))
    exitCreate.grid(row=0, column= 1)
