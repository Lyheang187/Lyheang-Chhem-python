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
root.title("This is my draw")
#  VARIABLES
grid = [
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,5,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,3],
    [3,2,3,2,0,2,3,2,3,3,3,3,3,3,3,2,3,2,0,2,3,2,3],
    [3,2,3,2,0,2,3,2,2,2,2,2,2,2,2,2,3,2,0,2,3,2,3],
    [3,2,3,2,2,2,3,2,0,0,2,3,2,0,0,2,3,2,2,2,3,2,3],
    [3,2,3,3,3,2,3,2,2,2,4,3,2,2,2,2,3,2,3,3,3,2,3],
    [3,0,2,2,2,0,0,0,3,3,3,3,3,3,3,0,0,0,2,2,2,0,3],
    [3,2,3,3,3,2,3,2,2,2,2,3,2,2,2,2,3,2,3,3,3,2,3],
    [3,2,3,2,2,2,3,2,0,0,2,3,2,0,0,2,3,2,2,2,3,2,3],
    [3,2,3,2,0,2,3,2,2,2,2,2,2,2,2,2,3,2,0,2,3,2,3],
    [3,4,3,2,0,2,3,2,3,3,3,3,3,3,3,2,3,2,0,2,3,2,3],
    [3,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,4,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
]

score = 0
notEnd = True
choiceToMove = []
theMonster = []
indexOf5 = []
# 2 = Food
# 3 = Wall
# 4 = monster
# 5 = Character

# squareSize = #choose the appropriate size of the squares
#  FUNCTION
def arrayToDrawing():
    global score
    myScore = "Score: "+ str(score)
    for Y in range (len(grid)):
        for X in range  (len(grid[0])):
            x1 = (X * 50)
            x2 = 50 + x1
            y1 = (Y * 50)
            y2 = 50 + y1
            if grid[Y][X] == 3:
                # color = ""
                # canvas.create_rectangle(x1,y1,x2,y2,fill = color, outline="")
                canvas.create_image(x1,y1, image=grass, anchor="NW")
            elif grid[Y][X] == 2:
                # color = ""
                # canvas.create_rectangle(x1,y1,x2,y2,fill = color, outline="")
                canvas.create_image(x1,y1, image=food, anchor="NW")
            elif grid[Y][X] == 5:
                # color = ""
                # canvas.create_rectangle(x1,y1,x2,y2,fill = color, outline="")
                canvas.create_image(x1,y1, image=player, anchor="NW")
            elif grid[Y][X] == 4: 
                enermy = canvas.create_image(x1,y1, image=monster, anchor="NW")
            elif grid[Y][X] == 0: 
                color = ""
                canvas.create_rectangle(x1,y1,x2,y2,fill = color, outline="")
            canvas.create_text(125, 25, text=myScore, font='consolas 24', fill='white')
    

# Movement
#-----------------------------------FindIndex--------------------------------------------#
def character(grid):
    global  indexOf5
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column]==5:
                indexOf5 = [row, column]
    return indexOf5


def indexOfMonster(grid):
    global theMonster
    for rIndex in range(len(grid)):
        for cIndex in  range(len(grid[rIndex])):
            if grid[rIndex][cIndex] == 4:
                theMonster.append([rIndex, cIndex])
    return theMonster




def whereToMove(grid, x, y):
    global choiceToMove
    choiceToMove = []
    if grid[x][y-1] != 3 and grid[x][y-1] != 4:
        choiceToMove.append('Left')
    if grid[x][y+1] != 3 and grid[x][y+1] != 4:
        choiceToMove.append('Right')
    if grid[x-1][y] != 3 and grid[x-1][y] != 4:
        choiceToMove.append('Up')
    if grid[x+1][y] != 3 and grid[x+1][y] != 4:
        choiceToMove.append('Down')
    return  choiceToMove

