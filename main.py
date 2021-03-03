#  IMPORTS
import tkinter as tk
from tkinter import *
import random

#  CONSTANTS
SCREEN_WIDTH = 1150
SCREEN_HEIGHT = 650
root = tk.Tk()
canvas = tk.Canvas(root)
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
root.title("Lyheang's game")
#  VARIABLES
grid = [
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,5,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,3],
    [3,2,3,2,0,2,3,2,3,3,3,3,3,3,3,2,3,2,0,2,3,2,3],
    [3,2,3,2,0,2,3,2,2,2,2,2,2,2,2,2,3,2,0,2,3,2,3],
    [3,2,3,2,2,2,3,2,0,0,2,3,2,0,0,2,3,2,2,2,3,2,3],
    [3,2,3,3,3,2,3,2,2,2,2,3,2,2,2,2,3,2,3,3,3,2,3],
    [3,0,2,2,2,0,0,0,3,3,3,3,3,3,3,0,0,0,2,2,2,0,3],
    [3,2,3,3,3,2,3,2,2,2,2,3,2,2,2,2,3,2,3,3,3,2,3],
    [3,2,3,2,2,2,3,2,0,0,2,3,2,0,0,2,3,2,2,2,3,2,3],
    [3,2,3,2,0,2,3,2,2,2,2,2,2,2,2,2,3,2,0,2,3,2,3],
    [3,2,3,2,0,2,3,2,3,3,3,3,3,3,3,2,3,2,0,2,3,2,3],
    [3,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,4,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
]

score = 0
notFinished = True
notWin = True
choiceToMove = []
indexOfEnemy = []
finalResult = 'LOST!!!'
isLost = False
pre = 4              # to store data when enemy move
# 2 = Food
# 3 = Wall
# 4 = monster
# 5 = Character

# squareSize = #choose the appropriate size of the squares
#  FUNCTION
def arrayToDrawing():
    global score, finalResult
    
    myScore = "Score: "+ str(score)
    for Y in range (len(grid)):
        for X in range  (len(grid[0])):
            x1 = (X * 50)
            x2 = 50 + x1
            y1 = (Y * 50)
            y2 = 50 + y1
            if grid[Y][X] == 3:
                canvas.create_image(x1,y1, image=grass, anchor=NW)
            elif grid[Y][X] == 2:
                canvas.create_image(x1,y1, image=food, anchor=NW)
            elif grid[Y][X] == 5:
                canvas.create_image(x1,y1, image=player, anchor=NW)
            elif grid[Y][X] == 4: 
                enermy = canvas.create_image(x1,y1, image=monster, anchor=NW)

            canvas.create_text(125, 25, text=myScore, font='consolas 24', fill='white')
    if score == 1260:
        finalResult = 'WON!'
        result()
    

# Movement
#-----------------------------------FindIndex--------------------------------------------#
def character(grid):
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column]==5:
                indexOf5 = [row, column]
    return indexOf5
#-----------------------------------MoveDown--------------------------------------------#
def moveDown(event):
    global grid,score
    if score != 1260 and not isLost:
        indexOf5 = character(grid)
        rowOfindex5 = indexOf5[0]
        columnOfindex5 = indexOf5[1]
        if grid[rowOfindex5+1][columnOfindex5] == 2:
            score += 10
        if grid[rowOfindex5+1][columnOfindex5] == 4:
            result()
            return None
        if grid[rowOfindex5+1][columnOfindex5] != 3:
            grid[rowOfindex5][columnOfindex5] = 0
            grid[rowOfindex5+1][columnOfindex5] = 5
        canvas.delete("all")
        arrayToDrawing()
#-----------------------------------MoveUp--------------------------------------------#
def moveUp(event):
    global grid,score
    if score != 1260 and not isLost:
        indexOf5 = character(grid)
        rowOfindex5 = indexOf5[0]
        columnOfindex5 = indexOf5[1]
        if grid[rowOfindex5-1][columnOfindex5] == 2:
            score += 10
        if grid[rowOfindex5-1][columnOfindex5] == 4:
            result()
            return None
        if grid[rowOfindex5-1][columnOfindex5] != 3:
            grid[rowOfindex5][columnOfindex5] = 0
            grid[rowOfindex5-1][columnOfindex5] = 5
        canvas.delete("all")
        arrayToDrawing()
