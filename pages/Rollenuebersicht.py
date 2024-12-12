import flet as ft

class Rollenuebersicht(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        page = ft.Container(
                ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
                        content=ft.Text(value="Rollenübersicht", size= 50, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
                        margin=5,
                        padding=5,
                    ),

                    ft.Container(
                        content=ft.Text(value="Rolle", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=7,
                        padding=7,
                    ),

                    ft.Container(
                        content=ft.Text(value="beschreibung", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=9,
                        padding=9,

                    ),

                    ft.Container(
                        content=ft.Text(value="Spiel beitreten", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        padding=10,
                        
                    ),

                    ft.Container(
                        content=ft.Text(value="Übersicht", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,
                        padding=10,
                        
                    ),
                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=400,
            height=700,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#2D142C","#510A32"]),
            border_radius=10,
            alignment=ft.alignment.center
            )
        return page