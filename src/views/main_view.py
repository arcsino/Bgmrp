import flet as ft

from views import HelpView, HomeView, MakeView, SettingView
from views.components import Navbar


class MainView(ft.Row):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.navbar = Navbar(nav_item_on_click=self.item_clicked)
        self.views: list[ft.Column] = [
            HomeView(),
            MakeView(),
            HelpView(),
            SettingView(),
        ]
        self.controls = [
            self.navbar,
            ft.VerticalDivider(width=5),
            ft.Column(
                controls=self.views,
                expand=True,
            ),
        ]

    def item_clicked(self, index: int):
        """when NavItem() is clicked"""
        for view in self.views:
            view.visible = False
        self.views[index].visible = True
        self.update()
        self.update()
