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
        return {"Coffee":4.00, "Tea":3.00,"CatPass":5.00,"Pastrie":2.00}
    else:
        menu = {}
        for i in range(numItems):
            itemName = input(f"What is the name of item? ")
            itemPrice = float(input(f"And what is the price of {itemName}? "))
            menu[itemName] = itemPrice
        return menu
    
def addItemsToCart(cafeMenu):
    """ Executes a loop that prompts the user to enter an item from the given menu and adds it to a list
    
    Parameters:
    cafeMenu: dict, the menu of items and prices
    
    Returns:
    cart, a list of items the user has ordered"""
    
    shoppingDoneCheck = ""
    cart = {}
    while shoppingDoneCheck.lower() != "done":
        cartItem = input("What can I get for you today? [CaSe SeNsItIvE, type 'done' when finished] ")
        if cartItem.lower() == "done":
            shoppingDoneCheck = "done"
        elif cartItem not in cafeMenu:
            print(f"Sorry, we don not have {cartItem} on the menu today. Scroll up to have another look at the menu.")
        else:
            cart[cartItem] = cafeMenu[cartItem]
    
    return cart

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

def printReceipt(originalOrder, discounts, discountCode, split):
    """ For each item in the order, this prints the name, the original price, the savings per item, then the final total
    
    Parameters:
    originalOrder: dict, original items with prices
    discounts: dict, discounted items with prices
    discountCode: str, determines if the user has the discount or not
    split: int, nuber of people splitting the bill
    
    Returns:
    Multiple prints that make the output look like a reciept"""
    
    for item in originalOrder:
        if discountCode == "n/a":
            print(f"{item}\t\t ${originalOrder[item]:.2f}")
        else:
            print(f"{item}\t\t ${originalOrder[item]:.2f}")
            print(f"  Savings  \t-${discounts[item]:.2f}")
            
    print("-----------------------")
    print(f"Subtotal\t ${sum(originalOrder.values()):.2f}")
    print(f"Savings\t\t-${sum(discounts.values()):.2f}")
    total = sum(originalOrder.values()) - sum(discounts.values())
    print(f"Total\t\t ${total:.2f}")
    if split > 1:
        costPer = splitBill(total, split)
        print(f"Split\t\t ${costPer:.2f}")
    else:
        pass
     

def main():
    """Holds the cafe name, student boolean
    
    No parameters
    
    No returns"""
    
    #Initialize menu
    #initializeMenu(3)
    #initializeMenu()
    cafeMenu = initializeMenu(int(input("How many menu items do you want to set today? [0 for default menu] ")))

    # Welcome Banner for the cat cafe my wife want's to own
    printWelcome("Cagle Cat Cafe")

    #Prints menu for user
    for item in cafeMenu:
        print(f"{item}\t\t ${cafeMenu[item]:.2f}")
        
    #User shooping cart
    cart = addItemsToCart(cafeMenu)
    
    print("\nAlrighty, so I have: a ", end=" ")
    for value in cart:
        print(f"{value}", end=", ")

    #Get item price(s)
    

    #Student or faculty discount
    student = input("\nAre you a student? [Yes/No] ")
    if student.lower() == "yes":
        discountCode = "student"
    else:
        faculty = input("Are you faculty? [Yes/No] ")
        if faculty.lower() == "yes":
            discountCode = "faculty"
        else:
            discountCode = "n/a"


    # test applyDiscount function
    # print(applyDiscount(cart, "student"), "student")
    # print(applyDiscount(cart, "faculty"), "faculty")
    #print(applyDiscount(cart, discountCode))
    discountedOrder = applyDiscount(cart, discountCode)
    
    #finding the discount for each item prepping for the reciept function
    discounts = {k: -(discountedOrder[k] - cart[k]) for k in discountedOrder if k in cart} #I did use AI to figue this one out. How to quickly get a difference of dict values and put it back into a dict
    total = sum(discountedOrder.values())

    #Splitting bill
    userSplitting = int(input("And how many people are paying today? Just you or your party? [Number] "))

    #Print reciept
    printReceipt(cart, discounts, discountCode, userSplitting)

main()
    