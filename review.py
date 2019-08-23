#Give the user the following options. Once the option that is selected is completed keep asking them until they hit 4 to quit:

#Hello, please choose one of following options:
#1) Check balance
#2) Add money to account
#3) Withdraw money from account
#4) Quit
#What will you like to do?

userInput = -1
balance = 0

while userInput != 4: # while 4 is not pressed loop will continue

    print(
        f"Hello, please choose one of following options:" "\n"
        f"1) Check balance""\n"
        f"2) Add money to account""\n"
        f"3) Withdraw money from account""\n"
        f"4) Quit""\n"
        f"What will you like to do?""\n"
    )

    balance = 500
    newBalance = balance

    if userInput == 1:
        print(f"Your current account has ${balance} dollars")
    elif userInput == 2:
        deposit = int(input("How much would you like to deposit? "))
        newBalance = (int(deposit) + int(balance))
        print(f"Your account now holds ${newBalance} dollars")
    elif userInput == 3:
        withdraw = int(input("How much money would you like to withdraw? "))
        newNum = int(newBalance) - withdraw
        if withdraw > int(newBalance):
            print("Insufficient Funds")
        else:
            print("Your account now holds " + str(newNum))

    userInput = int(input("enter number"))



