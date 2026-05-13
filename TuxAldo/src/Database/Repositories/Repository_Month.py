import sqlite3 as sql
from config import DB_NAME
from models.Month import Month

class MonthDao:


    #funcion de guardado en la base de datos 
        #toma 
    def save_month(self, year_id, month_title, month_date):
        with sql.connect(DB_NAME) as conn:

            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO months (year_id, month_title, date_start)
                VALUES (?, ?, ?)
            ''', (year_id, month_title, month_date))


            return cursor.lastrowid

    def get_months_by_year(self, year_id):

        with sql.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT id, year_id, month_title, date_start
                FROM months
                WHERE year_id = ?
            ''', (year_id,))

            rows = cursor.fetchall()

            months = []
            for row in rows:
                month = Month(id=row[0],title=row[2], date_start=row[3])
                months.append(month)

        return months

