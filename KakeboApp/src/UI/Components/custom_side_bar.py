import flet as ft

class CustomSideBar(ft.Container):
    def __init__(self):
        super().__init__(selected=False,
                         destinations=[
                                ft.NavigationRailDestination(icon=ft.icons.HOME, label="Home"),
                                ft.NavigationRailDestination(icon=ft.icons.USER, label="Profile"),

                         ],)
        self.bgcolor = "#04002B"
        self.width = 200
        self.height = self.expand
        self.padding = ft.padding.symmetric(vertical=20, horizontal=10)
        self.border_radius = 20
        self.border = ft.border.all(1, "#1B263B")
        self.shadow = ft.BoxShadow(
            blur_radius=15,
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
            offset=ft.Offset(0, 4)
        )
      
        