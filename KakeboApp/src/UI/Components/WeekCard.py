import flet as ft
from models.Week import Week

class WeekCard(ft.Container):
    def __init__(self, week_obj: Week):
        super().__init__()

        self.bgcolor = "#04002B"
        self.width = self.expand
        self.height = 120
        self.border_radius = 12
        self.padding = 15
        self.margin = ft.margin.only(bottom=10)
        self.border = ft.border.all(1, "#1B263B")
        self.shadow = ft.BoxShadow(
            blur_radius=15, 
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK), 
            offset=ft.Offset(0, 4)
        )

        prefix = "+" if week_obj.balance >= 0 else "-"

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[

                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[

                        ft.Text(week_obj.title, size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Text(f"{week_obj.start_date.strftime("%d/%m")} - {week_obj.end_date.strftime("%d/%m")}", size=10, color=ft.Colors.GREY_400),
                    
                        
                    ]
                ),

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            spans=[
                                ft.TextSpan("INGRESOS: ", ft.TextStyle(color=ft.Colors.WHITE)),
                                ft.TextSpan(f"${week_obj.incomes:.2f}", ft.TextStyle(color=ft.Colors.GREEN_ACCENT_400))
                            ],
                            size=14,


                        ),
                        ft.Text(
                            spans=[
                                ft.TextSpan("GASTOS: ", ft.TextStyle(color=ft.Colors.WHITE)),
                                ft.TextSpan(f"${week_obj.expenses:.2f}", ft.TextStyle(color=ft.Colors.RED_ACCENT_400))
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
                                ft.TextSpan(f"BALANCE: ", ft.TextStyle(color=ft.Colors.WHITE)),
                                ft.TextSpan(f"{prefix} ${abs(week_obj.balance):.2f}", ft.TextStyle(color="#ffd900"))
                            ],
                            size=14,
                            
                        ),

                        
                        
                    ]
                )
            ,
            ]
        )

    

