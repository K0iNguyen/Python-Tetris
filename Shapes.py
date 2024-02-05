#X and Y depict current center coordination of the block

#Comments on functions and procedures is only in class L1, every other class is all referencing class L1. Functions and Procedures work on the same principles with adjustment based on which Shape the class is representing.
class L1:
    def __init__(self,PlayingSpace):
        self.X = 4 #spawn center X
        self.Y = 3 #spawn center Y
        self.PlayingSpace = PlayingSpace
        #self.Orientations = [1,2,3,4]
        self.currentOrientation = 1
    
    #spawn is adjusted for every different orientation | PS. Hoping to find a better way to do this.
    def spawn(self): 
        #1st Orientation
        disValue = "1"
        if self.currentOrientation == 1:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y][self.X + 1] = disValue
            self.PlayingSpace[self.Y][self.X - 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X + 1] = disValue

        #2nd Orientation
        elif self.currentOrientation == 2:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y][self.X + 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 2][self.X] = disValue
        
        #3rd Orientation
        elif self.currentOrientation == 3:
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X + 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X - 1] = disValue
            self.PlayingSpace[self.Y][self.X - 1] = disValue
        
        #4rd Orientation
        elif self.currentOrientation == 4:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y - 2][self.X - 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 2][self.X] = disValue

    #despawn procedure is as same as spawn procedure with empty values.
    def despawn(self): 
        disValue = " "
        if self.currentOrientation == 1:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y][self.X + 1] = disValue
            self.PlayingSpace[self.Y][self.X - 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X + 1] = disValue

        #2nd Orientation
        elif self.currentOrientation == 2:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y][self.X + 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 2][self.X] = disValue
        
        #3rd Orientation
        elif self.currentOrientation == 3:
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X + 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X - 1] = disValue
            self.PlayingSpace[self.Y][self.X - 1] = disValue
        
        #4rd Orientation
        elif self.currentOrientation == 4:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y - 2][self.X - 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 2][self.X] = disValue
        
    def rotateUp(self):
        if self.currentOrientation == 4:
            if self.X == 9: #changing X coordinate to accomodate for change of orientaion at the edge | This is done for every different shape limit.
                self.X -= 1
            self.currentOrientation = 1
        else:
            if self.currentOrientation == 2:
                if self.X == 0: #change X coordinate for different edge
                    self.X += 1
            self.currentOrientation += 1
    
    def downAction(self):
                self.despawn()
                self.Y += 1
                self.spawn()
                return True
        
    def down(self):
        if self.Y != 24:
            disValue = "1"
            if self.currentOrientation == 1 and self.PlayingSpace[self.Y + 1][self.X] != disValue and self.PlayingSpace[self.Y + 1][self.X + 1] != disValue and self.PlayingSpace[self.Y + 1][self.X - 1] != disValue:
                    return self.downAction()
            elif self.currentOrientation == 2 and self.PlayingSpace[self.Y + 1][self.X] != disValue and self.PlayingSpace[self.Y + 1][self.X + 1] != disValue:
                return self.downAction()
            elif self.currentOrientation == 3 and self.PlayingSpace[self.Y][self.X] != disValue and self.PlayingSpace[self.Y + 1][self.X - 1] != disValue and self.PlayingSpace[self.Y][self.X + 1] != disValue:
                return self.downAction()
            elif self.currentOrientation == 4 and self.PlayingSpace[self.Y + 1][self.X] != disValue and self.PlayingSpace[self.Y - 1][self.X - 1] != disValue:
                return self.downAction()
            else:
                return False
        else:
            return False

#X and Y axis limit for each orientation
#Z1, Z2, and I only have 2 orientation as orientation 1 and 2
#If were to recreate the orientation, recommend to have a graph of all possible orientation of every shape.
# same x right (8): 1, 2, 3
# same x right (9): 4, 5
# x right(7): 6

# same x left (0): 2, 5
# same x left (1): 1, 3, 4, 6

