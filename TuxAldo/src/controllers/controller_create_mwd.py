import datetime
import calendar

from Database.Repositories import Repository_Year
from Database.Repositories import Repository_Month
from Database.Repositories import Repository_Week




class ControllerCreateMWD:

    id_year = None
    id_month = None
    id_week = None
    id_day = None

    def __init__ (self):
        self.date = datetime.date.today()

    def create_year(self):

        year = self.date.year
        year_dao = Repository_Year.YearDao()
        self.id_year = year_dao.save_year(year)

           
        self.create_months(self.id_year)




    def create_months(self, id_year):

        year_val = self.date.year 

        for month_idx in range(1, 13):

            month_title = calendar.month_name[month_idx]
            # Creamos la fecha del primer día de ese mes automáticamente
            month_date = f"{year_val}-{month_idx:02d}-01" 
        
            month_dao = Repository_Month.MonthDao()
            # Ahora pasas la fecha generada, no una externa
            self.id_month = month_dao.save_month(id_year, month_title, month_date)

            self.create_week(self.date.year, self.id_month, month_idx)


     

    def create_week(self, year, id_month, month_number):

        week_dao = Repository_Week.WeekDao()

        cal = calendar.monthcalendar(year, month_number)

        for week_days in cal:
            real_days = [d for d in week_days if d != 0]
            if not real_days: continue

            start_w = datetime.date(year, month_number, real_days[0])
            end_w = datetime.date(year, month_number, real_days[-1])

            # Guardamos la semana vinculada al mes

            week_dao.save_week(id_month, start_w, end_w)



            



