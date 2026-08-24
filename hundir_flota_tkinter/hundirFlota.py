from plantillaPartida import *
from tableroJuego import *

#Inicia el juego.
def hundirFlota(nickname):

    #Iniciar cruceros.
    for i in range(crucero[0]):
        newCruiser()
    #Iniciar fragatas.
    for i in range(fragata[0]):
        newFrigate()
    #Iniciar lanchas.
    for i in range(lancha[0]):
        newBoat()
    #Iniciar tablero.
    #Descomentar la siguiente línea mostrará la posición de los barcos por consola.
    #boardGame()
    createInterface(nickname)
    #createInterface()

