class Income:
    def __init__(self, date, source, amount, note=""):
        self.date = date
        self.source = source
        self.amount = float(amount)
        self.note = note
