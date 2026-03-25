import datetime
import locale

try:
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') 
except:
    locale.setlocale(locale.LC_TIME, 'spanish')



class Day:
    def __init__(self, date):
        self.date = datetime.datetime.strptime(date, '%Y-%m-%d')
        self.transactions = []
        self.title = self.date.strftime("%A").capitalize()  # Nombre del día de la semana
        self.incomes = 0
        self.expenses = 0
        self.balance = 0
    #agrega una nueva transaccion
    def add_transaction(self, transaction):

        self.transactions.append(transaction)
        self.calculate_balance()

    #calculo del balance del dia 
    def calculate_balance(self):

        self.income = 0
        self.expense = 0
        self.balance = 0

        for transaction in self.transactions:
            if transaction.type == 'expense':
                self.expense += transaction.value
            else:
                self.income += transaction.value
        self.balance = self.income - self.expense       