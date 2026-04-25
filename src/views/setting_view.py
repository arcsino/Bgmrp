import flet as ft

from views.components import ExplainContainer


class SettingView(ft.Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.visible = False
        self.scroll = ft.ScrollMode.AUTO
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            ExplainContainer(
                title="設定",
                body="テーマを切り替えることができます．",
            ),
            ft.Switch(
                label=" ライトテーマ",
                on_change=self.theme_changed,
            ),
        ]

    def theme_changed(self, _: ft.Event[ft.Switch]):
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.page.update()
