#python
# visualization.py
# Author: Anusha
# Visualizes financial data and provides notification alerts.

import matplotlib.pyplot as plt

class VisualizationManager:
    def __init__(self, transactions):
        self.transactions = transactions

    def plot_expense_pie(self):
        """Show pie chart of expense distribution across categories."""
        category_totals = {}

        for t in self.transactions:
            if t['type'] == 'expense':
                category_totals[t['category']] = category_totals.get(t['category'], 0) + t['amount']
        labels = list(category_totals.keys())
        sizes = list(category_totals.values())
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title('Expense by Category')
        plt.show()

    def notify(self, message):
        """Print alert notifications (console-based)."""
        print(f"ALERT: {message}")
