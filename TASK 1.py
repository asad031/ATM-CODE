balance = 100.

while True:
    print("Welcome to the banking app. Please choose an option:")
    print("1. Check balance")
    print("2. Deposit amount")
    print("3. Withdraw amount")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Your balance is ${:.2f}".format(balance))
    elif choice == "2":
        add_amount = float(input("Enter the amount to deposit ($): "))
        if add_amount <= 0:
            print("Invalid amount. ")
        else:
            balance += add_amount
            print("Deposit successful. Your new balance is ${:.2f}".format(balance))
    elif choice == "3":
        withdraw_amount = float(input("Enter the amount to withdraw ($): "))
        if withdraw_amount <= 0:
            print("Invalid amount. ")
        elif withdraw_amount > balance:
            print("Insufficient balance.")
        else:
            balance -= withdraw_amount
            print("Withdrawal successful. Your new balance is ${:.2f}".format(balance))
    elif choice == "4":
        print("Thank you for using the banking app.")