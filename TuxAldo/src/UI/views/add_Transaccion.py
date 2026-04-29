import flet as ft
 

from UI.Components.custom_side_bar import CustomBottomBar
from UI.Components.add_trasaction_components import DetailsComponent
from UI.Components.add_trasaction_components import TitleComponent

class AddTransaccionView(ft.View):
    def __init__(self, page: ft.Page):

        self.bottom_bar = CustomBottomBar()
        self._selected_type     = "INGRESO"
        self.details_component = DetailsComponent()
        self.title_component = TitleComponent()




        super().__init__(
            route="/add_transaccion",
            bgcolor="#00021d",
            navigation_bar=self.bottom_bar,
            padding=ft.Padding.only(top=30, left=5, right=5, bottom=10),
            controls=[ft.Column(
                controls=[
                    
                    self.title_component,
                    self.details_component,

                ],
                expand=True
                
                )
                
            ]
        )