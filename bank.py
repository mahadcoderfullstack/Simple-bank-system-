balance = 1000

while True:
    print("\n==== Simple Bank System ====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your current balance is:", balance)
        input("Press Enter to continue...")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print("Deposit successful!")
        else:
            print("Invalid amount!")
        input("Press Enter to continue...")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")
        input("Press Enter to continue...")

    elif choice == "4":
        print("Thank you! Program exiting...")
        break

    else:
        print("Invalid choice!")
        input("Press Enter to continue...")
