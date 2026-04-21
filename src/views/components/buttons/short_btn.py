import flet as ft

from views.components import CustomButton


class ShortButton(CustomButton):
    def __init__(
        self,
        height: int | float,
        text: str,
        on_click: ft.EventHandler,
        bgcolor: ft.Colors = None,
    ):
        super().__init__(height, text, on_click)
        self.width = 100
        if bgcolor:
            self.bgcolor = bgcolor
        else:
            self.bgcolor = ft.Colors.PRIMARY_CONTAINER
