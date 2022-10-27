
#1. 

def Factorial(x):
    
    #x = int(input("Write an integer"))
    #y = (x)
    y=1
    for i in range(x):
        
        y=y*(x-i)
            
        
    return y
        
def main():

    print(Factorial(7))
    
if __name__== "__main__":
    main()

    
#2.

def doubleIt(phrase):
    size=len(phrase)
    phrase = int(input("Write a string or integer"))
    x = phrase
    for i in range(x):
        newS=(x)
        if x==str:
            y=newS
            newS=(size - i)
            y=newS.index(1,x)
            print(x.replace(newS.index, newS.index*newS.index))

        else:
            x == int(phrase)
            z=newS2
            newS2=(x)
            newS2=x[0]
            newS2=x[0+i]
            z=newS2.index(1,x)
            print(x.replace(newS2.index, newS2.index*newS2.index))

def main(): 
    
    doubleIt("Write a string or integer")

if __name__== "__main__":
    main()


#3.


def camelCase(filename):
    filename=int(input("Write a name (of two words) that could be used for a file"))
    size=len(filename)
    for i in range(size):
        filename=filename.replace("/", "-")
        #The lower() method returns the lowercased string from the given string and replaces with an uppercase version
        #The str.title takes the first letter of each new word, and makes it uppercase
        filename=str.title(filename)
        filename=filename.replace(filename.index(1), lower(filename.index(1)))
        filename=filename.strip()
        print(filename)
    
    
    
def main():

    camelCase("Write a name (of two words) that could be used for a file")

if __name__ == "__main__":
    main()




