import flet as ft


# Main compount
class TextEditor(ft.UserControl):
    def __init__(self) -> None:
        super().__init__()
        self.textfield = ft.TextField(
            multiline=True,
            autofocus=True,
            border=ft.InputBorder.NONE,
            on_change=self.save_text,
            content_padding=30,
            cursor_color="blue",
        )

    # Save Function -> it saves the data from the save.txt file
    def save_text(self, e: ft.ControlEvent) -> None:
        with open("save.txt", "w") as f:
            f.write(self.textfield.value)

    # Read Function -> it read the saved data from the save.txt file
    def read_text(self) -> None | str:
        # if save.txt file exists then open file and read its data
        try:
            with open("save.txt", "r") as f:
                return f.read()

        # Else return some text
        except FileNotFoundError:
            self.textfield.hint_text = "Type here...."

    # Build function
    def build(self) -> ft.TextField:
        self.textfield.value = self.read_text()
        return self.textfield


def main(page: ft.Page) -> None:
    page.title = "XOR Editor"
    page.scroll = True

    page.add(TextEditor())


if __name__ == "__main__":
    ft.app(target=main)
