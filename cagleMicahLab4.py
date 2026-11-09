# Campus Cafe lab
def printWelcome(cafeName):
    """Prints a formatted welcome banner displaying the cafe name

    Parameters:
    cafeName: str, the argument passed through the main() funcction

    Returns:
    str, a welcome message from the cafe."""

    print(f"\n~~ Welcome to the {cafeName}! ~~")
    
    
def applyDiscount(originalOrder, discountCode):
    """ Apply a 10% discount for students and a 5% discount for faculty. Otherwise, keep the original price. 
    
    Parameters:
    originalOrder: dict, patron's order with names and prices
    discountCode: str, either "student" or "faculty" to determine the discount applied
    
    Returns:
    dict, discounted prices rounded to 2 decimal places."""
    
    discountedOrder = {}
    for item, price in originalOrder.items():
        if discountCode == "student":
            discountedPrice = round(price * 0.9, 2)
        elif discountCode == "faculty":
            discountedPrice = round(price * 0.95, 2)
        else:
            discountedPrice = price
        discountedOrder[item] = discountedPrice
    return discountedOrder

    
def initializeMenu(numItems=0):
    """ Executes a loop that prompts the user to enter an item and the cost of that item (meant to build the menu)
    
    Parameter:
    numItems: int, how many items to be added to the menu
    
    Returns:
    dict, a dictionary of items and their prices or if 0, then a default menu is returned"""
    
    if numItems == 0:
        return {"Coffee":4.00, "Tea":3.00,"Cat Pass":5.00,"Pastrie":2.00}
    else:
        menu = {}
        for i in range(numItems):
            itemName = input(f"What is the name of item? ")
            itemPrice = float(input(f"And what is the price of {itemName}? "))
            menu[itemName] = itemPrice
        return menu

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
    
    # print(initializeMenu(3))

    # Welcome Banner for the cat cafe my wife want's to own
    printWelcome("Cagle Cat Cafe")

    #Prints menu for user
    print("\nWe have:\nCoffee   - $4.00\nTea      - $3.00\nCat Pass - $5.00\nPastrie  - $2.00")
    firstItem = input('\nWhat would you like? [First item of two] ')
    secondItem = input("And for your second item? ")
    print(f"Alright, so I have a {firstItem} and a {secondItem}.")

    #Get item price
    cafeMenu = {"coffee":4, "tea":3,"cat pass":5,"pastrie":2}
    firstItemPrice = getItemPrice(cafeMenu, firstItem.lower())
    secondItemPrice = getItemPrice(cafeMenu, secondItem.lower())
    userCartTotal = [firstItemPrice, secondItemPrice]

    #Student or faculty discount
    student = input("Are you a student? [yes/no] ")
    if student.lower() == "yes":
        discountCode = "student"
    else:
        faculty = input("Are you faculty? [yes/no] ")
        if faculty.lower() == "yes":
            discountCode = "faculty"
        else:
            discountCode = "n/a"

    # dict for the applyDiscount function and test execution
    originalOrder = {firstItem:firstItemPrice, secondItem:secondItemPrice} 
    #print(applyDiscount(originalOrder, discountCode))
    discountedOrder = applyDiscount(originalOrder, discountCode)
    #finding the discount for each item prepping for the reciept function
    discounts = {k: discountedOrder[k] - originalOrder[k] for k in discountedOrder if k in originalOrder} #I did use AI to figue this one out. How to quickly get a difference of dict values
    total = sum(discountedOrder.values())

    #Splitting bill
    userSplitting = int(input("And how many people are paying today? Just you or your party? [Number] "))
    if userSplitting == 1:
        print(f"Alrighty, and your total is ${total:.2f}")
    elif userSplitting > 1:
        totalSplit = splitBill(total, userSplitting)
        print(f"Each person in your party will pay ${totalSplit:.2f} today.")
    else:
        print("Well someone has to pay... you're not getting this for free.")

    


main()
    