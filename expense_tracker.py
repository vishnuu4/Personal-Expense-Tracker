expenses = []

print("PERSONAL EXPENSE TRACKER")

choice = 0

while choice != 5:
    print("1. Add Expense")
    print("2. View Total Expenses")
    print("3. Highest Expense")
    print("4. Lowest Expense")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))

        expense = {
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        print(f"Expense added: ₹{amount} - {category}")

    elif choice == 2:
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"Total expenses: ₹{total}")

    elif choice == 3:
        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            highest = expenses[0]["amount"]

            for expense in expenses:
                if expense["amount"] > highest:
                    highest = expense["amount"]

            print(f"Highest expense: ₹{highest}")

    elif choice == 4:
        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            lowest = expenses[0]["amount"]

            for expense in expenses:
                if expense["amount"] < lowest:
                    lowest = expense["amount"]

            print(f"Lowest expense: ₹{lowest}")

    elif choice == 5:
        print("Thanks for using Expense Tracker!")

    else:
        print("Invalid choice. Please try again.")
