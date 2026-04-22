import flet as ft

from .custom_btn import CustomButton


class CustomIconButton(CustomButton):

    def __init__(
        self,
        height: int | float,
        text: str,
        icon: ft.IconData,
        on_click: ft.ControlEventHandler[ft.Container],
    ):
        super().__init__(height, text, on_click)
        self.text = ft.Text(value=text, theme_style=ft.TextThemeStyle.TITLE_SMALL)
        self.icon = ft.Icon(name=icon, color=ft.Colors.ON_SECONDARY_CONTAINER)
        self.content = ft.Row(controls=[self.icon, self.text])
