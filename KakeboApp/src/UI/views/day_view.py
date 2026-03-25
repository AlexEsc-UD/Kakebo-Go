import flet as ft


from UI.Components.UpperFrame import UpperFrame
from UI.Components.ScrollableList import ScrollableCardList
from UI.Components.down_frame import DownFrame

from UI.Components.Cards.Transaction_Card import TransactionCard

from models.day import Day


class DayView(ft.View):
    def __init__(self,  page: ft.Page, day: Day):


        
        self.day = day
        self.upper_frame = UpperFrame(day)
        self.transaction_list = ScrollableCardList([TransactionCard(t) for t in day.transactions])
        self.down_frame = DownFrame()   
        
        
        super().__init__(
            route="/day",
            bgcolor="#00021d",
            padding=0,
            controls=[ft.Column(
                controls=[
                    self.upper_frame,
                    self.transaction_list,
                    self.down_frame
                ],
                expand=True
             
                )
            ]
        )
                         
                         
                         
                         
        
        
        