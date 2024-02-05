import os
from sys import set_coroutine_origin_tracking_depth

class PlayingField:
    def __init__(self):
        self.field = [[" " for i in range(10)] for i in range(25)] #2D array fields
        self.field[4] = ["-" for i in range(10)]
        self.score = 0   
    
    global filledRow
    filledRow = ["1" for i in range(10)]

    def display(self):
        for row in self.field:
            print(row)
        print(f"Score: {self.score}")

    def update(self):
        os.system("cls")
        self.limitUpdate()
        self.display()
        
    def checkRow(self):
        for i in range(25):
            if self.field[i] == filledRow:
                self.score += 1
                self.field.pop(i)
                self.field.insert(0, [" " for i in range(10)])
  
    def limitUpdate(self):
        for i in range(10):
            if self.field[4][i] == ' ':
                self.field[4][i] = "-"
                
    def checkEnd(self):
        if self.field[4] != ["-" for i in range(10)]:
            return True

