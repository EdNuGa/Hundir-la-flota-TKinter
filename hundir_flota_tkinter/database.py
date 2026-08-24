import os
import tkinter as tk
import sqlite3
from tkinter import messagebox
# Folder Name
dbOriginDir = "db"
# Database Name
dbName = "gameN.db"
# Full Database Path
# fullDbPath = dbOriginDir + "/" + dbName
fullDbPath = os.path.join(os.path.dirname(__file__), dbOriginDir, dbName)



def selectImage(nickname):
    # Conexión a la base de datos.
    conectar = sqlite3.connect(fullDbPath)
    cursor = conectar.cursor()
    cursor.execute(
        "SELECT imagePath FROM players WHERE nickname=?", (nickname, ))

    results = cursor.fetchall()
    return results[0][0]


def selectScore(nickname):
    # Conexión a la base de datos.
    conectar = sqlite3.connect(fullDbPath)
    cursor = conectar.cursor()
    cursor.execute("SELECT score FROM players WHERE nickname=?", (nickname, ))

    result = cursor.fetchone()
    return result


def selectGamesPlayed(nickname):
    # Conexión a la base de datos.
    conectar = sqlite3.connect(fullDbPath)
    cursor = conectar.cursor()
    cursor.execute(
        "SELECT gamesPlayed FROM players WHERE nickname=?", (nickname, ))

    result = cursor.fetchone()
    return result


def selectNickname(nickname):
    # Conexión a la base de datos.
    conectar = sqlite3.connect(fullDbPath)
    cursor = conectar.cursor()
    cursor.execute("SELECT * FROM players WHERE nickname=?", (nickname, ))

    results = cursor.fetchall()
    return results


def insertUser(nickEnt, passwdEnt, infoLabel):
    # Conexión a la base de datos.
    conectar = sqlite3.connect(fullDbPath)
    cursor = conectar.cursor()
    # Mientras no haya ningún campo vacío.
    if nickEnt.get() and passwdEnt.get():
        try:
            # Envía los datos.
            cursor.execute("INSERT INTO players (nickname, password) VALUES (?, ?)",
                           (nickEnt.get(), passwdEnt.get()))
            conectar.commit()
            infoLabel.config(text="Cuenta creada", fg="green")
            # Borra los campos.
            nickEnt.delete(0, tk.END)
            passwdEnt.delete(0, tk.END)
        # Si el nickname ya existe, salta excepción.
        except sqlite3.IntegrityError:
            infoLabel.config(text="El nombre '"+ nickEnt.get() +"' ya está en uso", fg="red")
    else:
        infoLabel.config(text="Porfavor completa todos los campos", fg="red")
    conectar.close()

#Conecta a la base de datos para obtener información del jugador.
def updateInfoGame(nickname, newGamesPlayed, newScore):
    #Reemplaza con la ruta correcta de tu base de datos.
    conectar = sqlite3.connect(fullDbPath)
    cursor = conectar.cursor()

    #Actualiza la información del juego para el jugador.
    cursor.execute("UPDATE players SET gamesPlayed=?, score=? WHERE nickname=?",
                   (newGamesPlayed, newScore, nickname))

    #Confirma la operación y cierra la conexión.
    conectar.commit()
    conectar.close()

def updateUserName(name, newUsername):
    try:
        conectar = sqlite3.connect(fullDbPath)
        cursor = conectar.cursor()
        cursor.execute("UPDATE players SET nickname = ? WHERE nickname = ?", (newUsername, name))

        conectar.commit()
        conectar.close()
        return True
    except:
        return False

def updateUserPassword(name, newPassword):
    try:
        conectar = sqlite3.connect(fullDbPath)
        cursor = conectar.cursor()

        cursor.execute("UPDATE players SET password = ? WHERE nickname = ?", (newPassword, name))

        conectar.commit()
        conectar.close()
        return True
    except:
        return False



def updateFilePath(imagePath, username):
    conectar = sqlite3.connect(fullDbPath)
    cursor = conectar.cursor()

    cursor.execute(
        "UPDATE players SET imagePath = ? WHERE nickname = ?", (imagePath, username))

    conectar.commit()
    conectar.close()

def deleteUserDb(user):
    conectar = sqlite3.connect(fullDbPath)
    cursor = conectar.cursor()

    cursor.execute("DELETE FROM players WHERE nickname = ?", (user,))

    conectar.commit()
    conectar.close()
    return True

def exitUser(window):
    window.destroy()


def createDb():

    # Si la ruta no existe creas la carpeta
    if not os.path.exists(dbOriginDir):
        os.mkdir(dbOriginDir)

    initialdir = os.getcwd()
    path = fullDbPath
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            nickname TEXT PRIMARY KEY,
            password TEXT,
            imagePath TEXT,
            gamesPlayed TEXT,
            score TEXT
        )
    """)
    connect.commit()
    connect.close()
