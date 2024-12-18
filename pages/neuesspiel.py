import flet as ft

class neuesspiel(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        page = ft.Stack([
            ft.Container(
            width=400,
            height=700,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#2D142C", "#510A32"]
            ),
            border_radius=10,
            alignment=ft.alignment.center
        ),

         ft.Column(
            spacing=10,
            controls=[
                ft.Container(height=170),

                ft.Container(
                    content=ft.Text(value="Neues Spiel", size=30, font_family="Times New Roman", weight="bold", color="#EE4540"),
                    margin=0,
                    padding=10,
                ),

                ft.Container(
                    content=ft.Text(value="Neues Spiel erstellen", size=20, font_family="Times New Roman", weight="bold", color="#C72C42"),
                    margin=0,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor="#510A32",
                    width=250,
                    height=50,
                    border_radius=10,
                    ink=True,
                    on_click=lambda _: self.page.go("/spieleinstellungen")
                ),

                ft.Container(height=40),

                ft.Container(
                    content=ft.Text(value="Aktives Spiel", size=30, font_family="Times New Roman", weight="bold", color="#EE4540"),
                    margin=0,
                    padding=10,
                ),

                ft.Container(
                    content=ft.Text(value="Spiel beitreten", size=20, font_family="Times New Roman", weight="bold", color="#C72C42"),
                    margin=0,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor="#510A32",
                    width=250,
                    height=50,
                    border_radius=10,
                    ink=True,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,  
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        ft.Column(
             controls=[
                ft.Container(),
                ft.Row(
                    controls=[
                        ft.Container(content=ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#EE4540", on_click=lambda _: self.page.go("/")),),
                        ft.Container(content=ft.Text(value="Spiele", size= 35, font_family= "Times New Roman", weight= "bold", color="#EE4540"),),
                        ft.Container(content=ft.IconButton(ft.Icons.MENU, icon_color="#EE4540", on_click=lambda _: self.page.go("/")),),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ]
        ),
        ])

        return page