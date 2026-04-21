import flet as ft


class CustomTextField(ft.TextField):
    def __init__(
        self,
        label: str,
        value: str = "",
        expand: bool = False,
        on_change: ft.EventHandler = None,
    ):
        super().__init__()
        self.label = label
        self.value = value
        self.expand = expand
        if on_change:
            self.on_change = on_change

        self.bgcolor = ft.Colors.SURFACE
        self.border_color = ft.Colors.ON_SURFACE_VARIANT
