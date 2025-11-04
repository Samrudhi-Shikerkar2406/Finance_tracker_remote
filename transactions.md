# 🧾 Transactions Module
### Branch: **transactions**
#### Contributor: **Samrudhi Shikerkar (Project Owner)**  
#### Course: Basic Toolkit for Research 
#### University: Goa University (2025)  
---
## 🎯 Purpose  
The **Transactions Module** serves as the backbone of the **Personal Finance Tracker**.  
It is responsible for recording, organizing, and analyzing all financial activities — including **income** and **expenses** — across multiple categories.  

This module allows users to:  
- Record income and expense transactions with category, amount, and date.  
- Retrieve all transactions in an organized format.  
- Filter transactions based on **type**, **category**, or **date range**.  
- Compute **total income**, **total expense**, and **remaining balance**.  
- Support other modules (Budgeting, History, Visualization) by providing structured financial data.

The Transaction Manager ensures that all financial records are validated, easy to manage, and ready for visualization and analysis across the system.

---

## 🧩 Design Overview  
The **Personal Finance Tracker** is designed using **modular, object-oriented programming (OOP)** principles.  
Each module performs a dedicated function, making the system clean, reusable, and scalable.

The system consists of the following modules:  
- **transactions.py** → Handles income and expense data.  
- **budgeting.py** → Tracks budgets and spending limits.  
- **history.py** → Logs and filters past financial records.  
- **visualization.py** → Displays spending trends using charts.  

The `TransactionManager` class in `transactions.py` is the **core data engine**, responsible for ensuring that all other modules receive accurate and categorized data.

### ⚙️ Software Design Principles

| Principle | Description |
|------------|-------------|
| **Modularity** | Each file (module) performs a distinct task for clean integration. |
| **Encapsulation** | Transaction data is securely managed within class methods. |
| **Reusability** | Functions can be reused for reporting, budgeting, and visualization. |
| **Scalability** | Supports adding new categories, transaction types, or storage backends. |
| **Testability** | Uses test-driven approach for validation without user input. |

---

## 🔁 Data Flow and Module Interaction  

### 1. **Transaction Management (transactions.py)**  
- Handles all income and expense entries.  
- Each transaction contains:  
  - **type:** income or expense  
  - **category:** e.g., Food, Salary, Transport  
  - **amount:** transaction value  
  - **date:** automatically recorded  

### 2. **Budget Control (budgeting.py)**  
- Uses transaction data to compare spending vs. budget.  
- Helps users track limits and remaining balances.  

### 3. **History Tracking (history.py)**  
- Logs transactions and updates in chronological order.  
- Provides filtering by date or category for review.  

### 4. **Visualization (visualization.py)**  
- Accesses categorized transactions to create visual insights such as pie charts and bar graphs. 

### 5. **Test Execution (main.py):**  
   - The program begins with predefined test cases that simulate user interactions like setting budgets, adding transactions, and verifying results.

### 6. **Output and Validation:**  
   - All module outputs (budgets, transactions, summaries) are printed to the console or verified through assertions in test cases.  
   - No direct user input is taken — validation happens via automated test results.

---

