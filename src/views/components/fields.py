import flet as ft


class CustomTextField(ft.TextField):
    def __init__(
        self,
        label: str,
        value: str = "",
        expand: bool = False,
        on_change: ft.ControlEventHandler[ft.TextField] | None = None,
    ):
        super().__init__()
        self.label = label
        self.value = value
        self.expand = expand
        self.bgcolor = ft.Colors.SURFACE
        self.border_color = ft.Colors.ON_SURFACE_VARIANT
        if on_change:
            self.on_change = on_change


class MultiLineTextField(ft.TextField):
    def __init__(
        self,
        label: str,
        value: str = "",
        expand: bool = False,
        on_change: ft.ControlEventHandler[ft.TextField] | None = None,
    ):
        super().__init__()
        self.label = label
        self.value = value
        self.expand = expand
        self.min_lines = 1
        self.max_lines = 9
        self.multiline = True
        self.bgcolor = ft.Colors.SURFACE
        self.border_color = ft.Colors.ON_SURFACE_VARIANT
        if on_change:
            self.on_change = on_change
