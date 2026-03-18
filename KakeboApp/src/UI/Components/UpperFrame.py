import flet as ft
from models.Day import Day
from models.Week import Week
from models.Month import Month



class UpperFrame(ft.Container):

    def __init__(self, day_obj: Day):
        super().__init__()
        self.bgcolor = "#04002B"
        self.width = self.expand
        self.height = 50
        self.border_radius = 20
        self.padding = ft.padding.symmetric(vertical=10, horizontal=15)
        self.margin = ft.margin.symmetric(horizontal=5, vertical=0)
        self.border = ft.border.all(1, "#1B263B")
        self.shadow = ft.BoxShadow(
            blur_radius=15, 
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK), 
            offset=ft.Offset(0, 4)
        )

        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[

                
                ft.Text(day_obj.title, size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text(day_obj.date.strftime("%d/%m"), size=12, color=ft.Colors.GREY_400)
            ]

        )




    