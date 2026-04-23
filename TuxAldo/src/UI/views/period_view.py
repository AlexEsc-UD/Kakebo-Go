import flet as ft



from UI.Components.UpperFrame import UpperFrame
from UI.Components.ScrollableList import ScrollableCardList
from UI.Components.custom_side_bar import CustomBottomBar


from UI.Components.Cards.Transaction_Card import TransactionCard
from UI.Components.balance_frame import BalanceFrame 
from UI.Components.Cards.general_card import GeneralCard
from UI.Components.custom_textfield import CustomTextField


from models.Month import Month
from models.day import Day
from models.week import Week

from UI.Components.type_selector import CustomButton

class PeriodView(ft.View):
    def __init__(self,  page: ft.Page, obj):

        self.obj = obj
        self.upper_frame = UpperFrame(obj)
        self.transaction_list = ScrollableCardList(self.list_card_type(obj))
        self.balance_frame = BalanceFrame(obj)
        self.bottom_bar = CustomBottomBar()   
        self.text_field = CustomTextField("Nombre", False, False)
        
        super().__init__(
            route="/Period",
            bgcolor="#00021d",
            padding= ft.Padding.only(top=30,left=5,right=5, bottom=10),
            navigation_bar=self.bottom_bar,
            controls=[ft.Column(
                controls=[
                    
                    self.upper_frame,
                    self.transaction_list,
                    self.balance_frame,
                    self.text_field
                    
                ],
                expand=True
             
                )
            ]
        )

    def list_card_type(self, obj):
        if isinstance(obj, Day):
            return [TransactionCard(t) for t in obj.transactions]
        elif isinstance(obj, Week):
            return [GeneralCard(d) for d in obj.days]
        elif isinstance(obj, Month):
            return [GeneralCard(w) for w in obj.weeks]
        else:
            return []
                         
                         
                         
                         
        
        
        