import time
import PlayingField
import Shapes
import random
import keyboard
import threading
import os

#Defining Functions
def randomize():
    return random.randint(0,6)

def down():
    currentShapes.spawn()
    flag = True
    while flag:
        playingArrayObject.update()
        time.sleep(1)
        flag = currentShapes.down()
        
def Main():
    while True:
        if keyboard.is_pressed("right"):
            time.sleep(0.15)
            currentShapes.right()
            playingArrayObject.update()
        if keyboard.is_pressed("left"):
            time.sleep(0.15)
            currentShapes.left()
            playingArrayObject.update()
        if keyboard.is_pressed("down"):
            time.sleep(0.15)
            currentShapes.down()
            playingArrayObject.update()
        if keyboard.is_pressed("up"):
            time.sleep(0.15)
            currentShapes.despawn()
            currentShapes.rotateUp()
            currentShapes.spawn()
            playingArrayObject.update()
        
        
            
def generateShapes(num):
    if num == 0:
        return Shapes.L1(field)
    elif num == 1:
        return Shapes.L2(field)
    elif num == 2:
        return Shapes.I(field)
    elif num == 3:
        return Shapes.O(field)
    elif num == 4:
        return Shapes.T(field)
    elif num == 5:
        return Shapes.Z1(field)
    else:
        return Shapes.Z2(field)
    
global filledRow
filledRow = ["1" for i in range(10)]
global emptyRow
emptyRow = [" " for i in range(10)]
    

#Defining Constants
playingArrayObject = PlayingField.PlayingField()
field = playingArrayObject.field
MainThread = threading.Thread(target = Main)

#main
MainThread.start()

while True:
    shapeNum = randomize()
    currentShapes = generateShapes(shapeNum)
    down()
    if playingArrayObject.checkEnd():
        break
    playingArrayObject.checkRow()
    
print("\033[A                             \033[A")
print("Game ended!")
print(f"Total Score: {playingArrayObject.score}")