import flet as ft

class DownFrame(ft.Container):
    def __init__(self):
        super().__init__()
        self.bgcolor = "#04002B"
        self.width = self.expand
        self.height = 70

        self.padding = 15

        self.shadow = ft.BoxShadow(
            blur_radius=15, 
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK), 
            offset=ft.Offset(0, 4)
        )

        self.content = ft.Row(
            controls=[],
            
        )