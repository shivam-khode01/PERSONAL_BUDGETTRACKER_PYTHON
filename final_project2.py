import csv
from datetime import datetime
categories = ["food", "entertainment", "utilities", "transportation", "housing", "healthcare", "savings"]  
class BudgetTracker:
    def __init__(self):
        self.income = 0
        self.expenses = {}  
        for category in categories:
            self.expenses[category] = 0  
    def add_income(self, amount):
        try:
            self.income += float(amount)
        except ValueError:
            print("Invalid input. Please enter a numeric value for income.")  
    def add_expense(self, category, amount): 
        if category in categories:
            try:
                self.expenses[category] += float(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value for expense.")  
        else:
            print("Invalid expense category. Choose from the predefined categories.")
    def get_budget(self):
        total_expenses = sum(self.expenses.values())  
        return self.income - total_expenses 
def main():
    budget = BudgetTracker()
    while True:
        print("\n1) Add Income")
        print("2) Add Expense")  
        print("3) View Budget")
        print("4) View Expenses")
        print("5) Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            amount = input("Enter income amount: ")
            budget.add_income(amount)
        elif choice == '2':
            category = input("Enter expense category: ")
            amount = input("Enter expense amount: ")
            budget.add_expense(category, amount)
        elif choice == '3':
            print(f"Remaining budget: {budget.get_budget()}")
        elif choice == '4':
            for cat, amt in budget.expenses.items():
                print(f"{cat}: {amt}")
        elif choice == '5':
            break
if __name__ == "__main__":
    main()

    