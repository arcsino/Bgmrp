import flet as ft

from .custom_btn import CustomButton


class ShortButton(CustomButton):

    def __init__(
        self,
        height: int | float,
        text: str,
        on_click: ft.ControlEventHandler[ft.Container],
        bgcolor: ft.ColorValue = ft.Colors.PRIMARY_CONTAINER,
    ):
        super().__init__(height, text, on_click)
        self.width = 100
        self.bgcolor = bgcolor