# y(24): 1, 2, 4, 5, 6
# y(23): 3

    def leftAction(self):
            self.despawn()
            self.X -= 1
            self.spawn()
     
    def left(self):
        disValue = "1"
        if self.currentOrientation == 1:
            if self.X != 1:
                if self.PlayingSpace[self.Y][self.X - 2] != disValue and self.PlayingSpace[self.Y - 1][self.X] != disValue:
                    self.leftAction()
        elif self.currentOrientation == 2:
           if self.X != 0:
               if self.PlayingSpace[self.Y][self.X - 1] != disValue and self.PlayingSpace[self.Y - 1][self.X - 1] != disValue and self.PlayingSpace[self.Y - 2][self.X - 1] != disValue:
                    self.leftAction()
        elif self.currentOrientation == 3:
           if self.X != 1:
               if self.PlayingSpace[self.Y][self.X - 2] != disValue and self.PlayingSpace[self.Y - 1][self.X - 2] != disValue:
                    self.leftAction()
        elif self.currentOrientation == 4:
           if self.X != 1:
               if self.PlayingSpace[self.Y][self.X - 1] != disValue and self.PlayingSpace[self.Y - 1][self.X - 1] != disValue and self.PlayingSpace[self.Y - 2][self.X - 2] != disValue:
                    self.leftAction()
        
    #Moving Shape to the Right
    def rightAction(self):
            self.despawn()
            self.X += 1
            self.spawn()

    def right(self):
        disValue = "1"
        if self.currentOrientation == 1:
           if self.X != 8:
               if self.PlayingSpace[self.Y][self.X + 2] != disValue and self.PlayingSpace[self.Y - 1][self.X + 2] != disValue:
                    self.rightAction()
        elif self.currentOrientation == 2:
           if self.X != 8:
               if self.PlayingSpace[self.Y][self.X + 2] != disValue and self.PlayingSpace[self.Y - 1][self.X + 1] != disValue and self.PlayingSpace[self.Y - 2][self.X + 1] != disValue:
                    self.rightAction()
        elif self.currentOrientation == 3:
           if self.X != 8:
               if self.PlayingSpace[self.Y][self.X] != disValue and self.PlayingSpace[self.Y - 1][self.X + 2] != disValue:
                    self.rightAction()
        elif self.currentOrientation == 4:
           if self.X != 9:
               if self.PlayingSpace[self.Y][self.X + 1] != disValue and self.PlayingSpace[self.Y - 1][self.X + 1] != disValue and self.PlayingSpace[self.Y - 2][self.X + 1] != disValue:
                    self.rightAction()
            
