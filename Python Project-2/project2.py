expenses = []  

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    
    if choice == "1":
        name = input("Enter expense name: ")
        
        try:
            amount = float(input("Enter expense amount: "))
            expenses.append((name, amount))
            print("Expense added successfully!")
        except ValueError:
            print("Invalid amount! Please enter a number.")


    elif choice == "2":
        if not expenses:
            print("No expenses added yet.")
        else:
            total = 0
            print("\n--- All Expenses ---")
            for i, (name, amount) in enumerate(expenses, start=1):
                print(f"{i}. {name} - {amount}")
                total += amount
            
            print("---------------------")
            print(f"Total Spent: {total}")

    
    elif choice == "3":
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")