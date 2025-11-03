# 📊 Visualization Module

### Author: Anusha Shrivatsava  
### Branch: visualization

## Overview
The Visualization module is part of the Personal Finance Tracker project. It is responsible for visualizing financial data, specifically by creating pie charts to display the distribution of expenses across different categories. Additionally, it provides simple console-based alert notifications for important user messages such as nearing expense limits.

## Features
- Generates a pie chart that visually summarizes expense distribution by category.
- Prints alert notifications to the console.
- Handles empty expense data gracefully by notifying the user when no expense transactions exist.

## Implementation Details
- Implemented in Python using the `matplotlib` library for chart plotting.
- The `VisualizationManager` class takes a list of transaction dictionaries and processes only those with `'type'` set to `'expense'`.
- Pie chart is generated dynamically based on categories and their cumulative amounts.
- Notifications are printed as console messages.

## Dependencies
- Python 3.x
- matplotlib (`pip install matplotlib`)

## Usage
1. Import the module or run as a standalone script.
2. Create a list of transactions where each transaction is a dictionary with keys: `'type'`, `'category'`, and `'amount'`.
3. Instantiate the `VisualizationManager` with the transactions list.
4. Call `plot_expense_pie()` to display the pie chart.
5. Use `notify(message)` to print alert messages.


