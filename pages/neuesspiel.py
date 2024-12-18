import flet as ft

class neuesspiel(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        # back_container = ft.Column(
        #     controls=[
        #         ft.Container(),
        #         ft.Row(
        #             controls=[
        #                 ft.Container(content=ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#EE4540", on_click=lambda _: self.page.go("/")),),
        #                 ft.Container(content=ft.Text(value="Spiele", size= 35, font_family= "Times New Roman", weight= "bold", color="#EE4540"),),
        #                 ft.Container(content=ft.IconButton(ft.Icons.MENU, icon_color="#EE4540", on_click=lambda _: self.page.go("/")),),
        #             ],
        #             alignment=ft.MainAxisAlignment.SPACE_AROUND,
        #         )
        #     ]
        # ),

        other_containers = ft.Column(
            spacing=10,  
            controls=[
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


                ft.Container(
                    content=ft.Text(value="Neues Spiel", size=30, font_family="Times New Roman", weight="bold", color="#EE4540"),
                    margin=10,
                    padding=10,
                ),

                ft.Container(
                    content=ft.Text(value="neues Spiel erstellen", size=20, font_family="Times New Roman", weight="bold", color="#C72C42"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor="#510A32",
                    width=250,
                    height=50,
                    border_radius=10,
                    ink=True,
                    on_click=lambda _: self.page.go("/spieleinstellungen")
                ),

                ft.Container(
                    content=ft.Text(value="Aktives Spiel", size=30, font_family="Times New Roman", weight="bold", color="#EE4540"),
                    margin=10,
                    padding=10,
                ),

                ft.Container(
                    content=ft.Text(value="Spiel beitreten", size=20, font_family="Times New Roman", weight="bold", color="#C72C42"),
                    margin=10,
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
        )

        background_container = ft.Container(
            content=other_containers,
            width=400,
            height=700,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#2D142C", "#510A32"]
            ),
            border_radius=10,
            alignment=ft.alignment.center
        )

        page = ft.Stack(
            controls=[
                background_container,  
                #back_container,  
            ]
        )

        return page