import flet as ft

class CustomButton(ft.Container):
    def __init__(self, text, on_click = None, **kwargs):
        super().__init__(**kwargs)
        self._on_click_callback = on_click
        self.text = text


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
                ft.Text(self.text, color=self.color_select(), size=14)
            ]
        )

        self.on_click = self.handle_click

    def color_select(self):
        if self.text == "Expense":
            return ft.Colors.RED_ACCENT_400
        else:
            return ft.Colors.GREEN_ACCENT_400

    def handle_click(self, e):
        if self._on_click_callback:
            self._on_click_callback(self.text)  

    def set_active(self, is_active: bool):
        if is_active:
            self.border = ft.Border.all(2, self.color_select())  # borde iluminado
            self.bgcolor = "#2A3F5F"  # fondo más claro
        else:
            self.border = ft.Border.all(1, "#1B263B")  # borde apagado
            self.bgcolor = "#1B263B"  # fondo original
        self.update()


class TypeSelector(ft.Row):
    def __init__(self, on_change=None, **kwargs):
        super().__init__(**kwargs)
        self._on_change = on_change
        self.expense_button = CustomButton("Expense", on_click=self.handle_selection)
        self.income_button = CustomButton("Income", on_click=self.handle_selection)
        self.add(self.expense_button, self.income_button)
class TypeSelector(ft.Row):
    def __init__(self, on_change=None, **kwargs):
        super().__init__(**kwargs)
        self.on_selection_change = on_change
        self.expense_button = CustomButton("Expense", on_click=self.handle_selection)
        self.income_button = CustomButton("Income", on_click=self.handle_selection)
        self.add(self.expense_button, self.income_button)

    def handle_selection(self, selected_type):
        self.expense_button.set_active(selected_type == "Expense")
        self.income_button.set_active(selected_type == "Income")
        if self.on_selection_change:
            self.on_selection_change(selected_type)
    def handle_selection(self, selected_type):
        self.expense_button.set_active(selected_type == "Expense")
        self.income_button.set_active(selected_type == "Income")
        if self._on_change:
            self._on_change(selected_type)
    