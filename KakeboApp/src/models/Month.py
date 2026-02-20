import datetime

class Month:
    def __init__(self, month_title, date_start):
        self.month_title = month_title    
        self.date = datetime.datetime.strptime(date_start, '%Y-%m-%d')
        self.weeks = []
        self.balance_month = 0
    

    def calculate_balance(self):

        self.balance_month = 0

        for week in self.weeks:
            
            self.balance_month += week.week_balance