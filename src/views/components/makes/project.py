import flet as ft

from core.module import (
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
    def __init__(self, new_project):
        super().__init__()
        self.new_project = new_project

        self.textfield = CustomTextField(label="新規プロジェクト")
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            ExplainContainer(
                title="プロジェクト一覧",
                body="プロジェクトに作成時の情報を保存しておくことで、追加の変更がしやすくなります。",
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

    def new_clicked(self, _: ft.ControlEventHandler[ft.Button]):
        self.new_project()


class ProjectItem(ft.Column):
    def __init__(self, project_path, update_list, edit_project, delete_project):
        super().__init__()
        self.project_path = project_path
        self.update_list = update_list
        self.edit_project = edit_project
        self.delete_project = delete_project

        self.project_obj = get_project_obj(self.project_path)
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

    def rename_project(self, _):
        self.textfield.value = self.project_path.stem
        self.change_edit_view()
        self.update()

    def save_project(self, _):
        self.project_name.value = self.textfield.value
        self.project_path = rename_project_file(self.project_path, self.textfield.value)
        self.textfield.value = ""
        self.index = self.change_default_view()
        self.update_list()  # update()

    def edit_clicked(self, _):
        self.edit_project(self)

    def delete_clicked(self, _):
        self.delete_project(self)


class ProjectList(ft.Column):
    def __init__(self, edit_project):
        super().__init__()
        self.edit_project = edit_project

        self.expand = True
        self.projects = get_project_files()
        self.new = NewProject(new_project=self.new_project)
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
        if new:
            self.dialog_open(
                icon=ft.Icons.INFO,
                icon_color=ft.Colors.BLUE,
                title="プロジェクトを作成しました",
                content=f"作成したプロジェクト: {self.new.textfield.value}",
                actions=[
                    ft.FilledButton(
                        ft.Text(value="OK", color=ft.Colors.WHITE),
                        bgcolor=ft.Colors.BLUE,
                        on_click=self.dialog_close,
                    )
                ],
            )
        else:
            self.dialog_open(
                icon=ft.Icons.ERROR,
                icon_color=ft.Colors.RED,
                title="エラー",
                content="プロジェクト名を入力してください！",
                actions=[
                    ft.FilledButton(
                        content=ft.Text(value="OK", color=ft.Colors.WHITE),
                        bgcolor=ft.Colors.BLUE,
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
            content=f"削除すると二度と元に戻りません。\n削除するプロジェクト: {item.project_name.value}",
            actions=[
                ft.FilledButton(
                    content=ft.Text(value="No", color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.BLUE,
                    on_click=self.dialog_close,
                ),
                ft.FilledButton(
                    content=ft.Text(value="Delete", color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.RED,
                    on_click=lambda _: self.delete_project(item),
                ),
            ],
        )

    def delete_project(self, item: ProjectItem):
        delete_project_file(item.project_path)
        self.update_project_items()
        self.dialog_close(item)

    def dialog_open(self, icon, icon_color, title, content, actions):
        self.dlg = CustomDialog(
            icon=icon,
            icon_color=icon_color,
            title=title,
            content=content,
            actions=actions,
        )
        self.page.show_dialog(self.dlg)

    def dialog_close(self, _):
        self.page.pop_dialog()
