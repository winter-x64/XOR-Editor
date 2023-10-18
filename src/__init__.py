import flet as ft
from .components.texteditor import TextEditor


def main(page: ft.Page) -> None:
    page.title = "XOR Editor"
    page.scroll = True

    page.add(TextEditor())
