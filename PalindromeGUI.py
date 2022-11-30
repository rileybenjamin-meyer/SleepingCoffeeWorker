
from graphics import*
from Button import*

def main():

    win=GraphWin("Palindrome", 800, 600)#dimension measurements are in pixels

    Q = Button(win, Point(600, 500), Point(700, 575), "cyan", "QUIT")
    Check = Button(win, Point(350, 350), Point(450, 425), "SteelBlue1", "Check")

    E = Entry(Point(400, 300), 50)
    E.draw(win)
    E.setSize(16)

    T = Text(Point(400, 250), "Write a potential palindrome below. Once you have written one, press Check ")
    T.draw(win)
    #T1 = text(Point(450, 500), "This is a Palindrome")
    #m = win.getMouse()
    #T.setText("No not a Palindrome")#this changes the text
    
    while True:

        m = win.getMouse()

        if Q.isClicked(m):
            break

        if Check.isClicked(m):
            pal = E.getText()
            length = len(pal)
            pal1 = True
          

            for i in range (length):
               
                if pal[i] != pal[length - 1 - i]:
                    pal1 = False
                    T.setText("This is not palindrome")
            if pal1 == True:
                T.setText("This is a palindrome")
            else: 
                pal1 = False
                T.setText("This is not palindrome")         
                      
        
    win.close()

if __name__ == "__main__":
    main()