class L2(L1):
    def spawn(self):
        disValue = "1"
        #1st Orientation
        if self.currentOrientation == 1:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y][self.X + 1] = disValue
            self.PlayingSpace[self.Y][self.X - 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X - 1] = disValue
        
        #2nd Orientation
        elif self.currentOrientation == 2:    
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y- 1][self.X] = disValue
            self.PlayingSpace[self.Y - 2][self.X] = disValue
            self.PlayingSpace[self.Y - 2][self.X + 1] = disValue

        #3rd Orientation
        elif self.currentOrientation == 3:
            self.PlayingSpace[self.Y][self.X + 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X + 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X - 1] = disValue
        
        #4th Orientation
        elif self.currentOrientation == 4:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y][self.X - 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 2][self.X] = disValue

    def despawn(self):
        disValue = " "
        #1st Orientation
        if self.currentOrientation == 1:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y][self.X + 1] = disValue
            self.PlayingSpace[self.Y][self.X - 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X - 1] = disValue
        
        #2nd Orientation
        elif self.currentOrientation == 2:    
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y- 1][self.X] = disValue
            self.PlayingSpace[self.Y - 2][self.X] = disValue
            self.PlayingSpace[self.Y - 2][self.X + 1] = disValue

        #3rd Orientation
        elif self.currentOrientation == 3:
            self.PlayingSpace[self.Y][self.X + 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X + 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X - 1] = disValue
        
        #4th Orientation
        elif self.currentOrientation == 4:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y][self.X - 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 2][self.X] = disValue
    
    def down(self):
        if self.Y != 24:
            disValue = "1"
            if self.currentOrientation == 1 and self.PlayingSpace[self.Y + 1][self.X] != disValue and self.PlayingSpace[self.Y + 1][self.X + 1] != disValue and self.PlayingSpace[self.Y + 1][self.X - 1] != disValue:
                return self.downAction()
            elif self.currentOrientation == 2 and self.PlayingSpace[self.Y + 1][self.X] != disValue and self.PlayingSpace[self.Y - 1][self.X + 1] != disValue:
                return self.downAction()
            elif self.currentOrientation == 3 and self.PlayingSpace[self.Y][self.X] != disValue and self.PlayingSpace[self.Y + 1][self.X + 1] != disValue and self.PlayingSpace[self.Y][self.X - 1] != disValue:
                return self.downAction()
            elif self.currentOrientation == 4 and self.PlayingSpace[self.Y + 1][self.X] != disValue and self.PlayingSpace[self.Y + 1][self.X - 1] != disValue:
                return self.downAction()
            else:
                return False
        else:
            return False    

    def left(self):
        disValue = "1"
        if self.currentOrientation == 1:
           if self.X != 1:
               if self.PlayingSpace[self.Y][self.X - 2] != disValue and self.PlayingSpace[self.Y - 1][self.X - 2] != disValue:
                    self.leftAction()
        elif self.currentOrientation == 2:
           if self.X != 0:
               if self.PlayingSpace[self.Y][self.X - 1] != disValue and self.PlayingSpace[self.Y - 1][self.X - 1] != disValue and self.PlayingSpace[self.Y - 2][self.X - 1] != disValue:
                    self.leftAction()
        elif self.currentOrientation == 3:
           if self.X != 1:
               if self.PlayingSpace[self.Y - 1][self.X - 2] != disValue and self.PlayingSpace[self.Y][self.X] != disValue:
                    self.leftAction()
        elif self.currentOrientation == 4:
           if self.X != 1:
               if self.PlayingSpace[self.Y][self.X - 2] != disValue and self.PlayingSpace[self.Y - 1][self.X - 1] != disValue and self.PlayingSpace[self.Y - 2][self.X - 1] != disValue:
                    self.leftAction()
    
    def right(self):
        disValue = "1"
        if self.currentOrientation == 1:
           if self.X != 8:
               if self.PlayingSpace[self.Y][self.X + 2] != disValue and self.PlayingSpace[self.Y - 1][self.X] != disValue:
                    self.rightAction()
        elif self.currentOrientation == 2:
           if self.X != 8:
               if self.PlayingSpace[self.Y][self.X + 1] != disValue and self.PlayingSpace[self.Y - 1][self.X + 1] != disValue and self.PlayingSpace[self.Y - 2][self.X + 2] != disValue:
                    self.rightAction()
        elif self.currentOrientation == 3:
           if self.X != 8:
               if self.PlayingSpace[self.Y][self.X + 2] != disValue and self.PlayingSpace[self.Y - 1][self.X + 2] != disValue:
                    self.rightAction()
        elif self.currentOrientation == 4:
           if self.X != 9:
               if self.PlayingSpace[self.Y][self.X + 1] != disValue and self.PlayingSpace[self.Y - 1][self.X + 1] != disValue and self.PlayingSpace[self.Y - 2][self.X + 1] != disValue:
                    self.rightAction()

class Z1(L1):
    def spawn(self):
        disValue = "1"
        #1st Orientation
        if self.currentOrientation == 1:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y][self.X + 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X - 1] = disValue
        
        #2nd Orientation
        elif self.currentOrientation == 2: 
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X + 1] = disValue
            self.PlayingSpace[self.Y - 2][self.X + 1] = disValue

    def despawn(self):
        disValue = " "
        #1st Orientation
        if self.currentOrientation == 1:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y][self.X + 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X - 1] = disValue
        
        #2nd Orientation
        elif self.currentOrientation == 2: 
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X + 1] = disValue
            self.PlayingSpace[self.Y - 2][self.X + 1] = disValue
    
    def rotateUp(self):
        if self.currentOrientation == 2:
            if self.X == 0:
                self.X += 1
            self.currentOrientation = 1
        else:
            self.currentOrientation += 1
            
    def left(self):
        disValue = "1"
        if self.currentOrientation == 1:
           if self.X != 1:
               if self.PlayingSpace[self.Y][self.X - 1] != disValue and self.PlayingSpace[self.Y - 1][self.X - 2] != disValue:
                    self.leftAction()
        elif self.currentOrientation == 2:
           if self.X != 0:
               if self.PlayingSpace[self.Y][self.X - 1] != disValue and self.PlayingSpace[self.Y - 1][self.X - 1] != disValue and self.PlayingSpace[self.Y - 2][self.X] != disValue:
                    self.leftAction()

    def right(self):
        disValue = "1"
        if self.currentOrientation == 1:
           if self.X != 8:
               if self.PlayingSpace[self.Y][self.X + 2] != disValue and self.PlayingSpace[self.Y - 1][self.X + 1] != disValue:
                    self.rightAction()
        elif self.currentOrientation == 2:
           if self.X != 8:
               if self.PlayingSpace[self.Y][self.X + 1] != disValue and self.PlayingSpace[self.Y - 1][self.X + 2]!= disValue and self.PlayingSpace[self.Y - 2][self.X + 2] != disValue:
                    self.rightAction()
     
    def down(self):
        if self.Y != 24:
            disValue = "1"
            if self.currentOrientation == 1 and self.PlayingSpace[self.Y + 1][self.X] != disValue and self.PlayingSpace[self.Y + 1][self.X + 1] != disValue and self.PlayingSpace[self.Y][self.X - 1] != disValue:
                return self.downAction()
            elif self.currentOrientation == 2 and self.PlayingSpace[self.Y + 1][self.X] != disValue and self.PlayingSpace[self.Y][self.X + 1] != disValue:
                return self.downAction()
            else:
                return False
        else:
            return False
     
