import asyncio
from pathlib import Path

import flet as ft

from core.module import (
    ProjectInfo,
    check_entry,
    get_project_obj,
    make_rp,
    write_project_info,
)
from views.components import CustomDialog

from .tabs import DescriptionTab, IconTab, NameTab, SoundsTab, VersionTab, VolumeTab


class EditHeader(ft.Row):
    def __init__(
        self,
        project_title: str,
        back_click: ft.Event,
        save_click: ft.Event,
        next_click: ft.Event,
    ):
        super().__init__()
        self.project_title = ft.Text(
            value=(
                project_title
                if len(project_title) <= 24
                else project_title[:24] + "..."
            ),
            expand=True,
            text_align=ft.TextAlign.CENTER,
            theme_style=ft.TextThemeStyle.TITLE_LARGE,
        )
        self.back_click = back_click
        self.save_click = save_click
        self.next_click = next_click

        self.controls = [
            ft.Container(
                height=40,
                expand=True,
                bgcolor=ft.Colors.ON_INVERSE_SURFACE,
                border_radius=ft.BorderRadius.all(5),
                content=ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            icon_color=ft.Colors.ON_PRIMARY_CONTAINER,
                            on_click=self.back_clicked,
                        ),
                        self.project_title,
                        ft.IconButton(
                            icon=ft.Icons.SAVE,
                            icon_color=ft.Colors.ON_PRIMARY_CONTAINER,
                            on_click=self.save_clicked,
                        ),
                    ],
                ),
            ),
            ft.FilledButton(
                ft.Text(value="作成する", color=ft.Colors.ON_SURFACE),
                bgcolor=ft.Colors.PRIMARY_CONTAINER,
                icon=ft.Icons.FOLDER_ZIP,
                icon_color=ft.Colors.ON_PRIMARY_CONTAINER,
                on_click=self.next_clicked,
            ),
        ]

    def back_clicked(self, _: ft.Event[ft.IconButton]):
        self.back_click()

    def save_clicked(self, _: ft.Event[ft.IconButton]):
        self.save_click()

    def next_clicked(self, _: ft.Event[ft.Container]):
        self.next_click()


class EditTabs(ft.Tabs):
    def __init__(self, project_obj: ProjectInfo):
        self.project_obj = project_obj
        self.name_tab = NameTab(name=self.project_obj.name)
        self.description_tab = DescriptionTab(description=self.project_obj.description)
        self.icon_tab = IconTab(icon=self.project_obj.icon)
        self.sounds_tab = SoundsTab(sounds=self.project_obj.sounds)
        self.volume_tab = VolumeTab(volume=self.project_obj.volume)
        self.version_tab = VersionTab(version=self.project_obj.version)
        tabs = [
            ft.Tab(label="名前", icon=ft.Icons.SELL),
            ft.Tab(label="説明", icon=ft.Icons.ARTICLE),
            ft.Tab(label="アイコン", icon=ft.Icons.IMAGE),
            ft.Tab(label="BGM", icon=ft.Icons.AUDIO_FILE),
            ft.Tab(label="音量", icon=ft.Icons.VOLUME_UP),
            ft.Tab(label="バージョン", icon=ft.Icons.NUMBERS),
        ]
        tab_views = [
            self.name_tab,
            self.description_tab,
            self.icon_tab,
            self.sounds_tab,
            self.volume_tab,
            self.version_tab,
        ]
        super().__init__(
            length=len(tabs),
            selected_index=0,
            animation_duration=0,
            expand=True,
            content=ft.Column(
                expand=True,
                controls=[
                    ft.TabBar(
                        tabs=tabs,
                        scrollable=False,
                        tab_alignment=ft.TabAlignment.FILL,
                    ),
                    ft.TabBarView(
                        expand=True,
                        controls=tab_views,
                    ),
                ],
            ),
        )


