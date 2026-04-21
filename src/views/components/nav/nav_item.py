import flet as ft


class NavItem(ft.Container):
    def __init__(
        self,
        label: str,
        icon: ft.IconData,
        on_click: ft.EventHandler,
        bgcolor: ft.ColorValue = ft.Colors.TRANSPARENT,
        icon_color: ft.ColorValue = ft.Colors.PRIMARY,
    ):
        super().__init__()
        self.label = label
        self.icon = ft.Icon(icon=icon, color=icon_color)
        self.on_click = on_click
        self.bgcolor = bgcolor
        self.ink = True
        self.height = 60
        self.padding = ft.Padding.only(left=20, top=10, right=25, bottom=10)
        self.border_radius = ft.BorderRadius.all(5)
        self.content = ft.Row(
            expand=True,
            controls=[
                self.icon,
                ft.Text(
                    value=self.label,
                    text_align=ft.TextAlign.CENTER,
                    theme_style=ft.TextThemeStyle.TITLE_SMALL,
                    expand=True,
                ),
            ],
        )
