import datetime

class Month:
    def __init__(self, month_title, date, year):
        self.month_title = month_title    
        self.date = datetime.datetime.strptime(date, '%Y-%m-%d')
        self.year = self.date.year
        self.weeks = []
        self.balance_month = 0
    

    def calculate_balance(self):

        self.balance_month = 0

        for week in self.weeks:
            
            self.balance_month += week.week_balance