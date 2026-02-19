import datetime

class Day:
    def __init__(self, date):
        self.date = datetime.datetime.strptime(date, '%Y-%m-%d')
        self.transactions = []
    
    def add_transaction(self, transaction):

        self.transactions.append(transaction)
        self.calculate_balance()

    def calculate_balance(self):

        self.balance = 0

        for transaction in self.transactions:
            if transaction.type == 'expense':
                self.balance -= transaction.value
            else:
                self.balance += transaction.value