class EditProject(ft.Column):
    def __init__(self, project_path: Path, back_clicking: ft.Event):
        super().__init__()
        self.project_path = project_path
        self.back_clicking = back_clicking

        self.expand = True
        self.file_picker = ft.FilePicker()
        self.header = EditHeader(
            project_title=self.project_path.stem,
            back_click=self.back_click,
            save_click=self.save_project_with_dlg,
            next_click=self.next_click,
        )
        self.tabs = EditTabs(project_obj=get_project_obj(self.project_path))
        self.controls = [self.header, self.tabs]

    def get_edited_project_obj(self):
        return ProjectInfo(
            name=self.tabs.name_tab.name,
            description=self.tabs.description_tab.description,
            icon=self.tabs.icon_tab.icon,
            sounds=self.tabs.sounds_tab.sounds,
            volume=self.tabs.volume_tab.volume,
            version=self.tabs.version_tab.version,
        )

    def back_click(self):
        if not get_project_obj(self.project_path) == self.get_edited_project_obj():
            self.dialog_open(
                icon=ft.Icons.WARNING,
                icon_color=ft.Colors.AMBER,
                title="変更を保存してません！",
                content="保存してプロジェクト一覧へ戻りますか？",
                actions=[
                    ft.FilledButton(
                        content=ft.Text(value="保存する", color=ft.Colors.ON_SURFACE),
                        bgcolor=ft.Colors.PRIMARY_CONTAINER,
                        on_click=lambda e: self.handle_back_dialog(e, save=True),
                    ),
                    ft.FilledButton(
                        content=ft.Text(value="保存しない", color=ft.Colors.ON_SURFACE),
                        bgcolor=ft.Colors.ERROR_CONTAINER,
                        on_click=lambda e: self.handle_back_dialog(e, save=False),
                    ),
                ],
            )
        else:
            self.back_clicking()

    def save_project(self):
        project_obj = self.get_edited_project_obj()
        write_project_info(self.project_path, project_obj)

    def save_project_with_dlg(self):
        self.save_project()
        self.dialog_open(
            icon=ft.Icons.INFO,
            icon_color=ft.Colors.BLUE,
            title="プロジェクトを保存しました！",
            content=f"{self.project_path}を削除すると，データが消えます．",
            actions=[
                ft.FilledButton(
                    content=ft.Text(value="閉じる", color=ft.Colors.ON_SURFACE),
                    bgcolor=ft.Colors.PRIMARY_CONTAINER,
                    on_click=self.dialog_close,
                )
            ],
        )

    def next_click(self):
        self.save_project()
        project_obj = get_project_obj(self.project_path)
        check = check_entry(project_obj)
        if not check:  # if not error
            self.page.run_task(self.pick_directory_and_make_rp, project_obj)
        else:
            self.dialog_open(
                icon=ft.Icons.CANCEL,
                icon_color=ft.Colors.RED,
                title="エラー",
                content=str(check),
                actions=[
                    ft.FilledButton(
                        content=ft.Text(value="閉じる", color=ft.Colors.ON_SURFACE),
                        bgcolor=ft.Colors.PRIMARY_CONTAINER,
                        on_click=self.dialog_close,
                    )
                ],
            )

    async def pick_directory_and_make_rp(self, project_obj: ProjectInfo):
        directory_path = await self.file_picker.get_directory_path(
            dialog_title="リソースパックの保存先フォルダ",
            initial_directory=str(Path.cwd()),
        )
        if directory_path:
            rp_path = Path(directory_path) / f"{project_obj.name}.zip"
            self.dialog_open(
                icon=ft.Icons.HOURGLASS_TOP,
                icon_color=ft.Colors.ORANGE,
                title="リソースパックを作成中...",
                content="オーディオファイルの数やサイズによっては，時間がかかる場合があります．",
                actions=[],
            )
            await asyncio.sleep(0)
            making = await asyncio.to_thread(make_rp, rp_path, project_obj)
            self.dialog_close()
            if not making:  # if not error
                self.dialog_open(
                    icon=ft.Icons.CHECK_CIRCLE,
                    icon_color=ft.Colors.GREEN,
                    title="リソースパックを作成しました",
                    content=str(rp_path),
                    actions=[
                        ft.FilledButton(
                            content=ft.Text(value="閉じる", color=ft.Colors.ON_SURFACE),
                            bgcolor=ft.Colors.PRIMARY_CONTAINER,
                            on_click=self.dialog_close,
                        )
                    ],
                )
            else:
                self.dialog_open(
                    icon=ft.Icons.CANCEL,
                    icon_color=ft.Colors.RED,
                    title="作成に失敗しました",
                    content=str(making),
                    actions=[
                        ft.FilledButton(
                            content=ft.Text(value="閉じる", color=ft.Colors.ON_SURFACE),
                            bgcolor=ft.Colors.PRIMARY_CONTAINER,
                            on_click=self.dialog_close,
                        )
                    ],
                )

    def dialog_open(self, icon, icon_color, title, content, actions):
        self.dlg = CustomDialog(
            icon=icon,
            icon_color=icon_color,
            title=title,
            content=content,
            actions=actions,
        )
        self.page.show_dialog(self.dlg)

    def dialog_close(self, _: ft.Event | None = None):
        self.page.pop_dialog()

    def handle_back_dialog(self, _: ft.Event[ft.FilledButton], save: bool):
        if save:
            self.save_project()
        self.page.pop_dialog()
        self.back_clicking()
