from graphics import*
from Button import*


def main():
    #you can do between 600-1000 pixels for pixels wide
    win = GraphWin("character creator", 800, 600)
    C = Circle(Point(300, 300), 250)
    C.draw(win)

    BigNose = Rectangle(Point(250, 325), Point(350, 400))
    smallNose = Rectangle(Point(275, 300 ), Point(325,375))

    BigMouth = Line(Point(200,500), Point(400,500))
    smallMouth = Line(Point(250, 450), Point(350, 450))

    BigEye1 = Circle(Point(200,250), 50)
    BigEye2 = Circle(Point(400, 250), 50)

    smallEye1 = Circle(Point(175, 250), 30)
    smallEye2 = Circle(Point(400, 250), 30)

    B = Button(win, Point(600, 100), Point(700, 175), "dark turquoise", "Big Eyes")
    B2 = Button(win, Point(600, 200), Point(700, 275), "dark turquoise", "Small Eyes")
    B3 = Button(win, Point(600, 300), Point(700, 375), "tomato", "Big Nose")
    B4 = Button(win, Point(600, 400), Point(700, 475), "tomato", "Small Nose")
    B5 = Button(win, Point(600, 500), Point(700, 575), "cyan", "Big Mouth")
    B6 = Button(win, Point(700, 400), Point(800, 475), "cyan", "Small Mouth")
    #this button is not showing up for some reason :(
    Q = Button(win, Point(600, 0), Point(700, 75), "misty rose", "QUIT")
    i = 1
    while True:
        m = win.getMouse()

        if B.isClicked(m):
            BigEye1.undraw()
            BigEye2.undraw()
            smallEye1.undraw()
            smallEye2.undraw()

            BigEye1.draw(win)
            BigEye2.draw(win)

        if B2.isClicked(m):
            smallEye1.undraw()
            smallEye2.undraw()
            BigEye1.undraw()
            BigEye2.undraw()

            smallEye1.draw(win)
            smallEye2.draw(win)

        if B3.isClicked(m):
            smallNose.undraw()
            BigNose.undraw()

            BigNose.draw(win)

        if B4.isClicked(m):
            smallNose.undraw()
            BigNose.undraw()

            smallNose.draw(win)

        if B5.isClicked(m):
            BigMouth.undraw()
            smallMouth.undraw()

            BigMouth.draw(win)

        if B6.isClicked(m):
            BigMouth.undraw()
            smallMouth.undraw()

            smallMouth.draw(win)

        if Q.isClicked(m):
                break
    
        i = i+5
#win.close(), closes the window
    win.close()

if __name__== "__main__":
    main() #indentation error?









        
