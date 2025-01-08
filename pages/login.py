import flet as ft

class login(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Column(
            controls=[
                ft.Container(
                    height=800,
                    width=350,
                    bgcolor="blue",
                    content=ft.Column(
                        controls=[
                            ft.Text('Welcome to the login'),
                            ft.Container(
                                content=ft.TextButton("Go to Homepage", on_click=lambda _: self.page.go("/"))
                            )
                        ]
                    )
                )
            ]
        )