from pathlib import Path

import flet as ft

from views.components import (
    BodyText,
    BorderImage,
    ExplainContainer,
    SmallExplainContainer,
)


class HomeView(ft.Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            ExplainContainer(
                title="Bgmrp v1.0.3",
                body="MinecraftにBGMを追加するリソースパックを簡単に作れるデスクトップアプリです。",
            ),
            BodyText(value="※Java版限定です。"),
            BorderImage(src=Path("images/wp.png")),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            SmallExplainContainer(
                title="変更ログ",
                body="・",
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
        ]
