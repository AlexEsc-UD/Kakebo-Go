import flet as ft
from models.Transaction import Transaction
from models.Day import Day
from models.Week import Week
# Asegúrate de que las rutas de importación coincidan con tu estructura

from UI.Components.Transaction_Card import TransactionCard
from UI.Components.DayCard import DayCard
from UI.Components.WeekCard import WeekCard


def main(page: ft.Page):
    page.title = "Kakebo GO - Dashboard"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#00021d"
    page.padding = 10

    # Título de la sección
    page.add(ft.Text("Historial Reciente", size=24, weight=ft.FontWeight.BOLD))
    page.add(ft.Divider(height=20, color=ft.Colors.TRANSPARENT))

    # Transacción de prueba
    transac = Transaction(1, "Salario", "2024-06-15", 1750000, "Trabajo", "income", "Pago mensual de nómina")
    transac2 = Transaction(2, "Supermercado", "2024-06-15", 250000, "Comida", "expense", "Compra semanal")
    transac3 = Transaction(3, "Compra de medicamentos", "2024-06-16", 22000, "Salud", "expense", "compra de medicacion")
    transac4 = Transaction(1, "Mesada semanal", "2024-06-15", 100000, "Ganancia ocasional", "income", "Pago mensual de nómina")

    day1 = Day("2024-06-15")
    day2 = Day("2024-06-16")

    week1 = Week("Semana 1", "2024-06-10", "2024-06-16")

    day1.add_transaction(transac)
    day1.add_transaction(transac2)
    day2.add_transaction(transac3)
    day2.add_transaction(transac4)

    week1.add_day(day1)
    week1.add_day(day2)
    
    # Añadimos las tarjetas
    page.add(
        TransactionCard(transac),
        TransactionCard(transac2),
        DayCard(day1),
        DayCard(day2),
        WeekCard(week1),



    )



if __name__ == "__main__":
    ft.app(target=main)