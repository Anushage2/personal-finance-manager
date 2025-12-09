import csv
import os

EXPENSE_FILE = "data/expenses.csv"
INCOME_FILE = "data/income.csv"

os.makedirs("data", exist_ok=True)

# Initialize CSV files if not exist
if not os.path.isfile(EXPENSE_FILE):
    with open(EXPENSE_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "category", "amount", "note"])

if not os.path.isfile(INCOME_FILE):
    with open(INCOME_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "source", "amount", "note"])

def save_expense(expense):
    with open(EXPENSE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([expense.date, expense.category, expense.amount, expense.note])

def save_income(income):
    with open(INCOME_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([income.date, income.source, income.amount, income.note])

def load_data(file):
    if not os.path.isfile(file):
        return []
    with open(file, "r") as f:
        reader = csv.reader(f)
        next(reader)
        return list(reader)
