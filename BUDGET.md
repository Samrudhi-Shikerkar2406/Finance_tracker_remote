# Budget Module
---
## Purpose
The Budgeting Module serves as the core component of the Personal Finance Tracker. Its main purpose is to help users effectively manage, monitor, and analyze their personal budgets for different expense categories.
This module allows users to:
- Set a budget limit for specific categories such as food, transport, entertainment, etc.
- Retrieve the allocated budget for any category.
- Track real-time spending against each category’s budget.
- View remaining (pending) balance to stay within budget.
- Update existing budgets as financial goals change.
- List all current budgets for a quick overview of financial planning.

By implementing these functionalities, the budgeting module ensures that users can maintain financial discipline, avoid overspending, and make data-driven financial decisions.

## Design Overview
The Personal Finance Tracker is built with a modular, object-oriented architecture that ensures scalability, reusability, and maintainability.  
The system is divided into logical components (modules), each focusing on a single responsibility — such as budgeting, transaction management, reporting, and visualization.  
The system is executed and verified through **test cases** rather than direct user input, ensuring automated validation of functionality and consistency.

The design of this application is guided by key software engineering principles:

| Principle | Description |
|------------|-------------|
| **Modularity** | Each module performs a distinct function — promoting code organization and maintainability. |
| **Encapsulation** | Data related to each module (budgets, transactions, history, visualization) is managed through its own class and methods. |
| **Scalability** | The structure allows easy expansion — e.g., adding investment tracking, savings goals, or user accounts. |
| **Reusability** | Code such as `BudgetManager` or transaction handling functions can be reused in other finance-related projects. |
| **Testability** | Unit tests ensure reliable and verifiable components. |

### **Data Flow and Module Interaction**

Below is the step-by-step logical flow of data within the system:

1. **Transaction Management (transactions.py):**  
   - Handles creation and storage of income and expense transactions.  
   - Each transaction contains attributes such as category, amount, and type (`income` or `expense`).

2. **Budget Control (budgeting.py):**  
   - The `BudgetManager` class manages budgets for each category.  
   - It compares actual spending (from transactions) against the allocated budget.  
   - Returns detailed summaries such as total spent, remaining balance, and overspending warnings.

3. **History Tracking (history.py):**  
   - Logs and organizes past transactions, updates, and changes in budgets.  
   - Provides chronological summaries for analysis or debugging.  
   - Acts as a lightweight ledger to maintain historical financial activity.

4. **Visualization (visualization.py):**  
   - Uses **Matplotlib** to graphically represent financial data.  
   - Produces bar charts, pie charts, and trend graphs to compare spending patterns.  
   - Enables easy interpretation of results from test data.

5. **Test Execution (main.py):**  
   - The program begins with predefined test cases that simulate user interactions like setting budgets, adding transactions, and verifying results.

6. **Output and Validation:**  
   - All module outputs (budgets, transactions, summaries) are printed to the console or verified through assertions in test cases.  
   - No direct user input is taken — validation happens via automated test results.

## Features of the Budgeting Module

The Budgeting Module provides several key features to help users efficiently manage their financial plans and spending habits. Each feature is designed to simplify budget tracking and ensure financial control.

##### 1. Set Budget
- Allows users to define a spending limit for different categories such as Food, Transport etc.
- This helps users allocate their income into specific purposes and avoid overspending.

**Example:**
```python
print(manager.set_budget("Food", 5000))
```

##### 2. Get Budget
- Retrieves the current budget amount assigned to a particular category.
- If no budget has been set for that category, it returns 0 by default — helping prevent errors during budget calculations.

**Example:**
```python
print(manager.get_budget("Food"))
```

##### 3. Track Spending
Calculates total expenses for each category and compares it with the assigned budget.
The module provides details on:
- Total Budget
- Amount Spent
- Remaining (Pending) Amount

**Example:**
```python
transactions = [
    {"category": "Food", "type": "expense", "amount": 1200},
    {"category": "Transport", "type": "expense", "amount": 800},
]

result = manager.check_spending("Food", transactions)
print(result)
```

This helps users instantly see where they stand financially.

##### 4. Update Budget
- Enables users to modify a previously set budget if their spending plan changes.
- This feature ensures flexibility and adaptability for real-world financial adjustments.

**Example:**
```python
print(manager.update_budget("Food", 6000))
```

##### 5. List Budgets
- Displays all active budgets along with their assigned amounts.
- This gives a quick summary view of the user’s overall financial allocation.

**Example:**
```python
print(manager.list_budgets())
```

## ️ Installation

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
Install all dependencies (mainly Matplotlib for visualization):
```bash
pip install matplotlib
```
You can also create a requirements.txt later if you want to automate this step.

##  Usage & Testing
This project is designed to run using predefined **test cases** (no user input required).  
Each module can be executed individually to verify its functionality.

##### Run the Budget Module
To test the Budgeting Module, run the following command:
```bash
python budgeting.py
```
##  Technologies Used

The budget module was developed using the technologies and tools listed below.

- **Python 3.13.0** — Core language for module logic and tests.
- **Matplotlib** — Charts and visualizations (bar, pie, line).
- **Visual Studio Code (VS Code)** — Development environment.
- **Git & GitHub** — Version control and repository hosting.

### Documentation

Complete documentation for this project can be found in the README file on GitHub:

* [https://github.com/Samrudhi-Shikerkar2406/Finance_tracker_remote](https://github.com/Samrudhi-Shikerkar2406/Finance_tracker_remote)

### **Future Enhancements**

| Feature | Description |
|----------|-------------|
| **Persistent History Storage** | Save transaction and budget data to files (CSV/JSON) for long-term access. |
| **Dynamic Data Input** | Extend the design to accept real-time user input or GUI-based inputs. |
| **Automated Monthly Reports** | Generate PDF or HTML reports summarizing financial performance. |
| **Advanced Data Visualization** | Use Seaborn or Plotly for interactive dashboards. |

### Author

![Author: Falak Sardar](https://img.shields.io/badge/Author-Falak_Sardar-orange)

Developed as part of the **Personal Finance Tracker** project.  
This module focuses on budget management, including setting, updating, and tracking category-wise spending.  

💻 **Tools & Technologies:** Python  | VS Code | Matplotlib  
📅 **Created:** 2025  
🔗 **GitHub Profile:** [Samrudhi-Shikerkar2406](https://github.com/Samrudhi-Shikerkar2406)

![Python](https://img.shields.io/badge/Python-3.13.0-blue) ![VS Code](https://img.shields.io/badge/Code_Editor-VS%20Code-blueviolet) ![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-red) [![Budgeting Module](https://img.shields.io/badge/Budgeting%20Module-Falak_Sardar-brightgreen)](https://github.com/Samrudhi-Shikerkar2406/Finance_tracker_remote/blob/master/budgeting.py)
[![GitHub](https://img.shields.io/badge/GitHub_Repository-Finance_Tracker_Remote-yellow)](https://github.com/Samrudhi-Shikerkar2406/Finance_tracker_remote)



