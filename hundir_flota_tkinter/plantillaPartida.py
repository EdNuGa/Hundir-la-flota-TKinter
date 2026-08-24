import random

#Variables con tres tipos de barcos, ajustables en tamaño y número.
#Se pueden añadir más variedad de barcos, pero habrá que añadir una función de creación además de la variable.
crucero = [1, 4]
fragata = [1, 3]
lancha = [1, 2]
victoria = (crucero[0]*crucero[1]) + (fragata[0]*fragata[1]) + (lancha[0]*lancha[1])

columna = 0
fila = []

#Elige una coordenada al azar.
def newCoordinate():
    #Variables globales:
    #Tablero contiene un array de todas las filas y columnas (Diferentes arrays).
    global tablero
    global fila
    global columna
    #Determina la columna de forma aleatoria.
    columna = random.randint(3, 11)
    #Determina la fila de forma aleatoria.
    fila = random.choice(['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9'])
    #Obtenemos el número de fila dentro de tablero.
    indice = tablero.index([i for i in tablero if i[0] == fila][0])
    #Devolvemos el valor de la columna y el valor de la fila.
    valor = [columna, indice]
    return valor

#Comprueba que la coordenada sea válida.
def validCoordinate(tablero, fila, columna):
    #Comprueba que la coordenada ofrecida esté dentro del rango del tablero jugable.
    if 0 <= fila < len(tablero) and 0 <= columna < len(tablero[0]):
        #Comprueba que la coordenada inicial sea mar (Valor 0).
        if tablero[fila][columna] == 0:
            #Comprueba que las casillas alrededor de la coordenada sea mar (Valor 0).
            if tablero[fila+1][columna] == 0 and tablero[fila-1][columna] == 0 and tablero[fila][columna+1] == 0 and tablero[fila][columna-1] == 0:
                if tablero[fila+1][columna+1] == 0 and tablero[fila+1][columna-1] == 0 and tablero[fila-1][columna+1] == 0 and tablero[fila-1][columna-1] == 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

#Obtiene una posición aleatoria, comprueba que sea válida y coloca los barcos.
def placeBoat(largo, barcos):
    global tablero
    #Obtención de la posición de newCoordinate y la almacenamos en posicion.
    posicion = newCoordinate()
    #Obtención de la columna y la fila (índice en array tablero) por separado.
    columna = posicion[0]
    indice = posicion[1]
    fila = tablero[indice]
    #Obtención de la posición en el tablero.
    localizacion = fila[columna]
    #Obtención de una dirección (Norte, sur, este y oeste) al azar mediante rando.randint.
    direccion = random.randint(0, 7)
    #Comprueba la coordenada de newCoordinate y la dirección obtenida para saber si el barco puede ser colocado sobre el tablero.
    viable = 0
    if validCoordinate(tablero,indice,columna):
        if direccion <= 1:
            # abajo indice +1.
            apuntar = "sur"
            for i in range(largo):
                if validCoordinate(tablero,indice+i,columna):
                    viable = viable + 1
                else:
                    viable = viable + 0
        elif direccion <= 3:
            # derecha columna +1.
            apuntar = "este"
            for i in range(largo):
                if validCoordinate(tablero,indice,columna+i):
                    viable = viable + 1
                else:
                    viable = viable + 0
        elif direccion <= 5:
            #arriba indice-1.
            apuntar = "norte"
            for i in range(largo):
                if validCoordinate(tablero,indice-i,columna):
                    viable = viable + 1
                else:
                    viable = viable + 0
        else:
            #izquierda columna -1.
            apuntar = "oeste"
            for i in range(largo):
                if validCoordinate(tablero,indice,columna-i):
                    viable = viable + 1
                else:
                    viable = viable + 0
    if viable == largo:
        print(f"Barco de longitud {largo} colocado correctamente.")
        for i in range(largo):
            if apuntar == "sur":
                # indice-1.
                tablero[indice + i][columna] = 2
            elif apuntar == "este":
                # columna-1.
                fila[columna + i] = 2
            elif apuntar == "norte":
                # indice+1.
                tablero[indice - i][columna] = 2
            elif apuntar == "oeste":
                # indice+1.
                fila[columna - i] = 2
    else:
        placeBoat(largo, barcos)

#Funciones para colocar cada barco, pasándole los valores de las variables iniciales.
def newCruiser():
    global crucero
    barcos = crucero[0]
    largo = crucero[1]
    placeBoat(largo, barcos)

def newFrigate():
    global fragata
    barcos = fragata[0]
    largo = fragata[1]
    placeBoat(largo, barcos)

def newBoat():
    global lancha
    barcos = lancha[0]
    largo = lancha[1]
    placeBoat(largo, barcos)

def boardGame():
    for i in tablero:
        print(str(i) + "\n")

#Tablero de juego.
fA = ["f0", "c0", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"]
f0 = ["f0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "c10"]
f1 = ["f1", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "c10"]
f2 = ["f2", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "c10"]
f3 = ["f3", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "c10"]
f4 = ["f4", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "c10"]
f5 = ["f5", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "c10"]
f6 = ["f6", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "c10"]
f7 = ["f7", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "c10"]
f8 = ["f8", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "c10"]
f9 = ["f9", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "c10"]
f10 = ["f10", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "c10"]
fB = ["f10", "c0", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"]

tablero = [fA, f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, fB]

