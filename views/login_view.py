from flet import *

class login(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return Column(
            controls=[
                Container(
                    height=800,
                    width=350,
                    bgcolor="blue",
                    content=Column(
                        controls=[
                            Text('Welcome to the login'),
                            Container(
                                content=TextButton("Go to Homepage", on_click=lambda _: self.page.go("/"))
                            )
                        ]
                    )
                )
            ]
        )