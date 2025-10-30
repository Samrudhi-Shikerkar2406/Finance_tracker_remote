# transactions.py - transaction management module
# Author: Samrudhi Shikerkar
# Handles adding, viewing, and categorizing income and expense transactions.

import datetime


class TransactionManager:
    """
    TransactionManager Module
    --------------------------
    Provides class to manage income and expense transactions.
    Includes add, view, filter, and summary features.
    """

    def __init__(self):
        # Stores all transactions as a list of dictionaries
        self.transactions = []

    def add_transaction(self, amount, category, t_type, date=None, note=""):
        """Add a validated transaction"""
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number")
        if t_type not in ("income", "expense"):
            raise ValueError("Transaction type must be 'income' or 'expense'")
        if date is None:
            date = datetime.date.today().isoformat()

        transaction = {
            "amount": amount,
            "category": category.strip().title(),
            "type": t_type,
            "date": date,
            "note": note
        }
        self.transactions.append(transaction)

    def get_all_transactions(self):
        """Return list of all transactions"""
        return self.transactions

    def get_transactions_by_category(self, category):
        """Return transactions of a specific category"""
        return [t for t in self.transactions if t["category"] == category]

    def get_transactions_by_type(self, t_type):
        """Return all income or expense transactions"""
        return [t for t in self.transactions if t["type"] == t_type]

    def calculate_total(self, t_type):
        """Calculate total income or expense"""
        return sum(t["amount"] for t in self.transactions if t["type"] == t_type)

    def get_transactions_by_date_range(self, start_date, end_date):
        """Return transactions between two dates (YYYY-MM-DD)"""
        return [
            t for t in self.transactions
            if start_date <= t["date"] <= end_date
        ]


# ---------------------- #
# Temporary Test Section #
# ---------------------- #
if __name__ == "__main__":
    tm = TransactionManager()
    tm.add_transaction(1000, "salary", "income")
    tm.add_transaction(200, "food", "expense")
    tm.add_transaction(300, "travel", "expense")

    print("All Transactions:", tm.get_all_transactions())
    print("Expense Total:", tm.calculate_total("expense"))
    print("Food Only:", tm.get_transactions_by_category("Food"))

    # Example test for date range (using today's date)
    today = datetime.date.today().isoformat()
    print("Transactions Today:", tm.get_transactions_by_date_range(today, today))
