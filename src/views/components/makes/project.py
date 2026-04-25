from pathlib import Path

import flet as ft

from core.module import (
    ProjectInfo,
    delete_project_file,
    get_icon_image,
    get_project_files,
    get_project_obj,
    new_project_file,
    rename_project_file,
)
from views.components import (
    BorderContainer,
    CustomDialog,
    CustomTextField,
    ExplainContainer,
    TitleText,
)


class NewProject(ft.Column):
    def __init__(self, new_project: ft.Event):
        super().__init__()
        self.new_project = new_project
        self.textfield = CustomTextField(label="新規プロジェクト")
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            ExplainContainer(
                title="プロジェクト一覧",
                body="プロジェクトに作成時の情報を保存しておくことで，追加の変更がしやすくなります．",
            ),
            ft.Row(
                controls=[
                    self.textfield,
                    ft.IconButton(
                        icon=ft.Icons.ADD,
                        icon_color=ft.Colors.ON_PRIMARY_CONTAINER,
                        on_click=self.new_clicked,
                    ),
                ]
            ),
            ft.Divider(height=5),
        ]

    def new_clicked(self, _: ft.Event[ft.Button]):
        self.new_project()


class ProjectItem(ft.Column):

    def __init__(
        self,
        project_path: Path,
        update_list: ft.Event,
        edit_project: ft.Event,
        delete_project: ft.Event,
    ):
        super().__init__()
        self.project_path: Path = project_path
        self.update_list = update_list
        self.edit_project = edit_project
        self.delete_project = delete_project
        self.project_obj: ProjectInfo = get_project_obj(self.project_path)
        self.project_name = TitleText(value=self.project_path.stem)
        self.textfield = CustomTextField(label="変更後のプロジェクト名")
        self.change_default_view()

    def change_default_view(self):
        self.controls = [
            BorderContainer(
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row(
                            expand=True,
                            controls=[
                                ft.Image(
                                    src=get_icon_image(self.project_obj.icon),
                                    border_radius=ft.BorderRadius.all(5),
                                    width=50,
                                ),
                                self.project_name,
                            ],
                        ),
                        ft.PopupMenuButton(
                            icon_color=ft.Colors.ON_PRIMARY_CONTAINER,
                            items=[
                                ft.PopupMenuItem(
                                    content="名称変更",
                                    icon=ft.Icons.EDIT,
                                    on_click=self.rename_project,
                                ),
                                ft.PopupMenuItem(
                                    content="編集",
                                    icon=ft.Icons.TUNE,
                                    on_click=self.edit_clicked,
                                ),
                                ft.PopupMenuItem(
                                    content="削除",
                                    icon=ft.Icons.DELETE,
                                    on_click=self.delete_clicked,
                                ),
                            ],
                        ),
                    ],
                ),
            )
        ]

    def change_edit_view(self):
        self.controls = [
            BorderContainer(
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        self.textfield,
                        ft.IconButton(
                            icon=ft.Icons.CHECK,
                            icon_color=ft.Colors.ON_PRIMARY_CONTAINER,
                            on_click=self.save_project,
                        ),
                    ],
                ),
            )
        ]

    def rename_project(self, _: ft.Event[ft.PopupMenuItem]):
        self.textfield.value = self.project_path.stem
        self.change_edit_view()
        self.update()

    def save_project(self, _: ft.Event[ft.IconButton]):
        renamed = rename_project_file(self.project_path, self.textfield.value)
        if isinstance(renamed, Exception):
            self.dialog_open(
                icon=ft.Icons.CANCEL,
                icon_color=ft.Colors.RED,
                title=str(renamed),
                content=f"入力されたプロジェクト名: {self.textfield.value.strip()}",
                actions=[
                    ft.FilledButton(
                        content=ft.Text(value="閉じる", color=ft.Colors.ON_SURFACE),
                        bgcolor=ft.Colors.PRIMARY_CONTAINER,
                        on_click=self.dialog_close,
                    )
                ],
            )
            return
        else:
            self.dialog_open(
                icon=ft.Icons.INFO,
                icon_color=ft.Colors.BLUE,
                title="プロジェクト名を変更しました！",
                content=f"変更後のプロジェクト名: {self.textfield.value.strip()}",
                actions=[
                    ft.FilledButton(
                        content=ft.Text(value="閉じる", color=ft.Colors.ON_SURFACE),
                        bgcolor=ft.Colors.PRIMARY_CONTAINER,
                        on_click=self.dialog_close,
                    )
                ],
            )
        self.project_name.value = renamed.stem
        self.project_path = renamed
        self.textfield.value = ""
        self.change_default_view()
        self.update_list()  # update()

    def edit_clicked(self, _: ft.Event[ft.PopupMenuItem]):
        self.edit_project(self)

    def delete_clicked(self, _: ft.Event[ft.PopupMenuItem]):
        self.delete_project(self)

    def dialog_open(
        self,
        icon: ft.IconData,
        icon_color: ft.ColorValue,
        title: str,
        content: str,
        actions: list[ft.FilledButton],
    ):
        self.dlg = CustomDialog(
            icon=icon,
            icon_color=icon_color,
            title=title,
            content=content,
            actions=actions,
        )
        self.page.show_dialog(self.dlg)

    def dialog_close(self, _: ft.Event[ft.FilledButton]):
        self.page.pop_dialog()


