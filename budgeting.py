print("The budgeting.py handles budget setting and pending calculations for each category.")

class BudgetManager:
    def __init__(self):
        self.budgets = {}

    def set_budget(self, category, amount):
        """Assign a budget to a specific category."""
        self.budgets[category] = amount

    def get_budget(self, category):
        """Retrieve the allocated budget for a category."""
        return self.budgets.get(category, 0)

    def check_spending(self, category, transactions):
        """Track spent vs pending for a category."""
        spent = sum(t['amount'] for t in transactions if t['category'] == category and t['type'] == 'expense')
        return {
            'budget': self.get_budget(category),
            'spent': spent,
            'pending': self.get_budget(category) - spent
        }

    def update_budget(self, category, new_amount):
        """Update the budget amount for an existing category."""
        if category in self.budgets:
            self.budgets[category] = new_amount
            print(f"Budget for '{category}' updated to {new_amount}.")
        else:
            print(f"No existing budget for '{category}' to update.")

    def list_budgets(self):
        """Display all categories with their allocated budgets."""
        if not self.budgets:
            print("No budgets have been set yet.")
        else:
            for category, amount in self.budgets.items():
                print(f"{category}: ₹{amount}")


