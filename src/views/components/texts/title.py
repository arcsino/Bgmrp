import flet as ft


class TitleText(ft.Text):
    """Almost h3 tag"""

    def __init__(self, value: str):
        super().__init__()
        self.value = value
        self.theme_style = ft.TextThemeStyle.TITLE_MEDIUM
