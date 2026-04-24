import flet as ft

from views.components import EditProject, ProjectItem, ProjectList


class MakeView(ft.Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.visible = False
        self.controls = [ProjectList(self.handle_edit_project)]

    def handle_project_list(self):
        """when IconButton() in EditHeader() is clicked"""
        self.controls = [ProjectList(self.handle_edit_project)]
        self.update()

    def handle_edit_project(self, item: ProjectItem):
        """when PopupMenuButton() in ProjectItem() is clicked"""
        self.controls = [
            EditProject(
                project_path=item.project_path,
                back_clicking=self.handle_project_list,
            )
        ]
        self.update()
