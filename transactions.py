# transactions.py - transaction management module"
# Author: Samrudhi Shikerkar
# Handles adding, viewing, and categorizing income and expense transactions.

class TransactionManager:
    def __init__(self):
        # stores all transactions as list of dicts
        self.transactions = []