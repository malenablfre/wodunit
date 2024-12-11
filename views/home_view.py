import flet as ft

class home(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        page = ft.Container(
                ft.Column(
                spacing=0,
                controls=[
                    ft.Text(value="Whodunit?", size= 50, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
                    ft.Text(value="Das Spiel des Mörders", size= 25, font_family= "Times New Roman", weight= "bold", color="#801336"),

                    ft.Container(
                        content=ft.Text(value="Aktive Spiele", size= 20, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor="#510A32",
                        width=250,
                        height=50,
                        border_radius=10,
                        on_click=lambda _: self.page.go("/login")
                    ),

                    ft.Container(
                        content=ft.Text(value="Spiel beitreten", size= 20, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor="#510A32",
                        width=250,
                        height=50,
                        border_radius=10,
                        #on_click=
                    ),

                    ft.Container(
                        content=ft.Text(value="Übersicht", size= 20, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor="#510A32",
                        width=250,
                        height=50,
                        border_radius=10,
                        #on_click=
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            width=400,
            height=700,
            bgcolor="#2D142C",
            border_radius=10
            )
        return page