from tracker import add_expense, view_expenses, total_expenses

def menu():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spent")
        print("4. Exit")

        choice = input("Enter your choice (1–4): ")

        if choice == '1':
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            try:
                amount = float(amount)
                add_expense(category, amount)
            except ValueError:
                print("Please enter a valid number for amount.")
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print(f"Total spent: ${total_expenses():.2f}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
