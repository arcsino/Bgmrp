import flet as ft


class CustomDialog(ft.AlertDialog):
    def __init__(
        self,
        icon: ft.IconData,
        icon_color: ft.ColorValue,
        title: str,
        content: str,
        actions: list[ft.FilledButton],
    ):
        super().__init__()
        self.icon = ft.Icon(icon, color=icon_color)
        self.title = ft.Text(value=title, text_align=ft.TextAlign.CENTER)
        self.content = ft.Text(value=content, text_align=ft.TextAlign.CENTER)
        self.actions = actions
        self.modal = True
        self.shape = ft.RoundedRectangleBorder(radius=10)
        self.actions_alignment = ft.MainAxisAlignment.CENTER
