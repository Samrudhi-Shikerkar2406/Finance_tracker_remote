#History.py
#Author: Keziah Blossom Pereira
#Provides methods for transaction history display and filtering.

class HistoryManager:
    def __init__(self, transaction_manager):
        self.tm = transaction_manager

    def show_all(self):
        #Show all transactions.
        return self.tm.get_all_transactions()  
    
    def filter_by_date(self, start_date, end_date):
        #Filter transactions by date range.
        transactions = self.tm.get_all_transactions()
        return [t for t in transactions if start_date <= t['date'] <= end_date] 
    
    def filter_by_category(self, category):
        #Filter transactions by category.
        return self.tm.get_transactions_by_category(category)