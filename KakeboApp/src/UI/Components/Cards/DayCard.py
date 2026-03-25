import flet as ft
from models.day import Day

class DayCard(ft.Container):
    def __init__(self, day_obj: Day):
        super().__init__()
        self.bgcolor = "#04002B"
        self.width = self.expand
        self.height = 120
        self.border_radius = 20
        self.padding = 15
        self.margin = ft.margin.only(bottom=10)
        self.border = ft.border.all(1, "#1B263B")
        self.shadow = ft.BoxShadow(
            blur_radius=15, 
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK), 
            offset=ft.Offset(0, 4)
        )

        prefix = "+" if day_obj.balance >= 0 else "-"

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[

                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[

                        ft.Text(day_obj.title, size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Text(day_obj.date.strftime("%d/%m"), size=10, color=ft.Colors.GREY_400),
                    
                        
                    ]
                ),

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            spans=[
                                ft.TextSpan("In: ", ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE)),
                                ft.TextSpan(f"${day_obj.incomes:,.2f}", ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.GREEN_ACCENT_400))
                            ],
                            size=14,


                        ),
                        ft.Text(
                            spans=[
                                ft.TextSpan("Egr: ", ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE)),
                                ft.TextSpan(f"${day_obj.expenses:,.2f}", ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.RED_ACCENT_400))
                            ],
                            size=14,
                            
                        ),
                    ]
                ),

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            spans=[
                                ft.TextSpan(f"Bal: ", ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE)),
                                ft.TextSpan(f"{prefix} ${abs(day_obj.balance):,.2f}", ft.TextStyle(weight=ft.FontWeight.BOLD,color="#ffd900"))
                            ],
                            size=14,
                            
                        ),

                        
                        
                    ]
                )
            ,
            ]
        )

    def on_click(self, e):
        self.page.go("/day")