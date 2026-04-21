import flet as ft


class CustomButton(ft.Container):
    def __init__(
        self,
        height: int | float,
        text: str,
        on_click: ft.EventHandler,
        bgcolor: ft.Colors = None,
    ):
        super().__init__()
        self.height = height
        self.on_click = on_click
        if bgcolor:
            self.bgcolor = bgcolor
        else:
            self.bgcolor = ft.Colors.PRIMARY_CONTAINER

        self.ink = True
        self.expand = False
        self.alignment = ft.MainAxisAlignment.CENTER
        self.border_radius = ft.BorderRadius.all(5)
        self.padding = ft.Padding.only(left=10, right=10)
        self.content = ft.Text(value=text, theme_style=ft.TextThemeStyle.TITLE_SMALL)
