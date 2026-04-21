import flet as ft


class BodyText(ft.Text):
    """Almost p tag"""

    def __init__(self, value: str):
        super().__init__()
        self.value = value
        self.theme_style = ft.TextThemeStyle.BODY_LARGE