class Z2(Z1):
    def spawn(self):
        disValue = "1"
        #1st Orientation
        if self.currentOrientation == 1:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y][self.X - 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X + 1] = disValue
        
        #2nd Orientation
        elif self.currentOrientation == 2: 
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X - 1] = disValue
            self.PlayingSpace[self.Y - 2][self.X - 1] = disValue

    def despawn(self):
        disValue = " "
        #1st Orientation
        if self.currentOrientation == 1:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y][self.X - 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X + 1] = disValue
        
        #2nd Orientation
        elif self.currentOrientation == 2: 
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X - 1] = disValue
            self.PlayingSpace[self.Y - 2][self.X - 1] = disValue
      
    def rotateUp(self):
        if self.currentOrientation == 2:
            if self.X == 9:
                self.X -= 1
            self.currentOrientation = 1
        else:
            self.currentOrientation += 1
     
    def left(self):
        disValue = "1"
        if self.currentOrientation == 1:
           if self.X != 1:
               if self.PlayingSpace[self.Y][self.X - 2] != disValue and self.PlayingSpace[self.Y - 1][self.X - 1] != disValue:
                    self.leftAction()
        elif self.currentOrientation == 2:
           if self.X != 1:
               if self.PlayingSpace[self.Y][self.X - 1] != disValue and self.PlayingSpace[self.Y - 1][self.X - 2] != disValue and self.PlayingSpace[self.Y - 2][self.X - 2] != disValue:
                    self.leftAction()

    def right(self):
        disValue = "1"
        if self.currentOrientation == 1:
           if self.X != 8:
               if self.PlayingSpace[self.Y][self.X + 1] != disValue and self.PlayingSpace[self.Y - 1][self.X + 2] != disValue:
                    self.rightAction()
        elif self.currentOrientation == 2:
           if self.X != 9:
               if self.PlayingSpace[self.Y][self.X + 1] != disValue and self.PlayingSpace[self.Y - 1][self.X + 1]!= disValue and self.PlayingSpace[self.Y - 2][self.X] != disValue:
                    self.rightAction()
     
    def down(self):
        if self.Y != 24:
            disValue = "1"
            if self.currentOrientation == 1 and self.PlayingSpace[self.Y + 1][self.X] != disValue and self.PlayingSpace[self.Y + 1][self.X - 1] != disValue and self.PlayingSpace[self.Y][self.X + 1] != disValue:
                return self.downAction()
            elif self.currentOrientation == 2 and self.PlayingSpace[self.Y][self.X - 1] != disValue and self.PlayingSpace[self.Y + 1][self.X] != disValue:
                return self.downAction()
            else:
                return False
        else:
            return False

