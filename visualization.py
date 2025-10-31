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
