
user_funds = 10.31
price = {"Burger" : "1.99", "Fries" : "0.99" }
item_price = price["Burger"]

if item_price < user_funds:
    print("You have enough money!")
if item_price == user_funds:
    print("You have the precise amount of money")
if item_price > user_funds:
    print("Sorry you don't have enough money")



