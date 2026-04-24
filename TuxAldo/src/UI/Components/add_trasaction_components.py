import flet as ft
from datetime import datetime

from UI.Components.custom_textfield import CustomTextField

class TitleComponent(ft.Container):

    def __init__(self):
        super().__init__()

        self.today = datetime.now().strftime("%d/%m")
        self.title_textfield = CustomTextField("Pago de ...", False, False)

        self.bgcolor = "#04002B"
        self.width = self.expand
        self.height = 100
        self.border_radius = 20
        self.padding = 15
        self.margin = ft.Margin.only(bottom=10)
        self.border = ft.Border.all(1, "#1B263B")
        self.shadow = ft.BoxShadow(
            blur_radius=15, 
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK), 
            offset=ft.Offset(0, 4)
        )

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[

                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        
                        ft.Text("Titulo", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Text(self.today, size=10, color=ft.Colors.GREY_400),
                    ]
                ),
                self.title_textfield




            ]

        )
