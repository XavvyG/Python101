from classes import Budget

print("\n---iSaveMore Budget App---\n")

def errorMsg():
    print("Invalid input!")

pincode = input("Please enter your 4-digit PIN code: ")
if pincode == "0000":

    selection1 = input("\nPlease select an option: \n1.) Set Budget \n2.) Use Current Budget\n")

    def overwriteBudget ():
        file1 = open("food.txt", "w")
        file1.write(str(food.balance))
        file1.close()
        file2 = open("entertainment.txt", "w")
        file2.write(str(entertainment.balance))
        file2.close()
        file3 = open("clothing.txt", "w")
        file3.write(str(clothing.balance))
        file3.close()

    def transferBalance (from_, to_):
        return from_.withdraw(to_.deposit(int(input("Transfer amount: "))))

    def viewBalance():
        print(f"\nFood {food}")
        print(f"Entertainment {entertainment}")
        print(f"Clothing {clothing}")


    if selection1 == "1":
        food = Budget(int(input("Set your food budget: ")))
        entertainment = Budget(int(input("Set your entertainment budget: ")))
        clothing = Budget(int(input("Set your clothing budget: ")))
        overwriteBudget()

    elif selection1 == "2":
        file1 = open("food.txt", "r")
        food_amount = file1.readline()
        food = Budget(int(food_amount))
        file2 = open("entertainment.txt", "r")
        entertainment_amount = file2.readline()
        entertainment = Budget(int(entertainment_amount))
        file3 = open("clothing.txt", "r")
        clothing_amount = file3.readline()
        clothing = Budget(int(clothing_amount))
    else:
        errorMsg()

    selection2 = input("\nPlease select an option: \n1.) Deposit \n2.) Withdraw \n3.) Transfer\n4.) View Balance\n")

    if selection2 == "1":
        print("---DEPOSIT FUNDS---")
        food.deposit(int(input("Food deposit: ")))
        entertainment.deposit(int(input("Entertainment deposit: ")))
        clothing.deposit(int(input("Clothing deposit: ")))
        overwriteBudget ()
        viewBalance()

    elif selection2 == "2":
        print("---WITHDRAW FUNDS---")
        food.withdraw(int(input("Food withdraw: ")))
        entertainment.withdraw(int(input("Entertainment withdraw: ")))
        clothing.withdraw(int(input("Clothing withdraw: ")))
        overwriteBudget()
        viewBalance()

    elif selection2 == "3":
        print("---TRANSFER FUNDS---")
        transfer = input("Please select an option: \n1.) Food -> Entertainment \n2.) Food -> Clothing \n3.) Entertainment -> Food \n4.) Entertainment -> Clothing\n5.) Clothing -> Food \n6.) Clothing -> Entertainment \n")
        if transfer == "1":
            transferBalance(food,entertainment)
        if transfer == "2":
            transferBalance(food,clothing)
        if transfer == "3":
            transferBalance(entertainment,food)
        if transfer == "4":
            transferBalance(entertainment,clothing)
        if transfer == "5":
            transferBalance(clothing,food)
        if transfer == "6":
            transferBalance(clothing,entertainment)
        else:
            errorMsg()
        overwriteBudget()
        viewBalance()

    elif selection2 == "4":
        print("---BALANCE---")
        viewBalance()

    else:
        errorMsg()
else:
    errorMsg()