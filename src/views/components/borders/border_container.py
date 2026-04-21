import flet as ft


class BorderContainer(ft.Container):
    def __init__(self, content: ft.Control):
        super().__init__()
        self.content = content
        self.expand = True
        self.padding = ft.Padding.all(10)
        self.bgcolor = ft.Colors.ON_INVERSE_SURFACE
        self.border = ft.Border.all(width=1, color=ft.Colors.ON_SURFACE_VARIANT)
        self.border_radius = ft.BorderRadius.all(5)