class T(L1):
    def spawn(self):
        disValue = "1"
        #1st Orientation
        if self.currentOrientation == 1:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y][self.X + 1] = disValue
            self.PlayingSpace[self.Y][self.X - 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
        
        #2nd Orientation
        elif self.currentOrientation == 2:    
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y- 1][self.X] = disValue
            self.PlayingSpace[self.Y - 2][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X + 1] = disValue

        #3rd Orientation
        elif self.currentOrientation == 3:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X - 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X + 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
        
        #4th Orientation
        elif self.currentOrientation == 4:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X - 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 2][self.X] = disValue

    def despawn(self):
        disValue = " "
        #1st Orientation
        if self.currentOrientation == 1:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y][self.X + 1] = disValue
            self.PlayingSpace[self.Y][self.X - 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
        
        #2nd Orientation
        elif self.currentOrientation == 2:    
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y- 1][self.X] = disValue
            self.PlayingSpace[self.Y - 2][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X + 1] = disValue

        #3rd Orientation
        elif self.currentOrientation == 3:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X - 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X + 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
        
        #4th Orientation
        elif self.currentOrientation == 4:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X - 1] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 2][self.X] = disValue
            
    def down(self):
        if self.Y != 24:
            disValue = "1"
            if self.currentOrientation == 1 and self.PlayingSpace[self.Y + 1][self.X] != disValue and self.PlayingSpace[self.Y + 1][self.X + 1] != disValue and self.PlayingSpace[self.Y + 1][self.X - 1] != disValue:
                return self.downAction()
            elif self.currentOrientation == 2 and self.PlayingSpace[self.Y + 1][self.X] != disValue and self.PlayingSpace[self.Y][self.X + 1] != disValue:
                return self.downAction()
            elif self.currentOrientation == 3 and self.PlayingSpace[self.Y + 1][self.X] != disValue and self.PlayingSpace[self.Y][self.X + 1] != disValue and self.PlayingSpace[self.Y][self.X - 1] != disValue:
                return self.downAction()
            elif self.currentOrientation == 4 and self.PlayingSpace[self.Y + 1][self.X] != disValue and self.PlayingSpace[self.Y][self.X - 1] != disValue:
                return self.downAction()
            else:
                return False
        else:
            return False

    def left(self):
        disValue = "1"
        if self.currentOrientation == 1:
           if self.X != 1:
               if self.PlayingSpace[self.Y][self.X - 2] != disValue and self.PlayingSpace[self.Y - 1][self.X - 1] != disValue:
                    self.leftAction()
        elif self.currentOrientation == 2:
           if self.X != 0:
               if self.PlayingSpace[self.Y][self.X - 1] != disValue and self.PlayingSpace[self.Y - 1][self.X - 1] != disValue and self.PlayingSpace[self.Y - 2][self.X - 1] != disValue:
                    self.leftAction()
        elif self.currentOrientation == 3:
           if self.X != 1:
               if self.PlayingSpace[self.Y][self.X - 1] != disValue and self.PlayingSpace[self.Y - 1][self.X - 2] != disValue:
                    self.leftAction()
        elif self.currentOrientation == 4:
           if self.X != 1:
               if self.PlayingSpace[self.Y][self.X - 1] != disValue and self.PlayingSpace[self.Y - 1][self.X - 2] != disValue and self.PlayingSpace[self.Y - 2][self.X - 1] != disValue:
                    self.leftAction()
            
    def right(self):
        disValue = "1"
        if self.currentOrientation == 1:
           if self.X != 8:
               if self.PlayingSpace[self.Y][self.X + 2] != disValue and self.PlayingSpace[self.Y - 1][self.X + 1] != disValue:
                    self.rightAction()
        elif self.currentOrientation == 2:
           if self.X != 8:
               if self.PlayingSpace[self.Y][self.X + 1] != disValue and self.PlayingSpace[self.Y - 1][self.X + 2] != disValue and self.PlayingSpace[self.Y - 2][self.X + 1] != disValue:
                    self.rightAction()
        elif self.currentOrientation == 3:
           if self.X != 8:
               if self.PlayingSpace[self.Y][self.X + 1] != disValue and self.PlayingSpace[self.Y - 1][self.X + 2] != disValue:
                    self.rightAction()
        elif self.currentOrientation == 4:
           if self.X != 9:
               if self.PlayingSpace[self.Y][self.X + 1] != disValue and self.PlayingSpace[self.Y - 1][self.X + 1] != disValue and self.PlayingSpace[self.Y - 2][self.X + 1] != disValue:
                    self.rightAction()

