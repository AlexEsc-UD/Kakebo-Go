import datetime

class Week:
    def __init__(self, start_date, end_date, week_target):
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        self.days = []
        self.week_balance = 0
        

    

    def add_day(self, day):
        self.days.append(day)
        self.calculate_balance()

    def calculate_balance(self):
        self.week_balance = 0

        for day in self.days:
            day.calculate_balance()
            self.week_balance += day.balance