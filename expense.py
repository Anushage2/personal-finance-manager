class Expense:
    def __init__(self, date, category, amount, note=""):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.note = note
