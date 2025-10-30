# transactions.py - transaction management module"
# Author: Samrudhi Shikerkar
# Handles adding, viewing, and categorizing income and expense transactions.

import datetime

class TransactionManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, category, t_type, date=None, note=""):
        """Add a transaction with amount, category, type, and optional note"""
        if date is None:
            date = datetime.date.today().isoformat()
        transaction = {
            "amount": amount,
            "category": category,
            "type": t_type,
            "date": date,
            "note": note
        }
        self.transactions.append(transaction)
