from flet import *

class home(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return Column(
            controls=[
                Container(
                    height=800,
                    width=350,
                    bgcolor="red",
                    content=Column(
                        controls=[
                            Text('Welcome to the homepage'),
                            Container(
                                content=TextButton("Go to Login", on_click=lambda _: self.page.go("/login"))
                            )
                        ]
                    )
                )
            ]
        )