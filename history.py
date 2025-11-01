# history.py
# Author: Keziah Blossom Pereira
# Provides methods for transaction history display and filtering.

class TransactionManager:
     """Mock TransactionManager for testing HistoryManager"""
    def __init__(self):
        self.transactions = [
            {'id': 1, 'date': '2025-10-10', 'category': 'Food', 'amount': 120},
            {'id': 2, 'date': '2025-10-12', 'category': 'Travel', 'amount': 300},
            {'id': 3, 'date': '2025-10-15', 'category': 'Food', 'amount': 50},
        ]

    def get_all_transactions(self):
        return self.transactions

    def get_transactions_by_category(self, category):
        return [t for t in self.transactions if t['category'] == category]

class HistoryManager:
    def __init__(self, transaction_manager):
        self.tm = transaction_manager