class ProjectList(ft.Column):
    def __init__(self, edit_project: ft.Event):
        super().__init__()
        self.edit_project = edit_project

        self.expand = True
        self.projects = get_project_files()
        self.new = NewProject(self.new_project)
        self.project_items = ft.Column(expand=True, scroll=ft.ScrollMode.AUTO)
        self.controls = [self.new, self.project_items]
        self.project_items.controls = [
            ProjectItem(
                project_path=project,
                update_list=self.update_project_items,
                edit_project=self.edit_project,
                delete_project=self.confilm_delete_project,
            )
            for project in self.projects
        ]

    def update_project_items(self):
        self.projects = get_project_files()
        self.project_items.controls = [
            ProjectItem(
                project_path=project,
                update_list=self.update_project_items,
                edit_project=self.edit_project,
                delete_project=self.confilm_delete_project,
            )
            for project in self.projects
        ]
        self.update()

    def new_project(self):
        new = new_project_file(self.new.textfield.value)
        if isinstance(new, Exception):
            self.dialog_open(
                icon=ft.Icons.CANCEL,
                icon_color=ft.Colors.RED,
                title=str(new),
                content=f"入力されたプロジェクト名: {self.new.textfield.value.strip()}",
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
                icon=ft.Icons.CHECK_CIRCLE,
                icon_color=ft.Colors.BLUE,
                title="プロジェクトを作成しました",
                content=f"作成したプロジェクト: {self.new.textfield.value.strip()}",
                actions=[
                    ft.FilledButton(
                        ft.Text(value="閉じる", color=ft.Colors.ON_SURFACE),
                        bgcolor=ft.Colors.PRIMARY_CONTAINER,
                        on_click=self.dialog_close,
                    )
                ],
            )
        self.new.textfield.value = ""
        self.update_project_items()

    def confilm_delete_project(self, item: ProjectItem):
        self.dialog_open(
            icon=ft.Icons.WARNING,
            icon_color=ft.Colors.AMBER,
            title="本当に削除しますか？",
            content=f"削除すると二度と元に戻りません．\n削除するプロジェクト: {item.project_name.value}",
            actions=[
                ft.FilledButton(
                    content=ft.Text(value="いいえ", color=ft.Colors.ON_SURFACE),
                    bgcolor=ft.Colors.PRIMARY_CONTAINER,
                    on_click=self.dialog_close,
                ),
                ft.FilledButton(
                    content=ft.Text(value="削除する", color=ft.Colors.ON_SURFACE),
                    bgcolor=ft.Colors.ERROR_CONTAINER,
                    on_click=lambda _: self.delete_project(item),
                ),
            ],
        )

    def delete_project(self, item: ProjectItem):
        delete_project_file(item.project_path)
        self.update_project_items()
        self.dialog_close(item)

    def dialog_open(
        self,
        icon: ft.IconData,
        icon_color: ft.ColorValue,
        title: str,
        content: str,
        actions: list[ft.FilledButton],
    ):
        self.dlg = CustomDialog(
            icon=icon,
            icon_color=icon_color,
            title=title,
            content=content,
            actions=actions,
        )
        self.page.show_dialog(self.dlg)

    def dialog_close(self, _: ft.Event[ft.FilledButton]):
        self.page.pop_dialog()
