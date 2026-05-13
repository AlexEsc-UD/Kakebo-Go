import sqlite3 as sql
from config import DB_NAME
from models.week import Week

class WeekDao:

    def save_week(self, month_id, start_date, end_date):
        with sql.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO weeks (month_id, start_date, end_date)
                VALUES (?, ?, ?)
            ''', (month_id, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))

            return cursor.lastrowid

    def get_weeks_by_month(self, month_id):
        with sql.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT id, month_id, start_date, end_date
                FROM weeks
                WHERE month_id = ?
            ''', (month_id,))

            rows = cursor.fetchall()

            weeks = []
            week_number = 1
            for row in rows:
                title= f"Semana {week_number}"
                week = Week(id=row[0], title=title, start_date=row[2], end_date=row[3])
                weeks.append(week)
                week_number += 1

        return weeks