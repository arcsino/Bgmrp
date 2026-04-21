import flet as ft


class HeadLineText(ft.Text):
    """Almost h2 tag"""

    def __init__(self, value: str):
        super().__init__()
        self.value = value
        self.theme_style = ft.TextThemeStyle.HEADLINE_MEDIUM