## 🚀 Features of the Transaction Module  
# Transactions Module
[![Transactions Module](https://img.shields.io/badge/Transactions%20Module-Samrudhi%20Shikerkar-blue)](https://github.com/Samrudhi-Shikerkar2406/Finance_tracker_remote/blob/master/transactions.py)

## Features

The Transactions Module offers a set of powerful yet simple features to handle all financial activities.

### 1. **Add Transaction**
Records a new income or expense with input validation and categorization.
- Prevents invalid or missing data.
- Automatically timestamps each transaction.
**Example:**
```python
tm.add_transaction(1000, "Salary", "income", "2025-10-01")
tm.add_transaction(300, "Food", "expense", "2025-10-03")
```
### 2. **Get All Transactions**
Retrieves a list of all recorded transactions in a structured format for display or further processing.
**Example:**
```python
print(tm.get_all_transactions())
```

### 3. **Filter Transactions**
Enables filtering by:
- **Category** (e.g., only “Food” transactions)
- **Type** (income/expense)
- **Date Range** (between given start and end dates)
**Example:**
```python
print(tm.get_transactions_by_category("Food"))
print(tm.get_transactions_by_type("expense"))
print(tm.get_transactions_by_date_range("2025-10-01", "2025-10-31"))
```

### 4. **Calculate Totals**
Computes:
- Total Income  
- Total Expense  
- Net Balance  
**Example:**
```python
print(tm.calculate_total("income"))
print(tm.calculate_total("expense"))
```
**Expected Output:**
```bash
Total Income: 1000
Total Expense: 300
Net Balance: 700
```

### 5. **Data Summary**
Provides quick insights like:
- Number of transactions recorded  
- Highest expense category  
- Average income per entry  


### Summary
The Transactions Module is the foundation of the Personal Finance Tracker, offering flexibility, transparency, and accurate computation of all transactions.
It integrates seamlessly with the Budgeting, History, and Visualization modules for end-to-end financial management.
---

## ️🧩  Installation

Follow these steps to set up and run the **Personal Finance Tracker** project locally:

#### Clone the Repository
Use the following command to clone the project from GitHub:
```bash
git clone https://github.com/Samrudhi-Shikerkar2406/Finance_tracker_remote.git
```

#### Navigate to the Project Folder
Move into the project directory:
```bash
cd Finance_tracker_remote
```

#### Verify Python Installation
Ensure that Python 3.13.0 is installed on your system:
```bash
python --version
```

#### Install Required Libraries
Install all dependencies (specially Matplotlib):
```bash
pip install matplotlib
```

##  Usage & Testing
This project is designed to run using predefined **test cases** (no user input required).  
Each module can be executed individually to verify its functionality.

##### Run the Transactions Module
To run the transaction Module, use the following command:
```bash
python transactions.py
```
---
## 💻  Technologies Used

- **Python 3.13.0** — Core programming language
- **Matplotlib** — For visual representation (pie charts, bar graphs)
- **Visual Studio Code (VS Code)** —IDE used for development
- **Git & GitHub** —For version control and collaboration

---
### 📘  Documentation

Complete project documentation is available in the main repository:

* [https://github.com/Samrudhi-Shikerkar2406/Finance_tracker_remote](https://github.com/Samrudhi-Shikerkar2406/Finance_tracker_remote)

---

## 🔮 Future Enhancements

| Feature | Description |
|----------|--------------|
| Persistent Data Storage | Store all transaction data in CSV/JSON or integrate with SQLite/MySQL for long-term use. |
| Real-Time Input Handling | Add CLI or GUI inputs for interactive data entry. |
| Automated Reports | Generate weekly/monthly summaries in PDF or HTML format. |
| Expense Analytics Dashboard | Use Seaborn or Plotly for interactive trend visualizations. |
| User Profiles & Authentication | Allow multi-user access with personalized data. |

---

### 👩‍ Author

![Author: Samrudhi Shikerkar](https://img.shields.io/badge/Author-Samrudhi%20Shikerkar-blue)
Developed as part of the Personal Finance Tracker project.
This module focuses on recording and managing transactions, forming the backbone of the system’s financial operations.

---

💻 **Tools & Technologies:** Python  | VS Code | Matplotlib | Git and Github
📅 **Created:** 2025  
🔗 **GitHub Profile:** [Samrudhi-Shikerkar2406](https://github.com/Samrudhi-Shikerkar2406)

![Python](https://img.shields.io/badge/Python-3.13.0-pink) ![VS Code](https://img.shields.io/badge/Code_Editor-VS%20Code-green) ![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-red) [![GitHub](https://img.shields.io/badge/GitHub_Repository-Finance_Tracker_Remote-yellow)](https://github.com/Samrudhi-Shikerkar2406/Finance_tracker_remote)[![Transactions Module](https://img.shields.io/badge/Transactions%20Module-Samrudhi%20Shikerkar-blue)](https://github.com/Samrudhi-Shikerkar2406/Finance_tracker_remote/blob/master/transactions.py)
