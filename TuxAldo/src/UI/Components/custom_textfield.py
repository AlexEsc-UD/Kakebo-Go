import flet as ft

class CustomTextField(ft.TextField):
    # Agregamos 'password' (o el nombre que prefieras) al constructor
    def __init__(self, hiden_text, multiline=False, password=False):
        super().__init__()
        self.hint_text = hiden_text
        self.multiline = multiline
        self.expand = True
        
        # Configuración de estilo
        self.bgcolor = "#00021d"
        self.border_color = "#1B263B"
        self.focused_border_color = "#1B263B"
        self.color = ft.Colors.WHITE    
        self.height = 40
        self.border_radius = 10
        
        # Aplicamos las propiedades a la instancia de Flet
        self.can_reveal_password = password