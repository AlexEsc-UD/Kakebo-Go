import flet as ft

class CustomButton(ft.Container):
    def __init__(self, text, icon, on_click = None, **kwargs):
        super().__init__(**kwargs)
        self._on_click_callback = on_click
        self.text = text

        self._apply_colors()

        self.bgcolor = "#1B263B"
        self.width = 100
        self.height = 40
        self.border_radius = 10
        self.padding = 10
        self.margin = ft.Margin.only(bottom=10)
        self.border = ft.Border.all(1, "#1B263B")
        self.ink = True
        self.shadow = ft.BoxShadow(
            blur_radius=5, 
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK), 
            offset=ft.Offset(0, 2)
        )
        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Icon(icon, color= self.icon_color(), size=16),
            ]
        )

        self.on_click = self.handle_click

    def icon_color(self):
        if self.text == "Expense":
            self.bgcolor = ft.Colors.RED_ACCENT_400
        else:
            self.bgcolor = ft.Colors.GREEN_ACCENT_400
    
    def handle_click(self, e):
        if self._on_click_callback:
            self._on_click_callback(self.text)  


    