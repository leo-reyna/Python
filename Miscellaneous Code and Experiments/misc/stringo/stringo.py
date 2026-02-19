# RL. Jan 2023
# String Examples, If Statments
#
#

import os
os.system('cls')


width = os.get_terminal_size().columns  
print("---------------------------------".center(width))
print("Made in USA • Grown in Upstate NY".center(width))
print("---------------------------------".center(width))
print("WELCOME TO BELUGA COFFEE".center(width))
print("------------------------".center(width))
print("Stringo Industries 1999.".center(width))
# print("-" * 24, ``)

# Coffee Menu
menu = "Coffee, Decaf, Tea, Latte, Espresso, Iced Coffee"

customer = input("Enter your Name: ")

if customer == "Ben":
    print("You are not welcome here! Evil Ben!")
    exit()
else:
    message = f"Hello and welcome {customer}. Thank you for coming in today. What would like {menu}?"
    print(message) # message
    seleccion = input("Enter your selection: ")
    if seleccion == "Coffee": # coffee
        msgforcoffee = f"Perfect selection {customer}!"
        print(msgforcoffee)
    elif seleccion == "Tea":
        msgfortea = f"Tea is really good here {customer}"
        print(msgfortea)
    elif seleccion == "Decaf":
        msgfordecaf = f"Excellent choice! Decaf should help your heart {customer}"
        print(msgfordecaf)
    elif seleccion == "Latte":
        msgforlatte = f"So fancy!!, it will be a minute before you get the latte {customer}"
        print(msgforlatte)
    elif seleccion ==  "Espresso":
        msgforEspresso = f"Coming right up! {customer}"
        print(msgforEspresso)
    elif seleccion == "Iced Coffee":
        msforicedcoffee = f"Hot outside, better get something cold {customer}"
        print(msforicedcoffee)
# more to come