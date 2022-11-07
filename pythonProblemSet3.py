#1.

def currencyConverter():
    current = input("please enter which kind of currency you have. Choose number from list:\n 1.United State Dollar\n2.European Euro\n3.Japanese Yen\n4.Australian Dollar")
    money = input("Please enter how much money you have : \n")
    newCurrency = input("Please enter which type of currency you want to convert to. Choose number from list:\n 1.United State Dollar\n2.European Euro\n3.Japanese Yen\n4.Australian Dollar")

    currencies = {1:[1, 1.01, 146.92, 1.56], 2:[0.99, 1, 145.81, 1.55], 3:[0.0068, 0.0069, 1, 0.011], 4:[0.64, 0.65, 94.37, 1]}
    #float is another word to converting a stirng into a number, and the number is not an integer anymore because it can have a decimal point now
    #the input function ,makes the inputed number into a string(int)^
    currencyNames = ["United States Dollar", "European Euro", "Japanese Yen", "Australian Dollar"]
    print("calculating ur currency....\n")
    output = float(money) * currencies[int(current)][int(newCurrency) - 1]
    # subtracting 1 because we only have 0,1,2,3 currencies, idle includes 0 as a number^
    print("You have", output)


def main():
    currencyConverter()
   
    
if __name__ == "__main__":
    main()


#2.

def groceryList(selectedFood):

    food = {"apple" : 1.50,
            "orange" : 1.00,
            "banana" : 1.00,
            "bagel" : 1.25,
            "cabbage" : 1.50,
            "spinach" : 4.25,
            "milk" : 2.75,
            "eggs" : 3.25,
            "cake" : 8.00,
            "pasta" : 3.50}

    
             
    print("You have purchased: ")
        
    for key in selectedFood:
        print(key)
        print(food.get(key))
        
    
    a=(food.get(selectedFood[0]))
    b=(food.get(selectedFood[1]))
    c=(food.get(selectedFood[2]))
    d=(food.get(selectedFood[3]))
    total=a+b+c+d 
    print("Your total is " + str(total))


def main():

   
    groceryList(["banana", "cabbage", "milk", "cake"])
    
if __name__ == "__main__":
    main()



