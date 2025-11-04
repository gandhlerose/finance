
# Personal Budget Tracker

budget = []

def add_transaction():
    name = input("Enter transaction name: ")
    amount = float(input("Enter amount (use negative for expenses): "))
    budget.append({"name": name, "amount": amount})
    print(f"Transaction '{name}' added.")

def show_summary():
    total_income = sum(t["amount"] for t in budget if t["amount"] > 0)
    total_expenses = sum(t["amount"] for t in budget if t["amount"] < 0)
    balance = total_income + total_expenses
    print("\n--- Budget Summary ---")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${-total_expenses:.2f}")
    print(f"Balance: ${balance:.2f}")
    print("----------------------\n")

def show_transactions():
    if not budget:
        print("No transactions recorded yet.")
        return
    print("\n--- All Transactions ---")
    for t in budget:
        type_txn = "Income" if t["amount"] > 0 else "Expense"
        print(f"{t['name']}: ${t['amount']:.2f} ({type_txn})")
    print("------------------------\n")

def main():
    while True:
        print("1. Add transaction")
        print("2. Show summary")
        print("3. Show all transactions")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_transaction()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            show_transactions()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()