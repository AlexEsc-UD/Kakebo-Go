import flet as ft



from UI.Components.UpperFrame import UpperFrame
from UI.Components.ScrollableList import ScrollableCardList
from UI.Components.custom_side_bar import CustomBottomBar


from UI.Components.period_button import PeriodButton

from models.Month import Month
from models.day import Day
from models.week import Week


class HomeView(ft.View):
    def __init__(self,  page: ft.Page, obj1 : Day, obj2: Week, obj3: Month):


        self.obj1 = obj1
        self.obj2 = obj2
        self.obj3 = obj3
        self.bottom_bar = CustomBottomBar()
        self.period_buttons = ft.Column(
            controls=[
                PeriodButton(obj1),
                PeriodButton(obj2),
                PeriodButton(obj3)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=5
        )
        
        
        super().__init__(
            route="/",
            bgcolor="#00021d",
            padding= ft.Padding.only(top=30,left=5,right=5, bottom=10),
            navigation_bar=self.bottom_bar,
            controls=[ft.Column(
                controls=[

                    self.period_buttons

                    
                ],
                expand=True
             
                )
            ]
        )


                         
                         
                         
                         
        
        
        