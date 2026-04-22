from pathlib import Path

import flet as ft

from .border_container import BorderContainer


class BorderImage(BorderContainer):
    def __init__(self, src: Path | str):
        self.src = Path(src) if isinstance(src, str) else src
        self.content = ft.Image(
            src=str(self.src),
            border_radius=ft.BorderRadius.all(10),
            width=565,
            fit=ft.BoxFit.COVER,
        )
        super().__init__(content=self.content)
