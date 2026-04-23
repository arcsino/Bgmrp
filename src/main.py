import os

import flet as ft

from core.module import init_storage_path
from views.main_view import MainView


def main(page: ft.Page):
    page.title = "Bgmrp"
    page.window.width = 720
    page.window.height = 480
    page.window.resizable = False
    page.window.maximizable = False
    page.theme_mode = ft.ThemeMode.DARK
    init_storage_path(os.getenv("FLET_APP_STORAGE_DATA"))
    page.add(MainView())


ft.run(main)
