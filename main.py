import os
from random import choice,randint
# SYMBOLS = ['X','O']

def validarOpcion():

    opcion = input("Opcion: ")
    while not(opcion.isnumeric() and (int(opcion) > 0 or int(opcion) < 4)):
        opcion = input("ERROR!! Ingrese una opcion valida")
    opcion = int(opcion)
    return opcion

def printTable(space):
    print(f'''
            {space[0][0]} |  {space[0][1]}  | {space[0][2]}
        --------------------
            {space[1][0]} |  {space[1][1]}  | {space[1][2]}
        --------------------
            {space[2][0]} |  {space[2][0]}  | {space[2][0]}
        ''')

def validarGame(table):
    for x in table:
        for col in x:
            pass

def playGame():
    space = [[" "," "," "],
            [" "," "," "],
            [" "," "," "]]
    estado = True
    while(estado):
        printTable(space)
        print("Fila")
        fila = validarOpcion()
        print("Columna")
        columna = validarOpcion()
        while not (space[fila-1][columna-1] == " "):    
            print("ERROR")
            fila = validarOpcion()
            print("Columna")
            columna = validarOpcion()
        space[fila-1][columna-1] = "X"
        
        random_choice = randint(0,8)
        fila = random_choice
        columna = random_choice
        while not (space[fila-1][columna-1] == " "):
            fila = random_choice
            columna = random_choice

def play():
    print('''
    ╔╦╗╦╦╔═  ╔╦╗╔═╗╦╔═  ╔╦╗╔═╗╔═╗
     ║ ║╠╩╗   ║ ║ ║╠╩╗   ║ ║ ║║╣ 
     ╩ ╩╩ ╩   ╩ ╚═╝╩ ╩   ╩ ╚═╝╚═╝
    ''')
    
    status = True
    while (status):
        print("1. Play with IA")
        print("2. Play with 2 player")
        print("3. Salir")
        
        opcion = validarOpcion()
        
        if (opcion == 1):
            playGame()
        else:
            if (opcion == 2):
                playGame()
            else:
                status = False

def main():
    
    play()

main()