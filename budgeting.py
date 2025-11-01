class BudgetManager:
    def __init__(self):
        self.budgets = {}

    def set_budget(self, category, amount):
        self.budgets[category] = amount

    def get_budget(self, category):
        return self.budgets.get(category, 0)

    def check_spending(self, category, transactions):
        spent = sum(
            t['amount'] for t in transactions
            if t['category'] == category and t['type'] == 'expense'
        )
        return {
            'budget': self.get_budget(category),
            'spent': spent,
            'pending': self.get_budget(category) - spent
        }

    def update_budget(self, category, new_amount):
        if category in self.budgets:
            self.budgets[category] = new_amount
            print(f"Budget for '{category}' updated to {new_amount}.")
        else:
            print(f"No existing budget for '{category}' to update.")

    def list_budgets(self):
        if not self.budgets:
            print("No budgets have been set yet.")
        else:
            for category, amount in self.budgets.items():
                print(f"{category}: ₹{amount}")


# ✅ Example usage
print("The budgeting.py handles budget setting and pending calculations for each category.")

if __name__ == "_main_":
    print("BudgetManager test run started...\n")
manager = BudgetManager()
manager.set_budget("Food", 5000)
manager.set_budget("Transport", 2000)

transactions = [
    {"category": "Food", "type": "expense", "amount": 1200},
    {"category": "Transport", "type": "expense", "amount": 800},
]

print(manager.check_spending("Food", transactions))
manager.list_budgets()
manager.update_budget("Food", 6000)
manager.list_budgets()
