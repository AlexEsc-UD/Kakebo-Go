import datetime

class Transaction:
    def __init__(self, id, title, date, value, category, type, description):
        self.id = id
        self.title = title
        self.date = datetime.datetime.strptime(date, '%Y-%m-%d')
        self.value = value
        self.category = category
        self.description = description
        self.type = type



    