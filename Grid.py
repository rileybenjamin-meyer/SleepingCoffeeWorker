# Grid and Main method
from Fish import *
from graphics import *
from Button import *

#Import random is similar to button and graphics, as it is importing seperate
#code so its more efficient and organized. But random is used to generate
#random numbers, randint, or to randomly choose a value in a list, random.choice[]
import random

#This imports the code from the Shark.py file, and then you can
#past things through, an ex. being a series of points 
from Shark import *
#import time
   
def reset(img):
    main()
#To reset everything, I used main() because this redraws the window
#with everything (grid+images+buttons) in it, except they fish and shark now have new positions
#We tried to figure out a way to close the prior window, but I ran out of time

def run(F1, F2, F3, S):

    F1,F2,F3 = F1[0], F2[1], F3[2]
    
    S.move(F1.pos, F2.pos, F3.pos)

#The following if statements, check to see if the shark is on the same cell
#as the fish, and then directs the fish to undraw, creating a facade of it
#being eaten

    if S.pos == F1.pos:
        F.undraw(win)

    if S.pos == F2.pos:
        F2.undraw(win)

    if S.pos == F3.pos:
        F3.undraw(win)

#The following for statements do the opposite of the above, they check to
#see if the fish haven't been eaten in order to direct them to continue
#"running away"
    for S in F1:
        if not F1.isEaten:
            F1.move(S.pos)

    for S in F2:
        if not F2.isEaten:
            F2.move(S.pos)

    for S in F3:
        if not F3.isEaten:
            F3.move(S.pos)

#We created a list to document the possible moves for the shark 
    LS = [(x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1),(x-1,y+0),(x+1,y+0),
    (x+0,y-1),(x+0,y+1),(x+2,y+0),(x-2,y+0),(x+0,y+2),(x+0,y-2)]

#Then we got the position of each fish and made them = to a variable
    F1pos = F1.getPos()
    F2pos = F2.getPos()
    F3pos = F3.getPos()
#Then we created a current minimun value to check each of our coordinates
#against, to track the minimum coordinates in the list, the minimum meaning that
#those coordinates are closest to a fish
    curMin = 500
#Were using i to track the index of each value to figure out what the index is
#of the coordinates in the list that were the minimum 
    i = 0

#The following for loop first starts by taking in the positions in the list,
#and as it loops, it will go in the order of the list.
#In the 2nd line, it gets the X coordinate of the first fish, and finds
#the difference between the fish X coordinate and the sharks X coordinate,
#to determine whether that fish is close to the shark, in terms of X.
#Then in the 3rd line, it does this same thing except with the Y coordinate
#The totalDiff, then adds up the difference in the X values
#and the difference in the Y values.(This is one 3 times because we have 3 fish)

    for pos in LS:

        diffX = abs(F1pos[0] - pos[0])
        diffY = abs(F1pos[1] - pos[1])
        totalDiff = diffX + diffY 

        diffX1 = abs(F2pos[0] - pos[0])
        diffY1 = abs(F2pos[1] - pos[1])
        totalDiff1 = diffX1 + diffY1

        diffX2 = abs(F3pos[0] - pos[0])
        diffY2 = abs(F3pos[1] - pos[1])
        totalDiff = diffX2 + diffY2

#As shown above, we created a current minumum and set it to 500, knowing that
#when checking for a new minimun, all the points will be smaller than 500,
#and then compare to the new current minimun, which would be on the right"scale"
#We then set the totalDiff to the curent minimum in order to find the "real" one
#As said above, setting i to the minPos, we can track what number in the list
#the actual minimum was. Then, to actually have i go thrrough the loop, without
#using a for i in range loop, we had i go up by one each time to go through
#each point in the list. This is repeated three times for the different total-
#diff's caluculated, for the 3 fish.
#The goal of doing all this, was the have the shark move toward the closest fish

        if totalDiff < curMin:

            curMin = totalDiff
            minPos = i
        i = i+1

        if totalDiff1 < curMin:

            curMin = totalDiff1
            minPos = i
        i = i+1

        if totalDiff2 < curMin:

            curMin = totalDiff2
            minPos = i
        i = i+1


def main():

#Here we created our window, called "Shark Simluator":
    win = GraphWin("Shark Simulator", 600, 600)

#Here we created each of our buttons using points outside of the grid,
#but still in the window
    Q = Button(win, Point(450, 450), Point(550, 500), "red", "QUIT")
    R = Button(win, Point(450, 350), Point(550, 400), "blue", "RESET")
    M = Button(win, Point(450, 250), Point(550, 300), "green", "MOVE")
    run = Button(win, Point(450, 150), Point(550, 200), "yellow", "RUN")

#To create the grid, we then use a for i in range (21) loop to repeatedly
#draw the vertical and horizontal lines until it has fufilled the range
#The range is 21 because you start counting the coordinates from (0,0), and to
#get to 20, it is 21 lines
    for i in range(21):

#The first line is for horizontal lines. By multiplying i by 20, it bring the
#points up to scale on the grid
#The second line is for vertical lines.Same thing.
        L = Line(Point(20*i, 0), Point(20*i, 400))
        L.draw(win)

        L1 = Line(Point(0, 20*i), Point(400, 20*i))
        L1.draw(win)

#After importing random, we used randint, to take the random "choice" between
#0-19. Then I set the x and y of the fish to that random number it chose. 

    x = random.randint(0,19)
    y = random.randint(0,19)

    x1 = random.randint(0,19)
    y1 = random.randint(0,19)

    x2 = random.randint(0,19)
    y2 = random.randint(0,19)


    F1 = Fish([x,y], win)
    F2 = Fish([x1,y1], win)
    F3 = Fish([x2,y2], win)

#We also did the same thing for the shark.
    
    x3 = random.randint(0,19)
    y3 = random.randint(0,19)

    S = Shark([x3,y3], win)

#In this part, we just wrote what should happen is each of the button's are
#clicked. The quit button should just get rid of the window and stop the code
#The reset just creates a new window with all the reset objects and images
#The move just calls upon each of the fish and the shark to move based on my
#defined movement, it uses the move method. (move takes x and y points
#to move  to a particular x, y point in the window.
#Same thing for run (essentially)

    while True:
        m = win.getMouse()

        if Q.isClicked(m):
            break

        if R.isClicked(m):
            reset(win)

        if M.isClicked(m):
            
            F1.move()
            F2.move()
            F3.move()
            S.move()

        if run.isClicked(m):
            F1.move()
            F2.move()
            F3.move()
            S.move()

#Also, commented out, I wanted to have the shark move toward the fish, and tried
#to do that by adding 2, so it would move 2 cells, or add 1 to the fish's pos

            '''if S.getPos() + 2 == F1.getPos():
                F1.getPos(x+1, y+1)'''
               
            

    win.close()

if __name__ == "__main__":
    main()
    
