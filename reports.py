import pandas as pd
import matplotlib.pyplot as plt
from file_manager import EXPENSE_FILE, INCOME_FILE

def show_expense_report():
    df = pd.read_csv(EXPENSE_FILE)
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["amount"])
    print("\n📊 Expense Summary by Category:")
    summary = df.groupby("category")["amount"].sum()
    print(summary)
    summary.plot(kind="bar", title="Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()

def show_income_report():
    df = pd.read_csv(INCOME_FILE)
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["amount"])
    print("\n📊 Income Summary by Source:")
    summary = df.groupby("source")["amount"].sum()
    print(summary)
    summary.plot(kind="bar", title="Income by Source")
    plt.xlabel("Source")
    plt.ylabel("Amount")
    plt.show()

def monthly_balance():
    df_exp = pd.read_csv(EXPENSE_FILE)
    df_inc = pd.read_csv(INCOME_FILE)
    df_exp["amount"] = pd.to_numeric(df_exp["amount"], errors="coerce")
    df_inc["amount"] = pd.to_numeric(df_inc["amount"], errors="coerce")
    df_exp["month"] = df_exp["date"].str[:7]
    df_inc["month"] = df_inc["date"].str[:7]
    exp_monthly = df_exp.groupby("month")["amount"].sum()
    inc_monthly = df_inc.groupby("month")["amount"].sum()
    balance = pd.DataFrame({"Income": inc_monthly, "Expenses": exp_monthly}).fillna(0)
    print("\n📘 Monthly Balance:")
    print(balance)
    balance.plot(kind="bar", title="Income vs Expenses")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.show()
