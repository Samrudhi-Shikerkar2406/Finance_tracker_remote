# 🧾 Transaction Management Module  
### Branch: **transactions**
#### Contributor: **Samrudhi Shikerkar (Project Owner)**  
#### Course: Basic Toolkit for Research 
#### University: Goa University (2025)  

---

## 📘 Overview
This module handles all transaction-related operations in the Personal Finance Tracker.

---

## 🧰 Purpose  
The Transaction Management System handles all financial operations — from recording user transactions to computing total income, expenses, and remaining balances.  
It ensures that every other module in the system receives accurate, structured financial data.

---

## 💡 Design Overview  
Each transaction is treated as a structured record containing:
- **Amount**
- **Category** (e.g., Food, Transport, Salary)
- **Type** (Income or Expense)
- **Date**
- **Optional Notes**

The system supports adding, filtering, viewing, and summarizing transactions.  
This modular approach allows seamless integration with other components like **Budgeting** (which checks spending limits) and **Visualization** (which plots expense charts).

---

## ✨ Features Implemented
- Add, view, and filter transactions.
- Manage income and expense types.
- Store category, date, and notes.
- Calculate total income or expenses.

---

## 🧮 Key Functions
- `add_transaction()`
- `get_all_transactions()`
- `get_transactions_by_category()`
- `calculate_total()`

---

## 📊 Testing Example
python
tm = TransactionManager()
tm.add_transaction(1000, "Salary", "income")
tm.add_transaction(200, "Food", "expense")
print(tm.calculate_total("expense"))