from pathlib import Path

import flet as ft

from core.module import get_format_version, get_icon_image
from views.components import (
    BodyText,
    BorderContainer,
    CustomTextField,
    MultiLineTextField,
)


class NameTab(ft.Column):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.textfield = CustomTextField(
            label="リソースパック名",
            value=self.name,
            expand=True,
            on_change=self.changed_value,
        )
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            BodyText(value="リソースパックの名前を入力してください．"),
            ft.Row(
                controls=[
                    self.textfield,
                    ft.VerticalDivider(width=1, color=ft.Colors.TRANSPARENT),  # margin
                ]
            ),
        ]

    def changed_value(self, _: ft.Event[ft.TextField]):
        self.name = self.textfield.value


class DescriptionTab(ft.Column):
    def __init__(self, description):
        super().__init__()
        self.description = description

        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.textfield = MultiLineTextField(
            label="リソースパックの説明",
            value=self.description,
            expand=True,
            on_change=self.changed_value,
        )
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            BodyText(value="リソースパックの説明を入力してください．"),
            ft.Row(
                controls=[
                    self.textfield,
                    ft.VerticalDivider(width=1, color=ft.Colors.TRANSPARENT),  # margin
                ]
            ),
        ]

    def changed_value(self, _: ft.Event[ft.TextField]):
        self.description = self.textfield.value


class IconTab(ft.Column):
    def __init__(self, icon):
        super().__init__()
        self.icon = icon
        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.file_picker = ft.FilePicker()
        self.input_controls()

    def input_controls(self):
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            BodyText(
                value="リソースパックのアイコンを選択してください．画像ファイルはPNG形式です．"
            ),
            ft.Row(
                controls=[
                    BorderContainer(
                        content=ft.Row(
                            controls=[
                                ft.Image(
                                    src=get_icon_image(self.icon),
                                    border_radius=ft.BorderRadius.all(5),
                                    width=50,
                                ),
                                ft.Container(
                                    expand=True,
                                    content=BodyText(
                                        value=(
                                            self.icon
                                            if self.icon
                                            else "画像を選択してください．"
                                        )
                                    ),
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.ADD_PHOTO_ALTERNATE_OUTLINED,
                                    icon_color=ft.Colors.ON_PRIMARY_CONTAINER,
                                    on_click=self.pick_files,
                                ),
                            ],
                        )
                    ),
                    ft.VerticalDivider(width=1, color=ft.Colors.TRANSPARENT),  # margin
                ]
            ),
        ]

    async def pick_files(self, _: ft.Event):
        icon = await self.file_picker.pick_files(
            dialog_title="画像を選択",
            initial_directory=str(Path.cwd()),
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["png", "PNG"],
            allow_multiple=False,
        )
        if icon and icon[0].path:
            self.icon = icon[0].path
        self.input_controls()
        self.update()


class SoundsTab(ft.Column):
    def __init__(self, sounds: list):
        super().__init__()
        self.sounds = sounds
        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.file_picker = ft.FilePicker()
        self.input_controls()

    def input_controls(self):
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            BodyText(
                value="追加するBGMを選択してください．オーディオファイルはOGG形式です．"
            ),
            ft.Row(
                controls=[
                    ft.Icon(icon=ft.Icons.AUDIO_FILE),
                    ft.Container(
                        expand=True,
                        content=BodyText(
                            value=(
                                f"{len(self.sounds)} 件の音源"
                                if self.sounds
                                else "音源を追加してください．"
                            )
                        ),
                    ),
                    ft.IconButton(
                        icon=ft.Icons.UPLOAD_FILE,
                        icon_color=ft.Colors.ON_PRIMARY_CONTAINER,
                        on_click=self.pick_files,
                    ),
                    ft.VerticalDivider(width=1, color=ft.Colors.TRANSPARENT),  # margin
                ],
            ),
            ft.Column(
                expand=True,
                controls=[
                    self.get_sound_item(path, index)
                    for index, path in enumerate(self.sounds)
                ],
            ),
        ]

    def get_sound_item(self, path, index):
        return BorderContainer(
            content=ft.Row(
                controls=[
                    ft.Icon(icon=ft.Icons.AUDIO_FILE),
                    ft.Container(expand=True, content=BodyText(value=path)),
                    ft.IconButton(
                        icon=ft.Icons.CLOSE,
                        icon_color=ft.Colors.ON_PRIMARY_CONTAINER,
                        on_click=lambda _: self.delete_sound(index),
                    ),
                ],
            )
        )

    async def pick_files(self, _: ft.Event):
        picked = await self.file_picker.pick_files(
            dialog_title="音声ファイルを選択",
            initial_directory=str(Path.cwd()),
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["ogg", "OGG"],
            allow_multiple=True,
        )
        if picked:
            for f in picked:
                if f.path and f.path not in self.sounds:
                    self.sounds.append(f.path)
            self.sounds.sort()
        self.input_controls()
        self.update()

    def delete_sound(self, index):
        self.sounds.remove(self.sounds[index])
        self.input_controls()
        self.update()


class VolumeTab(ft.Column):
    def __init__(self, volume):
        super().__init__()
        self.volume = volume

        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.slider = ft.Slider(
            value=self.volume,
            min=0,
            max=100,
            divisions=10,
            label="{value}%",
            on_change=self.changed_value,
        )
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            BodyText(value="BGMの音量を設定してください．"),
            self.slider,
        ]

    def changed_value(self, _):
        self.volume = self.slider.value


class VersionTab(ft.Column):
    def __init__(self, version):
        super().__init__()
        self.version = version

        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.format = get_format_version()
        self.options = [
            ft.DropdownOption(key=key, content=BodyText(value=key))
            for key in self.format.keys()
        ]
        self.dropdown = ft.Dropdown(
            value=self.version,
            options=self.options,
            menu_height=400,
            border_color=ft.Colors.ON_SURFACE_VARIANT,
            on_select=self.changed_option,
        )
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            BodyText(value="マイクラのバージョンを設定してください．"),
            self.dropdown,
        ]

    def changed_option(self, e: ft.ControlEvent):
        self.version = e.data
