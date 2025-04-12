import flet as ft
from pathlib import Path
from controls import TitleText, BodyText, ExplainContainer


def home_view():
    return ft.Column(
        controls=[
            ExplainContainer(
                title="Bgm RP Maker v3.0.0",
                body="This is a desktop app that enables you to easily create resource pack that change the BGM of Minecraft.",
            ),
            ft.Image(
                src=Path("images/wp.png"),
                border_radius=ft.border_radius.all(10),
            ),
        ],
    )
