import flet as ft

from .nav_item import NavItem


class Navbar(ft.Column):

    def __init__(self, nav_item_on_click: ft.Event):
        super().__init__()
        self.nav_item_on_click = nav_item_on_click
        self.width = 120
        self.controls: list[NavItem] = [
            NavItem(
                label="ホーム",
                icon=ft.Icons.HOME,
                bgcolor=ft.Colors.PRIMARY_CONTAINER,
                icon_color=ft.Colors.ON_PRIMARY_CONTAINER,
                on_click=lambda _: self.on_clicked(0),
            ),
            NavItem(
                label="作成",
                icon=ft.Icons.CREATE_NEW_FOLDER,
                on_click=lambda _: self.on_clicked(1),
            ),
            NavItem(
                label="ヘルプ",
                icon=ft.Icons.HELP,
                on_click=lambda _: self.on_clicked(2),
            ),
            NavItem(
                label="設定",
                icon=ft.Icons.SETTINGS,
                on_click=lambda _: self.on_clicked(3),
            ),
        ]

    def on_clicked(self, index: int):
        for nav in self.controls:
            nav.bgcolor = ft.Colors.TRANSPARENT
            nav.icon.color = ft.Colors.PRIMARY
        self.controls[index].bgcolor = ft.Colors.PRIMARY_CONTAINER
        self.controls[index].icon.color = ft.Colors.ON_PRIMARY_CONTAINER
        self.nav_item_on_click(index)
        self.nav_item_on_click(index)
