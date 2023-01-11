# Fish Class
from graphics import *
#from Button import *
import random
#from Shark import *

#We use a constructor to begin our class, and define everything in our class
class Fish:

    def __init__(self, pos, win):

#We then made our self x and y points = to the positions of x and y
        self.x = pos[0]
        self.y = pos[1]

#To draw my image in the grid, we multiplied x by 20, so it would be 
#to scale of the grid. We did this same thing for y, we also added 10 to both, to
#make sure each image was located in the exact center of a square.We then draw it.
        self.I = Image(Point(self.x*20+10, self.y*20+10),"fishImage.png")
        self.I.draw(win)        

#To define the movement for the fish, we passed it through self,and
#we wanted to have the fish move left by 1, so
#we added 1 to the x value, and set the change in x to that 1, and 0 for y
# Then, we used the move method, and multiplied the change in x and y by 20
#to bring it to scale of the grid
    def move(self):
        
        self.x = self.x + 1
        deltaX = 1
        deltaY = 0
        self.I.move(20*deltaX, 20*deltaY)



        '''self.I = Image(Point(self.pos2[0], self. pos2[1], "fishImage.png")
        self.fishBody2.draw(win)

        self.fishBody3 = Image(Point(self.pos3[0], self. pos3[1], "fishImage.png")
        self.fishBody3.draw(win)

        listOfPosition.append(self.fishBody1, self.fishBody2, self.fishBody3)'''


        

    
        

        
        

        


    
    

        
            


       
        