class I(Z1):
    def spawn(self):
        disValue = "1"
        #1st Orientation
        if self.currentOrientation == 1:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 2][self.X] = disValue
            self.PlayingSpace[self.Y - 3][self.X] = disValue
        
        #2nd Orientation
        elif self.currentOrientation == 2:    
            self.PlayingSpace[self.Y][self.X - 1] = disValue
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y][self.X + 1] = disValue
            self.PlayingSpace[self.Y][self.X + 2] = disValue

    def despawn(self):
        disValue = " "
        #1st Orientation
        if self.currentOrientation == 1:
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y - 1][self.X] = disValue
            self.PlayingSpace[self.Y - 2][self.X] = disValue
            self.PlayingSpace[self.Y - 3][self.X] = disValue
        
        #2nd Orientation
        elif self.currentOrientation == 2:    
            self.PlayingSpace[self.Y][self.X - 1] = disValue
            self.PlayingSpace[self.Y][self.X] = disValue
            self.PlayingSpace[self.Y][self.X + 1] = disValue
            self.PlayingSpace[self.Y][self.X + 2] = disValue
           
    def rotateUp(self):
        if self.currentOrientation == 2:
            self.currentOrientation = 1
        else:
            if self.X == 9:
                self.X -= 2
            if self.X == 0:
                self.X += 1
            self.currentOrientation += 1
      
    def left(self):
        disValue = "1"
        if self.currentOrientation == 2:
           if self.X != 1:
               if self.PlayingSpace[self.Y][self.X - 2] != disValue:
                    self.leftAction()
        elif self.currentOrientation == 1:
           if self.X != 0:
               if self.PlayingSpace[self.Y][self.X - 1] != disValue and self.PlayingSpace[self.Y - 1][self.X - 1] != disValue and self.PlayingSpace[self.Y - 2][self.X - 1] != disValue and self.PlayingSpace[self.Y - 3][self.X - 1] != disValue:
                    self.leftAction()

    def right(self):
        disValue = "1"
        if self.currentOrientation == 2:
           if self.X != 7:
               if self.PlayingSpace[self.Y][self.X + 3] != disValue:
                    self.rightAction()
        elif self.currentOrientation == 1:
           if self.X != 9:
               if self.PlayingSpace[self.Y][self.X + 1] != disValue and self.PlayingSpace[self.Y - 1][self.X + 1]!= disValue and self.PlayingSpace[self.Y - 2][self.X + 1] != disValue and self.PlayingSpace[self.Y - 3][self.X + 1] != disValue:
                    self.rightAction()

    def down(self):
        if self.Y != 24:
            disValue = "1"
            if self.currentOrientation == 2 and self.PlayingSpace[self.Y + 1][self.X] != disValue and self.PlayingSpace[self.Y + 1][self.X - 1] != disValue and self.PlayingSpace[self.Y + 1][self.X + 1] != disValue and self.PlayingSpace[self.Y + 1][self.X + 2] != disValue:
                return self.downAction()
            elif self.currentOrientation == 1 and self.PlayingSpace[self.Y + 1][self.X] != disValue:
                return self.downAction()
            else:
                return False
        else:
            return False
        
class O(L1):
    def spawn(self):
        self.PlayingSpace[self.Y][self.X] = "1"
        self.PlayingSpace[self.Y][self.X + 1] = "1"
        self.PlayingSpace[self.Y - 1][self.X + 1] = "1"
        self.PlayingSpace[self.Y - 1][self.X] = "1"

    def despawn(self):
        self.PlayingSpace[self.Y][self.X] = " "
        self.PlayingSpace[self.Y][self.X + 1] = " "
        self.PlayingSpace[self.Y - 1][self.X + 1] = " "
        self.PlayingSpace[self.Y - 1][self.X] = " "
        
    def left(self):
        disValue = "1"
        if self.X != 0:
            if self.PlayingSpace[self.Y][self.X - 1] != disValue and self.PlayingSpace[self.Y - 1][self.X - 1] != disValue:
                self.leftAction()

    def right(self):
        disValue = "1"
        if self.X != 8:
            if self.PlayingSpace[self.Y][self.X + 2] != disValue and self.PlayingSpace[self.Y - 1][self.X + 2]:
                self.rightAction()
            
    def down(self):
        if self.Y != 24:
            if self.PlayingSpace[self.Y + 1][self.X] != "1" and self.PlayingSpace[self.Y + 1][self.X + 1] != "1":
                return self.downAction()
            else:
                return False
        else:
            return False



