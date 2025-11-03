#### 🟢 Falak (Budget branch)

# 💵 Budget Management Module

### Author: Falak Sardar  
### Branch: `budget`

---

## 📘 Overview
This module allows users to create, update, and track budgets for various expense categories.

---

## ✨ Features Implemented
- Set budgets for different categories.
- Track spending progress.
- Update existing budgets dynamically.

---

## 🧮 Key Functions
- `set_budget()`
- `get_budget()`
- `check_spending()`
- `update_budget()`

---

## 📊 Example
python
bm = BudgetManager()
bm.set_budget("Food", 5000)
print(bm.check_spending("Food", transactions))