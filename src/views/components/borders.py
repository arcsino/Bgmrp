from pathlib import Path

import flet as ft


class BorderContainer(ft.Container):
    def __init__(self, content: ft.Control):
        super().__init__()
        self.content = content
        self.expand = True
        self.padding = ft.Padding.all(10)
        self.bgcolor = ft.Colors.ON_INVERSE_SURFACE
        self.border = ft.Border.all(width=1, color=ft.Colors.ON_SURFACE_VARIANT)
        self.border_radius = ft.BorderRadius.all(5)


class BorderImage(BorderContainer):
    def __init__(self, src: Path | str):
        self.src = Path(src) if isinstance(src, str) else src
        self.content = ft.Image(
            src=str(self.src),
            border_radius=ft.BorderRadius.all(10),
            width=500,
            fit=ft.BoxFit.COVER,
        )
        super().__init__(content=self.content)
        super().__init__(content=self.content)
