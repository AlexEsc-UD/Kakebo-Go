import flet as ft
import datetime 

from UI.Components.custom_side_bar import CustomBottomBar

class AddTransaccionView(ft.View):
    def __init__(self, page: ft.Page, on_add, on_cancel):

        self.bottom_bar = CustomBottomBar()
        self.on_add_callback    = on_add
        self.on_cancel_callback = on_cancel
        self._selected_type     = "INGRESO"
        self._today             = datetime.now().strftime("%d/%m")




        super().__init__(
            route="/add_transaccion",
            bgcolor="#00021d",
            navigation_bar=self.bottom_bar,
            padding=ft.Padding.only(top=30, left=5, right=5, bottom=10),
            controls=[ft.Column(
                controls=[






                ],
                expand=True
                
                )
                
            ]
        )