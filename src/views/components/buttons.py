import flet as ft


class CustomButton(ft.Container):

    def __init__(
        self,
        height: int | float,
        text: str,
        on_click: ft.ControlEventHandler[ft.Container],
        bgcolor: ft.ColorValue = ft.Colors.PRIMARY_CONTAINER,
    ):
        super().__init__()
        self.height = height
        self.on_click = on_click
        self.bgcolor = bgcolor
        self.ink = True
        self.expand = False
        self.alignment = ft.MainAxisAlignment.CENTER
        self.border_radius = ft.BorderRadius.all(5)
        self.padding = ft.Padding.only(left=10, right=10)
        self.content = ft.Text(value=text, theme_style=ft.TextThemeStyle.TITLE_SMALL)


class CustomIconButton(CustomButton):

    def __init__(
        self,
        height: int | float,
        text: str,
        icon: ft.IconData,
        on_click: ft.ControlEventHandler[ft.Container],
    ):
        super().__init__(height, text, on_click)
        self.text = ft.Text(value=text, theme_style=ft.TextThemeStyle.TITLE_SMALL)
        self.icon = ft.Icon(name=icon, color=ft.Colors.ON_SECONDARY_CONTAINER)
        self.content = ft.Row(controls=[self.icon, self.text])


class ShortButton(CustomButton):
    def __init__(
        self,
        height: int | float,
        text: str,
        on_click: ft.ControlEventHandler,
        bgcolor: ft.ColorValue = None,
    ):
        super().__init__(height, text, on_click)
        self.width = 100
        if bgcolor:
            self.bgcolor = bgcolor
        else:
            self.bgcolor = ft.Colors.PRIMARY_CONTAINER
