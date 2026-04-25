from pathlib import Path

import flet as ft

from views.components import SmallExplainContainer


class HomeView(ft.Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.controls = [
            ft.Container(
                content=ft.Image(
                    src=str(Path("wp.png")),
                    border_radius=ft.BorderRadius.all(10),
                    fit=ft.BoxFit.COVER,
                )
            ),
            SmallExplainContainer(
                title="v1.1.0 変更ログ",
                body="\n".join(
                    [
                        "・ライブラリの更新 (flet-v0.27.6 -> flet-v0.82.2)",
                        "・MCバージョン26.1-26.1.xに対応",
                        "・UI及びヘルプの説明文を改善",
                        "・軽微な不具合の修正",
                    ]
                ),
            ),
        ]
