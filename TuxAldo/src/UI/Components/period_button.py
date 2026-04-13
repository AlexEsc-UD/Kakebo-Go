import flet as ft
from models.day import Day
from models.week import Week
from models.Month import Month

class PeriodButton(ft.Container):
    def __init__(self, obj):
        super().__init__()
        self.bgcolor = "#04002B"
        self.width = self.expand
        self.height = 50
        self.border_radius = 20
        self.padding = ft.Padding.symmetric(vertical=10, horizontal=15)
        self.margin = ft.Margin.symmetric(horizontal=5, vertical=0)
        self.border = ft.Border.all(1, "#1B263B")
        self.shadow = ft.BoxShadow(
            blur_radius=15,
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
            offset=ft.Offset(0, 4)
        )
        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text(obj.title, size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text(self._format_date(obj), size=12, color=ft.Colors.GREY_400)
            ]
        )

    def _format_date(self, obj) -> str:
        if isinstance(obj, Day):
            return obj.date.strftime("%d/%m")
        elif isinstance(obj, Week):
            return f"{obj.start_date.strftime('%d/%m')} - {obj.end_date.strftime('%d/%m')}"
        elif isinstance(obj, Month):
            return obj.date.strftime("%Y")

        return ""
    
    def on_click(self, e):
        pass