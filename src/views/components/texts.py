import flet as ft


class HeadLineText(ft.Text):
    """Almost h2 tag"""

    def __init__(self, value: str):
        super().__init__()
        self.value = value
        self.theme_style = ft.TextThemeStyle.HEADLINE_MEDIUM


class TitleText(ft.Text):
    """Almost h3 tag"""

    def __init__(self, value: str):
        super().__init__()
        self.value = value
        self.theme_style = ft.TextThemeStyle.TITLE_MEDIUM


class BodyText(ft.Text):
    """Almost p tag"""

    def __init__(self, value: str):
        super().__init__()
        self.value = value
        self.theme_style = ft.TextThemeStyle.BODY_LARGE
