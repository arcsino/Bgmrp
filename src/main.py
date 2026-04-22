import flet as ft

from views.main_view import MainView


def main(page: ft.Page):
    page.title = "Bgmrp"
    page.window.width = 720
    page.window.height = 480
    page.window.resizable = False
    page.window.maximizable = False
    page.theme_mode = ft.ThemeMode.DARK
    page.add(MainView())


ft.run(main)
ft.run(main)
ft.run(main)
ft.run(main)
