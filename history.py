#History.py
#Author: Keziah Blossom Pereira
#Provides methods for transaction history display and filtering.

class HistoryManager:
    def __init__(self, transaction_manager):
        self.tm = transaction_manager