def moveMonster():
    global grid, choiceToMove, notEnd
    monsterIndex = indexOfMonster(grid)
    for monsters in monsterIndex:
        rowIndex = monsters[0]
        colIndex = monsters[1]
        place = whereToMove(grid, rowIndex, colIndex)
        if len(place) > 0:
            toMove = random.choice(place)
            if toMove == 'Up':
                if grid[rowIndex-1][colIndex] == 5:
                    notEnd = False
                elif grid[rowIndex-1][colIndex] != 5 and grid[rowIndex-1][colIndex] == 0:
                    grid[rowIndex-1][colIndex] = 4
                    grid[rowIndex][colIndex] = 0
                elif grid[rowIndex-1][colIndex] != 5 and grid[rowIndex-1][colIndex] == 2:
                    grid[rowIndex-1][colIndex] = 4
                    grid[rowIndex][colIndex] = 2
            if toMove == 'Right':
                if grid[rowIndex][colIndex+1] == 5:
                    notEnd = False
                elif grid[rowIndex][colIndex+1] != 5 and grid[rowIndex][colIndex+1] == 0:
                    grid[rowIndex][colIndex+1] = 4
                    grid[rowIndex][colIndex] = 0
                elif grid[rowIndex][colIndex+1] != 5 and grid[rowIndex][colIndex+1] == 2:
                    grid[rowIndex][colIndex+1] = 4
                    grid[rowIndex][colIndex] = 2
            if toMove == 'Down':
                if grid[rowIndex+1][colIndex] == 5:
                    notEnd = False
                elif grid[rowIndex+1][colIndex] != 5 and grid[rowIndex+1][colIndex] == 0 :
                    grid[rowIndex+1][colIndex] = 4
                    grid[rowIndex][colIndex] = 0
                elif grid[rowIndex+1][colIndex] != 5 and grid[rowIndex+1][colIndex] == 2 :
                    grid[rowIndex+1][colIndex] = 4
                    grid[rowIndex][colIndex] = 2
            if toMove == 'Left':
                if grid[rowIndex][colIndex-1] == 5:
                    notEnd = False
                elif grid[rowIndex][colIndex-1] != 5 and grid[rowIndex][colIndex-1] == 0 :
                    grid[rowIndex][colIndex-1] = 4
                    grid[rowIndex][colIndex] = 0
                elif grid[rowIndex][colIndex-1] != 3 and grid[rowIndex][colIndex-1] == 2  :
                    grid[rowIndex][colIndex-1] = 4
                    grid[rowIndex][colIndex] = 2

    canvas.delete('all')
    arrayToDrawing()
    canvas.after(450, moveMonster)





#-----------------------------------MoveDown--------------------------------------------#
def moveDown(event):
    global grid,score
    indexOf5 = character(grid)
    rowOfindex5 = indexOf5[0]
    columnOfindex5 = indexOf5[1]
    if grid[rowOfindex5+1][columnOfindex5] == 2:
        score += 10
    if grid[rowOfindex5+1][columnOfindex5] != 3:
        grid[rowOfindex5][columnOfindex5] = 0
        grid[rowOfindex5+1][columnOfindex5] = 5
    canvas.delete("all")
    arrayToDrawing()
#-----------------------------------MoveUp--------------------------------------------#
def moveUp(event):
    global grid,score
    indexOf5 = character(grid)
    rowOfindex5 = indexOf5[0]
    columnOfindex5 = indexOf5[1]
    if grid[rowOfindex5-1][columnOfindex5] == 2:
        score += 10
    if grid[rowOfindex5-1][columnOfindex5] != 3:
        grid[rowOfindex5][columnOfindex5] = 0
        grid[rowOfindex5-1][columnOfindex5] = 5
    canvas.delete("all")
    arrayToDrawing()
#-----------------------------------MoveLeft--------------------------------------------#
def moveLeft(event):
    global grid,score
    indexOf5 = character(grid)
    rowOfindex5 = indexOf5[0]
    columnOfindex5 = indexOf5[1]
    if grid[rowOfindex5][columnOfindex5-1] == 2:
        score += 10
    if grid[rowOfindex5][columnOfindex5-1] != 3:
        grid[rowOfindex5][columnOfindex5] = 0
        grid[rowOfindex5][columnOfindex5-1] = 5
    canvas.delete("all")
    arrayToDrawing()
#-----------------------------------MoveRight--------------------------------------------#
def moveRight(event):
    global grid, score
    indexOf5 = character(grid)
    rowOfindex5 = indexOf5[0]
    columnOfindex5 = indexOf5[1]
    if grid[rowOfindex5][columnOfindex5+1] == 2:
        score += 10
    if grid[rowOfindex5][columnOfindex5+1] != 3:
        grid[rowOfindex5][columnOfindex5] = 0
        grid[rowOfindex5][columnOfindex5+1] = 5
    canvas.delete("all")
    arrayToDrawing()

#-----------------------------*MOVE ENEMY*---------------------------------------



#----------------------------------Images-----------------------------------------------#
canvas.pack(expand=True, fill="both")
food = PhotoImage(file="food.png")
grass = PhotoImage(file="grass.png")
player = PhotoImage(file="Zombie.png")
monster = PhotoImage(file="monster.png")


#----------------------------------Btn-----------------------------------------------#
root.bind("<Left>", moveLeft) #LEFT CLICK
root.bind("<Right>", moveRight)  #RIGHT CLICK
root.bind("<Up>", moveUp) #Up CLICK
root.bind("<Down>", moveDown)  #Down CLICK
root.resizable(False,False)
arrayToDrawing()
moveMonster()

root.mainloop()




