FILE = "expenses.txt"

def welcome():
    print("PERSONAL EXPENSE TRACKER")
    print("--------------------------")
    print("1 View Expenses")
    print("2 Add Expenses")
    print("3 Remove Expenses")
    print("4 Total Expenses")
    print("5 Exit")
    print("--------------------------")

def load_expenses():
    expenses = []
    try:
        with open(FILE, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                category, amount = line.rsplit(",", 1)
                expenses.append({"category": category, "amount": float(amount)})
    except FileNotFoundError:
        pass  # first run, no file yet
    except Exception as e:
        print(e)
    return expenses

def save_expenses(expenses):
    with open(FILE, "w") as f:
        for e in expenses:
            f.write(f"{e['category']},{e['amount']}\n")

def view_expenses(expenses):
    if not expenses:
        print("\nThere are no expenses to view")
        return
    print("\nExpenses:")
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['category']} : {e['amount']}")
    print()

def add_expenses(expenses):
    try:
        category = input("Please enter the category: ")
        amount = float(input("Please enter the amount: "))
        expenses.append({"category": category, "amount": amount})
        save_expenses(expenses)
    except ValueError:
        print("Invalid amount input")
    except Exception as e:
        print(e)

def total_expenses(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"Your total expenses is: {total}")

def remove_expenses(expenses):
    if not expenses:
        print("\nThere are no expenses to remove")
        return
    view_expenses(expenses)
    try:
        number = int(input("Please enter the number: "))
        if 1 <= number <= len(expenses):
            removed = expenses.pop(number - 1)
            save_expenses(expenses)
            print(f"Removed: {removed['category']} - {removed['amount']} successfully")
        else:
            print("Number out of range")
    except ValueError:
        print("Invalid number")
    except Exception as e:
        print(e)

def main():
    welcome()
    expenses = load_expenses()
    while True:
        choice = input("\nChoose: ")
        if choice == "1":
            view_expenses(expenses)
        elif choice == "2":
            add_expenses(expenses)
        elif choice == "3":
            remove_expenses(expenses)
        elif choice == "4":
            total_expenses(expenses)
        elif choice == "5":
            print("Thank you for using this program")
            return
        else:
            print("Invalid choice")

main()