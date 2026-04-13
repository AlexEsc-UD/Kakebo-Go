import flet as ft

class CustomBottomBar(ft.NavigationBar):
    def __init__(self):
        super().__init__(
            selected_index=0,
            bgcolor="#04002B",
            border=ft.Border.all(1, "#1B263B"),
            shadow_color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
                ft.NavigationBarDestination(icon=ft.Icons.BAR_CHART, label="Statistics"),
                ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Settings"),
            ],
        )