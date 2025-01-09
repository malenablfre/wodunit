import flet as ft

class startseite(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        head_container = ft.Column(
            spacing=0,
            controls=[
                # ----- ÜBERSCHRIFT -----
                ft.Container(
                        content=ft.Text(value="Whodunit?", size= 55, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
                        alignment=ft.alignment.center,
                    ),

                # ----- UNTER-ÜBERSCHRIFT -----
                ft.Container(
                    content=ft.Text(value="Das Spiel des Mörders", size= 25, font_family= "Times New Roman", weight= "bold", color="#801336"),
                    margin=0,
                    alignment=ft.alignment.center,
                )
            ],
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        body_container = ft.Column(
            spacing=0,
            controls=[
                # ----- BUTTONS -----
                ft.Container(
                    content=ft.ElevatedButton(
                        text="Deine Spiele", 
                        style=ft.ButtonStyle(
                            alignment=ft.alignment.center,
                            shape=ft.RoundedRectangleBorder(radius=10),
                            color="#EE4540", 
                            bgcolor="#510A32", 
                            text_style=ft.TextStyle(size= 20, font_family= "Times New Roman", weight= "bold"), 
                            overlay_color="#801336"
                        ),
                        width=250,
                        height=50,
                        on_click=lambda _: self.page.go("/gameslots")
                    ),
                    margin=10
                ),

                ft.Container(
                    content=ft.ElevatedButton(
                        text="Übersicht", 
                        style=ft.ButtonStyle(
                            alignment=ft.alignment.center,
                            shape=ft.RoundedRectangleBorder(radius=10),
                            color="#EE4540", 
                            bgcolor="#510A32", 
                            text_style=ft.TextStyle(size= 20, font_family= "Times New Roman", weight= "bold"), 
                            overlay_color="#801336"
                        ),
                        width=250,
                        height=50,
                        on_click=lambda _: self.page.go("/uebersicht")
                    ),
                    margin=10
                )
            ],
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        page_container = ft.Container(
            ft.Column(
                spacing=40,
                controls=[
                    head_container,
                    body_container
                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
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
        
        page = ft.Stack(
            controls=[
                page_container
            ]
        )

        return page