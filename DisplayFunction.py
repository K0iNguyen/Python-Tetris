import os

class Display:
    def __init__(self, PlayingField):
        self.PlayingField = PlayingField
    
    def display(self):
        for row in self.PlayingField:
            print(row)

    def update(self):
        os.system("cls")
        self.display()

