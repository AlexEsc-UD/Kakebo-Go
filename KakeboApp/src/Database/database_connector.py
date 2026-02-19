import sqlite3 as sql

class DatabaseConnector:

    def __init__(self, db_name = 'kakebo.db'):
        self.db_name = db_name
        self.conn = sql.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        cursor = self.cursor

        cursor.execute('PRAGMA foreign_keys = ON;')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS years (
                id INTEGER PRIMARY KEY,
                year_number TEXT NOT NULL UNIQUE
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS months (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                year_id INTEGER NOT NULL,
                month_title TEXT NOT NULL,
                date TEXT NOT NULL,
                FOREIGN KEY (year_id) REFERENCES years (id) ON DELETE CASCADE
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS weeks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                month_id INTEGER NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                FOREIGN KEY (month_id) REFERENCES months (id) ON DELETE CASCADE
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS months (
                id INTEGER PRIMARY KEY,
                month_title TEXT NOT NULL UNIQUE,
                date TEXT NOT NULL,
                year_id INTEGER,
                FOREIGN KEY (year_id) REFERENCES years(id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                date TEXT NOT NULL,
                value REAL NOT NULL,
                category TEXT NOT NULL,
                type TEXT NOT NULL,
                description TEXT
            )
        ''')
        self.conn.commit()

