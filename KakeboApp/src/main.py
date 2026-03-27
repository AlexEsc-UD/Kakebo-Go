import flet as ft

from models import day
from models.Transaction import Transaction
from models.day import Day
from models.week import Week
from models.Month import Month


# Asegúrate de que las rutas de importación coincidan con tu estructura

from UI.Components.Cards.Transaction_Card import TransactionCard
from UI.Components.Cards.DayCard import DayCard
from UI.Components.Cards.WeekCard import WeekCard
from UI.Components.Cards.MounthCard import MonthCard
from UI.Components.ScrollableList import ScrollableCardList
from UI.Components.UpperFrame import UpperFrame
from UI.Components.down_frame import DownFrame
from UI.views.day_view import DayView


def main(page: ft.Page):


    page.title = "Kakebo GO - Dashboard"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#00021d"
    page.padding = 0


    # Título de la sección


    # Transacción de prueba
    transac = Transaction(1, "Salario", "2024-06-15", 1750000, "Trabajo", "income", "Pago mensual de nómina")
    transac2 = Transaction(2, "Supermercado", "2024-06-15", 250000, "Comida", "expense", "Compra semanal")
    transac3 = Transaction(3, "Compra de medicamentos", "2024-06-16", 22000, "Salud", "expense", "compra de medicacion")
    transac4 = Transaction(1, "Mesada semanal", "2024-06-17", 100000, "Ganancia ocasional", "income", "Pago mensual de nómina")
    transac5 = Transaction(1, "Venta de ropa usada", "2024-06-17", 50000, "Ganancia ocasional", "income", "Pago mensual")
    transac6 = Transaction(1, "Cena con amigos", "2024-06-18", 80000, "Ocio", "expense", "Salida a cenar con amigos")
    transac7 = Transaction(1, "Pago de servicios", "2024-06-18", 150000, "Hogar", "expense", "Pago mensual de servicios")


    day1 = Day("2024-06-15")
    day2 = Day("2024-06-16")
    day3 = Day("2024-06-17")
    day4 = Day("2024-06-18")

    week1 = Week("Semana 1", "2024-06-10", "2024-06-16")
    week2 = Week("Semana 2", "2024-06-17", "2024-06-23")

    mounth1 = Month("Junio", "2024-06-01")
    



    day1.add_transaction(transac)
    day1.add_transaction(transac2)
    day2.add_transaction(transac3)
    day3.add_transaction(transac4)
    day3.add_transaction(transac5)
    day4.add_transaction(transac6)
    day4.add_transaction(transac7)  

    week1.add_day(day1)
    week1.add_day(day2)
    week2.add_day(day3)
    week2.add_day(day4)

    mounth1.add_week(week1)
    mounth1.add_week(week2)

    ListCard = [
        DayCard(day1),
        DayCard(day2),
        TransactionCard(transac),
        TransactionCard(transac2),
        TransactionCard(transac3),
        TransactionCard(transac4),
        TransactionCard(transac5),
        TransactionCard(transac6),
        TransactionCard(transac7),
        WeekCard(week1),
        WeekCard(week2),
        MonthCard(mounth1)
    ]

    

    def route_change(e):
        page.views.clear()

        if page.route == "/day":
            page.views.append(DayView(page, day1))  # Aquí puedes pasar el día que quieras mostrar
        
        elif page.route == "/":
        
            page.go("/day") # Aquí puedes pasar el día que quieras mostrar
        page.update()

    def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)
        page.update()

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go("/day")  # Navega a la vista del día al iniciar la aplicación



    

    # Añadimos las tarjetas
ft.run(main)