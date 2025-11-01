# main.py
# Integrates all project modules
# Author: Samrudhi, Falak, Keziah, Anusha

from transactions import TransactionManager
from budgeting import BudgetManager
from history import HistoryManager
from visualization import VisualizationManager

def main():
    print("=== Personal Finance Tracker ===")

    # --- Transactions ---
    tm = TransactionManager()
    tm.add_transaction(1000, "Salary", "income")
    tm.add_transaction(200, "Food", "expense")
    tm.add_transaction(300, "Travel", "expense")
    print("\nAll Transactions:", tm.get_all_transactions())

    # --- Budgeting ---
    bm = BudgetManager()
    bm.set_budget("Food", 500)
    print("\nBudget Check:", bm.check_spending("Food", tm.get_all_transactions()))

    # --- History ---
    hm = HistoryManager(tm)
    print("\nHistory by Category (Food):", hm.filter_by_category("Food"))

    # --- Visualization ---
    vm = VisualizationManager(tm.get_all_transactions())
    vm.plot_expense_pie()
    vm.notify("Visualization complete.")

if __name__ == "__main__":
    main()
