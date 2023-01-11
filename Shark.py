# Shark Class

from graphics import *
import random

#We use a constructor to being our class, and define everything in our class
class Shark:

    def __init__(self, pos, win):

        #LS = [(x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1),(x-1,y+0),(x+1,y+0),
        #(x+0,y-1),(x+0,y+1),(x+2,y+0),(x-2,y+0),(x+0,y+2),(x+0,y-2)]

#We then made our self x and y points = to the positions of x and y
        self.x = pos[0]
        self.y = pos[1]

#To draw my image in the grid, we multiplied x by 20, so it would be 
#to scale of the grid. We did this same thing for y, we also added 10 to both, to
#make sure each image was located in the exact center of a square.We then draw it.
        self.I = Image(Point(self.x*20+10, self.y*20+10),"sharkImage.png")
        self.I.draw(win)

#To define the movement for the shark, we passed it through self, and
#set the change in x = 1, because we were trying to move it to the left, because we
#wanted to it this way, we set the change of y = 0
#In the if statement, we said that if the x point is >=20, it should subtract 1 from
#it, so it goes one to the right, so it can be seen in the grid. The same thing was 
#done for y. Our else statement then says that if non of these pat things are true,
#move 1 cell over
#Then we just have the shark move by using the same code as fish at the bottom
    def move(self):
        
        deltaX = 1
        deltaY = 0

        if  self.x>=20:
            self.x = self.x - 1

        elif self.y>=20:
            self.y = self.y - 1

        else:
            self.x = self.x+1
            self.y = self.y+1

        self.I.move(20*deltaX, 20*deltaY)

         

        

        
