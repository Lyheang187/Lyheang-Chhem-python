#  IMPORTS
import tkinter as tk
from tkinter import *

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
# 1 = Enermy
# 2 = Food
# 3 = Wall
# 4 = monster
# 5 = Character

# squareSize = #choose the appropriate size of the squares
#  FUNCTION
def arrayToDrawing():
    for Y in range (len(grid)):
        for X in range  (len(grid[0])):
            x1 = (X * 50)
            x2 = 50 + x1
            y1 = (Y * 50)
            y2 = 50 + y1
            if grid[Y][X] == 3:
                color = ""
                canvas.create_rectangle(x1,y1,x2,y2,fill = color, outline="")
                canvas.create_image(x1,y1, image=grass, anchor=NW)
            elif grid[Y][X] == 2:
                color = ""
                canvas.create_rectangle(x1,y1,x2,y2,fill = color, outline="")
                canvas.create_image(x1,y1, image=food, anchor=NW)
            elif grid[Y][X] == 5:
                # color = ""
                # canvas.create_rectangle(x1,y1,x2,y2,fill = color, outline="")
                canvas.create_image(x1,y1, image=player, anchor=NW)
            elif grid[Y][X] == 4: 
                canvas.create_image(x1,y1, image=monster, anchor=NW)
            else:
                color = ""
                canvas.create_rectangle(x1,y1,x2,y2,fill = color, outline="")

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
    indexOf5 = character(grid)
    rowOfindex5 = indexOf5[0]
    columnOfindex5 = indexOf5[1]
    if grid[rowOfindex5+1][columnOfindex5] == 2:
        score += 10
        print(score)
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
        print(score)
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
        print(score)
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
        print(score)
    if grid[rowOfindex5][columnOfindex5+1] != 3:
        grid[rowOfindex5][columnOfindex5] = 0
        grid[rowOfindex5][columnOfindex5+1] = 5
        canvas.delete("all")
    arrayToDrawing()

#----------------------------------Images-----------------------------------------------#
canvas.pack(expand=True, fill="both")
food = PhotoImage(file="Food.png")
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

root.mainloop()




