import os
from random import choice
SYMBOLS = ['X','O']

def validarOpcion():

    opcion = input("Opcion: ")
    while not(opcion.isnumeric() and (opcion < 1 or opcion > 3)):
        opcion = input("ERROR!! Ingrese una opcion valida")
    return opcion

def printTable(space):
    print(f'''
        {space[0]} | {space[1]} | {space[2]}
        ------------------------------------
        {space[3]} | {space[4]} | {space[5]}
        ------------------------------------
        {space[6]} | {space[7]} | {space[8]}
        ''')

def playComputer():
    random_choice = choice(SYMBOLS)
    space = [" "," "," "," "," "," "," "," "," "]
    while(space[] != " ")
    printTable(space)
    fila = input("Ingrese fila: ")
    columna = input("Ingrese columna")
    
    
def playPlayer_2():
    pass

def printMenu():
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
            playComputer()
        else:
            if (opcion == 2):
                playPlayer_2()
            else:
                status = False
        
        
    

def main():
    
    printMenu()

main()