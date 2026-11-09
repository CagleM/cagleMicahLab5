# Campus Cafe lab
def printWelcome(cafeName):
    """Prints a formatted welcome banner displaying the cafe name

    Parameters:
    cafeName: str, the argument passed through the main() funcction

    Returns:
    str, a welcome message from the cafe."""

    print(f"\n~~ Welcome to the {cafeName}! ~~")

def calculateTotal(price, isStudent):
    """Applies a discount depending on if the user is a student
    
    Parameters:
    price: float, current price of an item
    isStudent: boolean, dependent on student status

    Returns:
    float, (new) price rounded to 2 decimals."""

    if isStudent == True:
        price = price * 0.9
        return price
    else:
        return price

def getItemPrice(menu, itemName):
    """Looks up an item and returns the item price
    
    Parameters:
    menu: dict, mapping items to prices
    itemName: str, name of key
    
    Returns:
    float, price of item or zero depending on if the item exists"""

    if itemName in menu:
        return menu[itemName]
    else:
        return 0

def splitBill(priceTotal, numPeople):
    """Splits the bill evenly between a given number of people
    
    Parameters:
    pricesList: int, representing ordered item prices
    numPeople: int, group size
    
    Returns:
    The amount each person should pay"""

    totalSplit = priceTotal/numPeople # You may notice that I did not do the list way. I did it this way because of how the discount gives the subtotal and multipling a list by 0.9 is difficult to figure out right now.
    return totalSplit

def main():
    """Holds the cafe name, student boolean
    
    No parameters
    
    No returns"""

    # Welcome Banner for the cat cafe my wife want's to own
    printWelcome("Cagle Cat Cafe")

    #Prints menu for user
    print("\nWe have:\nCoffee   - $4.00\nTea      - $3.00\nCat Pass - $5.00\nPastrie  - $2.00")
    firstItem = input('\nWhat would you like? [First item of two] ')
    secondItem = input("And for your second item? ")
    print(f"Alright, so I have a {firstItem} and a {secondItem}.")

    #Get item price
    cafeMenu = {"Coffee":4, "Tea":3,"Cat Pass":5,"Pastrie":2}
    firstItemPrice = getItemPrice(cafeMenu, firstItem)
    secondItemPrice = getItemPrice(cafeMenu, secondItem)
    userCartTotal = [firstItemPrice, secondItemPrice]

    #Student discount
    student = input("Are you a student? [yes/no] ")
    if student.lower() == "yes":
        student = True
    else:
        student = False
    price = calculateTotal(sum(userCartTotal), student)

    #Splitting bill
    userSplitting = int(input("And how many people are paying today? Just you or your party? [Number] "))
    if userSplitting == 1:
        print(f"Alrighty, and your total is ${price:.2f}")
    elif userSplitting > 1:
        totalSplit = splitBill(price, userSplitting)
        print(f"Each person in your party will pay ${totalSplit:.2f} today.")
    else:
        print("Well someone has to pay... you're not getting this for free.")


main()
    