from graphics import*
from Button import*

def darken(img):
    x = img.getWidth()
    y = img.getHeight()
    
    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            red= red-50
            blue=blue-50
            green=green-50

            if green<0:
                green=0
            if blue<0:
                blue=0
            if red<0:
                red=0

            c = color_rgb((red), (green), (blue))
            img.setPixel(i, j, c)
            


def lighten(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            red= red+50
            blue=blue+50
            green=green+50

            if green>200:
                green=255
            else:
                green=green+10
            if blue>200:
                blue=255
            else:
                blue=blue+10
            if red>200:
                red=255
            else:
                red=red+10

            c = color_rgb((red), (green), (blue))
            img.setPixel(i, j, c)

def grayscale(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            totalLight=pix[0]+pix[1]+pix[2]
            avg = int(totalLight/3)
            red=avg
            green=avg
            blue=avg
    #each red, green, and blue values are the same
            c = color_rgb((red), (green), (blue))
            img.setPixel(i, j, c)


def contrast(img):
    x = img.getWidth()
    y = img.getHeight()
    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            
            if red>150:
                red=red+50
            else:
                red=red-50
            if green>150:
                green=green+50
            else:
                green=green-50
            if blue>150:
                blue=blue+50
            else:
                blue=blue-50
                
            if red<0:
                red=0
            if red>255:
                red=255
            if green<0:
                green=0
            if green>255:
                green=255
            if blue>255:
                blue=255
            if blue<0:
                blue=0
            
                    

        
           
            c = color_rgb((red), (green), (blue))
            img.setPixel(i, j, c)


def bluescale(img):
    x = img.getWidth()
    y = img.getHeight()
    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            blue=blue+50
            red=red-50
            green=green-50

            if blue>220:
                blue=255
            if red<10:
                red=0
            if green<10:
                green=0
            c = color_rgb((red), (green), (blue))
            img.setPixel(i, j, c)

def reset(img):
    x = img.getWidth()
    y = img.getHeight()
    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            red=red
            green=green
            blue=blue
            c = color_rgb((red), (green), (blue))
            img.setPixel(i, j, c)
def main():
    
    win = GraphWin("Image Editor", 800, 600)
    win.setBackground("white")

    I = Image(Point(300, 300), "alexMorgan1.png")
    I.draw(win)
    
    B = Button(win, Point(600, 25), Point(700, 100), "darkorange1", "Darken")
    B2 = Button(win, Point(600, 100), Point(700, 175), "darkgoldenrod1", "Lighten")
    B3= Button(win, Point(600, 175), Point(700, 250), "darkslategray4", "Grayscale")
    B4 = Button(win, Point(600, 250), Point(700, 325), "cornflowerblue", "Bluescale")
    B5 = Button(win, Point(600, 325), Point(700, 400), "deeppink1", "Contrast")

    Q = Button(win, Point(600, 400), Point(700, 475), "brown1", "QUIT")

    while True:
        m = win.getMouse()
        
        if B.isClicked(m):
            darken(I)
            
        if B2.isClicked(m):
            lighten(I)

        if B3.isClicked(m):
            grayscale(I)

        if B4.isClicked(m):
            bluescale(I)

        if B5.isClicked(m):
            contrast(I)  

        if Q.isClicked(m):
            break

    win.close()

if __name__ == "__main__":
    main()
