from expense import Expense
from income import Income
from file_manager import save_expense, save_income, load_data, EXPENSE_FILE, INCOME_FILE
from utils import input_float, input_date
import reports
import shutil
import os
import pandas as pd

def backup_data():
    os.makedirs("backup", exist_ok=True)
    shutil.copy(EXPENSE_FILE, "backup/expenses_backup.csv")
    shutil.copy(INCOME_FILE, "backup/income_backup.csv")
    print("✔ Data backup completed!")

def view_all_expenses():
    data = load_data(EXPENSE_FILE)
    if not data:
        print("No expenses found.")
        return
    df = pd.DataFrame(data, columns=["Date", "Category", "Amount", "Note"])
    print("\n📋 All Expenses:")
    print(df)

def view_all_income():
    data = load_data(INCOME_FILE)
    if not data:
        print("No income found.")
        return
    df = pd.DataFrame(data, columns=["Date", "Source", "Amount", "Note"])
    print("\n📋 All Income:")
    print(df)

def view_category_summary():
    df = pd.read_csv(EXPENSE_FILE)
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["amount"])
    summary = df.groupby("category")["amount"].sum()
    print("\n📊 Expense Category-wise Summary:")
    print(summary)

def search_expenses():
    df = pd.read_csv(EXPENSE_FILE)
    keyword = input("Enter category or note to search: ").lower()
    df_filtered = df[df["category"].str.lower().str.contains(keyword) | df["note"].str.lower().str.contains(keyword)]
    if df_filtered.empty:
        print("No matching expenses found.")
    else:
        print("\n🔍 Search Results:")
        print(df_filtered)

def main_menu():
    while True:
        print("\n==== PERSONAL FINANCE MANAGER ====")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Add New Income")
        print("4. View All Income")
        print("5. View Category-wise Expense Summary")
        print("6. Monthly Income Report")
        print("7. Income vs Expense Overview (Net Savings)")
        print("8. Backup Data")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            date = input_date()
            category = input("Enter category: ")
            amount = input_float("Enter amount: ")
            note = input("Note (optional): ")
            expense = Expense(date, category, amount, note)
            save_expense(expense)
            print("✔ Expense added successfully!")

        elif choice == "2":
            view_all_expenses()

        elif choice == "3":
            date = input_date()
            source = input("Enter income source: ")
            amount = input_float("Enter amount: ")
            note = input("Note (optional): ")
            income = Income(date, source, amount, note)
            save_income(income)
            print("✔ Income added successfully!")

        elif choice == "4":
            view_all_income()

        elif choice == "5":
            view_category_summary()

        elif choice == "6":
            reports.show_income_report()

        elif choice == "7":
            reports.monthly_balance()

        elif choice == "8":
            backup_data()

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("❌ Invalid option. Please try again.")
