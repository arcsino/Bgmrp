from pathlib import Path

import flet as ft

from views.components import BorderContainer


class BorderImage(BorderContainer):
    def __init__(self, src: Path):
        self.src = src
        self.content = ft.Image(
            src=src,
            border_radius=ft.BorderRadius.all(10),
            width=565,
            fit=ft.BoxFit.COVER,
        )
        super().__init__(content=self.content)
