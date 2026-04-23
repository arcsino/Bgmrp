import flet as ft

from .texts import BodyText, HeadLineText, TitleText


class ExplainContainer(ft.Container):
    def __init__(self, title: str, body: str):
        super().__init__()
        self.content = ft.Column(
            controls=[
                ft.Container(
                    content=HeadLineText(value=title),
                    padding=ft.Padding.all(5),
                    bgcolor=ft.Colors.ON_INVERSE_SURFACE,
                    border_radius=ft.BorderRadius.all(5),
                ),
                BodyText(value=body),
            ],
        )


class SmallExplainContainer(ft.Container):
    def __init__(self, title: str, body: str):
        super().__init__()
        self.content = ft.Column(
            controls=[
                ft.Container(
                    content=TitleText(value=title),
                    padding=ft.Padding.all(5),
                    bgcolor=ft.Colors.ON_INVERSE_SURFACE,
                    border_radius=ft.BorderRadius.all(5),
                ),
                BodyText(value=body),
            ],
        )
