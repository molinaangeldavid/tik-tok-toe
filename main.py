import os
from random import choice,randint

from sqlalchemy import false
# SYMBOLS = ['X','O']

def validarOpcion():
    option = input("Option: ")
    # if (menu == "menu"):
    while not(option.isnumeric() and (int(option) > 0 and int(option) < 4)):
        option = input("ERROR!! Input a valid option")
    # else:
        # if (menu == "game"):
        #     while not(option.isnumeric() and (int(option) > 0 and int(option) < 3)):
        #         option = input("ERROR!! Input a valid option")
    option = int(option)
    return option

def printTable(space):
    print(f'''
            {space[0][0]} |  {space[0][1]}  | {space[0][2]}
        ------------------
            {space[1][0]} |  {space[1][1]}  | {space[1][2]}
        ------------------
            {space[2][0]} |  {space[2][1]}  | {space[2][2]}
        ''')

def playComputer():
    random_choice = randint(0,2)
    fila = random_choice
    random_choice = randint(0,2)
    columna = random_choice
    return fila,columna

def validarGame(table,signo,player):
    for x in table:
        if (x == [signo,signo,signo]):
            print(f"Winner: {player}")
            return False
    new_table = []
    for x in range(3):
        for col in range(3):
            new_table[x][col] = table[col][x]
            if (x == col and table[x][col] =="X" or table[x][col] == 'O'):
                return False
            else:
                tablereverse = table[x][::-1]
                if (x == col and tablereverse[x][col]=="X" or tablereverse[x][col]=="O"):
                    return False
            
    for x in new_table:
        if (x == [signo,signo,signo]):
            print(f"Winner: {player}")
            return False
    

def playGame():
    space = [["","",""],
            ["","",""],
            ["","",""]]
    estado = True
    player = input("Write your name: ")
    while(estado):
        print(player)
        printTable(space)
        print("Fila")
        fila = validarOpcion()
        print("Columna")
        columna = validarOpcion()
        while not (space[fila-1][columna-1] == "" or space[fila-1][columna-1] == "O"):
            print("ERROR")
            fila = validarOpcion()
            print("Columna")
            columna = validarOpcion()
        space[fila-1][columna-1] = "X"
        print(space[fila-1][columna-1])
        # validarGame(space,"X",player)
        printTable(space)
        print(playComputer())
        fila = playComputer()[0]
        columna = playComputer()[1]
        while not (space[fila-1][columna-1] == "" or space[fila-1][columna-1] == "X"):
            fila = playComputer()[0]
            columna = playComputer()[1]
        space[fila-1][columna-1] = "O"
        print(space[fila-1][columna-1])
        # validarGame(table,'O')
        

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