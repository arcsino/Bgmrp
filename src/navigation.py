import flet as ft


class NavigationItem(ft.Container):
    def __init__(self, label, icon, on_click, bgcolor=ft.Colors.TRANSPARENT):
        super().__init__()
        self.content = ft.Row(controls=[ft.Icon(name=icon), ft.Text(value=label)])
        self.padding = 20
        self.bgcolor = bgcolor
        self.border_radius = 10
        self.ink = True
        self.on_click = on_click
