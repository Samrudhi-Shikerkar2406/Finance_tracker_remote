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

