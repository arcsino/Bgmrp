import flet as ft
from pathlib import Path

from controls import BorderImage, ExplainContainer, BodyText


class HomeView(ft.Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            ExplainContainer(
                title="Bgmrp v1.0.2",
                body="MinecraftにBGMを追加するリソースパックを簡単に作れるデスクトップアプリです。",
            ),
            BodyText(value="※Java版限定です。"),
            BorderImage(src=Path("images/wp.png")),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
        ]