#-----------------------------------MoveLeft--------------------------------------------#
def moveLeft(event):
    global grid,score
    if score != 1260 and not isLost:
        indexOf5 = character(grid)
        rowOfindex5 = indexOf5[0]
        columnOfindex5 = indexOf5[1]
        if grid[rowOfindex5][columnOfindex5-1] == 2:
            score += 10
        if grid[rowOfindex5][columnOfindex5-1] == 4:
            result()
            return None
        if grid[rowOfindex5][columnOfindex5-1] != 3:
            grid[rowOfindex5][columnOfindex5] = 0
            grid[rowOfindex5][columnOfindex5-1] = 5
        canvas.delete("all")
        arrayToDrawing()
#-----------------------------------MoveRight--------------------------------------------#
def moveRight(event):
    global grid, score
    if score != 1260 and not isLost:
        indexOf5 = character(grid)
        rowOfindex5 = indexOf5[0]
        columnOfindex5 = indexOf5[1]
        if grid[rowOfindex5][columnOfindex5+1] == 2:
            score += 10
        if grid[rowOfindex5][columnOfindex5+1] == 4:
            result()
            return None
        if grid[rowOfindex5][columnOfindex5+1] != 3:
            grid[rowOfindex5][columnOfindex5] = 0
            grid[rowOfindex5][columnOfindex5+1] = 5
        canvas.delete("all")
        arrayToDrawing()

#-----------------------------*GET INDEX OF ENEMY*-------------------------------#
def getEnIndex(grid):
    indexOf4 = []
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column]==4:
                indexOf4 = [row, column]
    return indexOf4

#-----------------------------*WHERE CAN ENEMY MOVE*-----------------------------#
def moveChoice():
    result = []
    index = getEnIndex(grid)
    row = index[0]
    col = index[1]
    if grid[row-1][col] != 3:
        result.append('t')
    if grid[row][col+1] != 3:
        result.append('r')
    if grid[row+1][col] != 3:
        result.append('b')
    if grid[row][col-1] != 3:
        result.append('l')
    return result

#-----------------------------*MOVE ENEMY*---------------------------------------#
def moveEn():
    global grid, pre
    index = getEnIndex(grid)
    if len(index) > 0 and not isLost:
        row = index[0]
        col = index[1]
        go = random.choice(moveChoice())
        if go == 't':
            if pre != 2:
                grid[row][col] = 0
            else:
                grid[row][col] = 2
            pre = grid[row-1][col]
            if pre == 5:
                result()
                return None
            grid[row-1][col] = 4
        elif go == 'r':
            if pre != 2:
                grid[row][col] = 0
            else:
                grid[row][col] = 2
            pre = grid[row][col+1]
            if pre == 5:
                result()
                return None
            grid[row][col+1] = 4
        elif go == 'b':
            if pre != 2:
                grid[row][col] = 0
            else:
                grid[row][col] = 2
            pre = grid[row+1][col]
            if pre == 5:
                result()
                return None
            grid[row+1][col] = 4
        elif go == 'l':
            if pre != 2:
                grid[row][col] = 0
            else:
                grid[row][col] = 2
            pre = grid[row][col-1]
            if pre == 5:
                result()
                return None
            grid[row][col-1] = 4
        canvas.delete("all")
        arrayToDrawing()

    canvas.after(300, moveEn)

#----------------------------------Images-----------------------------------------------#
def result():
    global isLost
    isLost = True
    canvas.delete("all")
    canvas.create_text(575, 325, text=finalResult, font='consolas 40', fill='black')


#----------------------------------Images-----------------------------------------------#
canvas.pack(expand=True, fill="both")
food = PhotoImage(file="Food.png")
grass = PhotoImage(file="wall.png")
player = PhotoImage(file="Zombie.png")
monster = PhotoImage(file="monster.png")


#----------------------------------Btn-----------------------------------------------#
root.bind("<Left>", moveLeft)       #LEFT CLICK
root.bind("<Right>", moveRight)     #RIGHT CLICK
root.bind("<Up>", moveUp)           #Up CLICK
root.bind("<Down>", moveDown)       #Down CLICK
root.resizable(False,False)
arrayToDrawing()
moveEn()

root.mainloop()




