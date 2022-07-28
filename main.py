import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
frm = ttk.Frame(root,padding=10)
root.title("Tic Tac Toe")
frm.grid()

gameGrid = [["","",""],["","",""],["","",""]]
b1 = None
b2 = None
b3 = None
b4 = None
b5 = None
b6 = None
b7 = None
b8 = None
b9 = None
playerMove = False

def checkWinCondition():
    checkDiagonals()
    checkColumns()
    checkRows()
    checkDrawCondition()

def checkDiagonals():
    # Diagonal And anti diagonal
    if((gameGrid[0][0] == "O" and gameGrid[1][1] == "O" and gameGrid[2][2] == "O")):
        messagebox.showinfo("Game Over", "Player 1 Wins")
        return
    if((gameGrid[0][0] == "X" and gameGrid[1][1] == "X" and gameGrid[2][2] == "X")):
        messagebox.showinfo("Game Over", "Player 2 Wins")
        return
    if((gameGrid[0][2] == "O" and gameGrid[1][1] == "O" and gameGrid[2][0] == "O")):
        messagebox.showinfo("Game Over", "Player 1 Wins")
        return
    if((gameGrid[0][2] == "X" and gameGrid[1][1] == "X" and gameGrid[2][0] == "X")):
        messagebox.showinfo("Game Over", "Player 2 Wins")
        return

def checkColumns():

    #Columns
    if((gameGrid[0][0] == "O" and gameGrid[1][0] == "O" and gameGrid[2][0] == "O")):
        messagebox.showinfo("Game Over", "Player 1 Wins")
        return
    if((gameGrid[0][0] == "X" and gameGrid[1][0] == "X" and gameGrid[2][0] == "X")):
        messagebox.showinfo("Game Over", "Player 2 Wins")
        return
    if((gameGrid[0][1] == "X" and gameGrid[1][1] == "X" and gameGrid[2][1] == "X")):
        messagebox.showinfo("Game Over", "Player 2 Wins")
        return
    if((gameGrid[0][1] == "O" and gameGrid[1][1] == "O" and gameGrid[2][1] == "O")):
        messagebox.showinfo("Game Over", "Player 1 Wins")
        return
    if((gameGrid[0][2] == "O" and gameGrid[1][2] == "O" and gameGrid[2][2] == "O")):
        messagebox.showinfo("Game Over", "Player 1 Wins")
        return
    if((gameGrid[0][2] == "X" and gameGrid[1][2] == "X" and gameGrid[2][2] == "X")):
        messagebox.showinfo("Game Over", "Player 2 Wins")
        return

def checkRows():
    #Rows
    if((gameGrid[0][0] == "O" and gameGrid[0][1] == "O" and gameGrid[0][2] == "O")):
        messagebox.showinfo("Game Over", "Player 1 Wins")
        return
    if((gameGrid[0][0] == "X" and gameGrid[0][1] == "X" and gameGrid[0][2] == "X")):
        messagebox.showinfo("Game Over", "Player 2 Wins")
        return

    if((gameGrid[1][0] == "O" and gameGrid[1][1] == "O" and gameGrid[1][2] == "O")):
        messagebox.showinfo("Game Over", "Player 1 Wins")
        return
    if((gameGrid[1][0] == "X" and gameGrid[1][1] == "X" and gameGrid[1][2] == "X")):
        messagebox.showinfo("Game Over", "Player 2 Wins")
        return
    if((gameGrid[2][0] == "X" and gameGrid[2][1] == "X" and gameGrid[2][2] == "X")):
        messagebox.showinfo("Game Over", "Player 2 Wins")
        return
    if((gameGrid[2][0] == "O" and gameGrid[2][1] == "O" and gameGrid[2][2] == "O")):
        messagebox.showinfo("Game Over", "Player 1 Wins")
        return

def checkDrawCondition():
    emptyFound = False
    for row in range(len(gameGrid)):
        for col in range(len(gameGrid[row])):
            x = gameGrid[row][col]
            if x != "X" and x != "O":
                emptyFound = True
                break
    if not emptyFound:
        messagebox.showinfo("Draw", "The game was drawn!")

def clickButton(input):
    global playerMove
    mark = ""
    if(playerMove == False):
        mark = "O"
        playerMove = True
    else:
        mark = "X"
        playerMove = False

    if(input == 1):
        if(gameGrid[0][0] != "O" and gameGrid[0][0] != "X"):
            b1.config(text=mark)
            gameGrid[0][0] = mark
    elif(input == 2):
        if(gameGrid[0][1] != "O" and gameGrid[0][1] != "X"):
            b2.config(text=mark)
            gameGrid[0][1] = mark
    elif (input == 3):
        if(gameGrid[0][2] != "O" and gameGrid[0][2] != "X"):
            b3.config(text=mark)
            gameGrid[0][2] = mark
    elif (input == 4):
        if(gameGrid[1][0] != "O" and gameGrid[1][0] != "X"):
            b4.config(text=mark)
            gameGrid[1][0] = mark
    elif (input == 5):
        if(gameGrid[1][1] != "O" and gameGrid[1][1] != "X"):
            b5.config(text=mark)
            gameGrid[1][1] = mark
    elif (input == 6):
        if(gameGrid[1][2] != "O" and gameGrid[1][2] != "X"):
            b6.config(text=mark)
            gameGrid[1][2] = mark
    elif (input == 7):
        if(gameGrid[2][0] != "O" and gameGrid[2][0] != "X"):
            b7.config(text=mark)
            gameGrid[2][0] = mark
    elif (input == 8):
        if(gameGrid[2][1] != "O" and gameGrid[2][1] != "X"):
            b8.config(text=mark)
            gameGrid[2][1] = mark
    elif (input == 9):
        if(gameGrid[2][2] != "O" and gameGrid[2][2] != "X"):
            b9.config(text=mark)
            gameGrid[2][2] = mark

    checkWinCondition()

b1 = tk.Button(frm, text="",height = 6,width=10,command=lambda:clickButton(1))
b1.grid(column=0,row=0)
b2 = tk.Button(frm, text="",height = 6,width=10, command=lambda:clickButton(2))
b2.grid(column=1, row=0)
b3 = tk.Button(frm, text="",height = 6,width=10, command=lambda:clickButton(3))
b3.grid(column=2, row=0)
b4 = tk.Button(frm, text="",height = 6,width=10, command=lambda:clickButton(4))
b4.grid(column=0, row=1)
b5 = tk.Button(frm, text="",height = 6,width=10, command=lambda:clickButton(5))
b5.grid(column=1, row=1)
b6 = tk.Button(frm, text="",height = 6,width=10, command=lambda:clickButton(6))
b6.grid(column=2, row=1)
b7 = tk.Button(frm, text="",height = 6,width=10, command=lambda:clickButton(7))
b7.grid(column=0, row=2)
b8 = tk.Button(frm, text="",height = 6,width=10, command=lambda:clickButton(8))
b8.grid(column=1, row=2)
b9 = tk.Button(frm, text="",height = 6,width=10, command=lambda:clickButton(9))
b9.grid(column=2, row=2)

root.mainloop()